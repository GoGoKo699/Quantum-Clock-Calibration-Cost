#!/usr/bin/env python3
"""Finite diagnostics for the calibration-paid clock results.

The checks use exact finite matrix formulas in floating point. They do not
certify the asymptotic family, a practical onset, or microscopic reservoirs.
Run: python verification/check_calibration.py --output verification/results.json
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import platform
from pathlib import Path

import numpy as np
import scipy
from scipy.integrate import quad
from scipy.linalg import eig, expm, solve
from scipy.special import roots_genlaguerre
from scipy.stats import gamma, nbinom

import thermal_model as thermal


class CheckFailure(RuntimeError):
    pass


class Checks:
    def __init__(self):
        self.count = 0
        self.max_errors = {}

    def require(self, condition, label):
        self.count += 1
        if not condition:
            raise CheckFailure(label)

    def close(self, actual, expected, tolerance, label):
        error = float(np.max(np.abs(np.asarray(actual)-np.asarray(expected))))
        self.max_errors[label] = max(error, self.max_errors.get(label, 0.0))
        self.require(np.isfinite(error) and error <= tolerance,
                     f"{label}: error {error:.5g} exceeds {tolerance:.5g}")
        return error


def moments_block(L, J1, J2):
    """Evolve density, count-weighted density, and count-square density."""
    q = L.shape[0]
    A = np.zeros((3*q, 3*q), complex)
    A[:q, :q] = L
    A[q:2*q, :q] = J1
    A[q:2*q, q:2*q] = L
    A[2*q:, :q] = J2
    A[2*q:, q:2*q] = 2*J1
    A[2*q:, 2*q:] = L
    return A


def read_moments(y, tr, checks):
    q = tr.size
    values = np.array([tr@y[:q], tr@y[q:2*q], tr@y[2*q:]])
    checks.close(values.imag, 0.0, 2e-7, "moment imaginary part")
    return values.real


def spectral_integral_envelope(L, n):
    """Conservative diagonalization bound; numerically checked, not intervals.

    For diagonalizable L, sum the absolute eigenmode norms. The factor sqrt(n)
    converts Hilbert--Schmidt output norm into trace norm. The zero eigenmode
    is excluded, leaving exp(Lt)-P. No well-conditioned basis is assumed.
    """
    values, vectors = eig(L)
    inverse = np.linalg.inv(vectors)
    stationary = int(np.argmin(np.abs(values)))
    if abs(values[stationary]) >= 1e-12:
        raise CheckFailure("No simple zero eigenmode found")
    m0, m1 = 0.0, 0.0
    for k, value in enumerate(values):
        if k == stationary:
            continue
        if value.real >= -1e-8:
            raise CheckFailure("Test generator is not strictly mixing")
        coefficient = (np.sqrt(n)*np.linalg.norm(vectors[:, k])
                       *np.linalg.norm(inverse[k, :]))
        m0 += coefficient/(-value.real)
        m1 += coefficient/value.real**2
    return float(m0), float(m1), float(np.linalg.cond(vectors))


def make_case(d, g, h, z, seed, checks):
    core = thermal.make_core(d, g, seed)
    source = thermal.build_generator(core, g, h, z)
    n, L = source["n"], source["L"]
    release_psi = np.zeros(n, complex)
    release_psi[:d] = core["psi"]
    source["release_state"] = thermal.vec(np.outer(release_psi, release_psi.conj()))
    source["q_min"] = float(np.linalg.eigvalsh(core["Q"]).min())
    J1, J2 = source["plus"]-source["minus"], source["plus"]+source["minus"]
    tr = thermal.vec(np.eye(n)).conj()
    rho, multiplier = thermal.constrained_solve(L, np.zeros(n*n, complex), 1.)
    j = float((tr@J1@rho).real)
    response, _ = thermal.constrained_solve(L, j*rho-J1@rho, 0.)
    D = float((tr@J2@rho+2*tr@J1@response).real)
    effect = float(np.linalg.eigvalsh(source["effect"]).max())
    checks.close(tr@L, 0., 2e-12, "trace preservation")
    checks.close(L@rho, 0., 2e-12, "stationary residual")
    checks.close(multiplier, 0., 2e-12, "stationary multiplier")
    checks.require(j > 0 and D >= 0, "positive current and count diffusion")
    checks.require(effect <= 2*g+1e-12, "complete jump budget")
    m0, m1, condition = spectral_integral_envelope(L, n)
    B = effect*m0+4*effect**2*m1+2*effect**2*m0**2
    rng = np.random.default_rng(seed+100)
    psi = rng.normal(size=n)+1j*rng.normal(size=n)
    psi /= np.linalg.norm(psi)
    starts = {"capture_reset": source["start"], "stationary": rho,
              "coherent": thermal.vec(np.outer(psi, psi.conj()))}
    return source, tr, rho, j, D, effect, m0, m1, B, condition, starts


def finite_source_checks(checks):
    cases = []
    for d, g, h, z, seed in [(2, 1.0, .2, .02, 2718),
                              (3, .7, .08, .012, 3141)]:
        source, tr, rho_ss, j0, D0, activity, m0, m1, B, cond, starts = (
            make_case(d, g, h, z, seed, checks))
        n, L0 = source["n"], source["L"]
        J10, J20 = source["plus"]-source["minus"], source["plus"]+source["minus"]
        summaries = []
        for a in [.7, 1., 1.4]:
            L, J1, J2, j, D = a*L0, a*J10, a*J20, a*j0, a*D0
            A, q = moments_block(L, J1, J2), n*n
            scaled_B = (a*activity*(m0/a)+4*(a*activity)**2*(m1/a**2)
                        +2*(a*activity)**2*(m0/a)**2)
            checks.close(scaled_B/B, 1., 2e-14, "scale-invariant transient B")
            max_envelope_ratio, max_cal_ratio = 0.0, 0.0
            for name, rho in starts.items():
                initial = np.concatenate([rho, np.zeros(2*q, complex)])
                for u in [.2, 2., 20., 200.]:
                    t = u/a
                    mass, mean, second = read_moments(expm(A*t)@initial, tr, checks)
                    mse = second-2*j*t*mean+(j*t)**2
                    envelope = D*t+B
                    checks.close(mass, 1., 3e-11, "finite-time normalization")
                    checks.require(mse >= -1e-8, "nonnegative centered count moment")
                    checks.require(mse <= envelope+1e-7, "finite signed-count envelope")
                    max_envelope_ratio = max(max_envelope_ratio, mse/envelope)
                kappa = .6*g
                step = kappa*solve(kappa*np.eye(3*q)-A, np.eye(3*q))
                for m in [3, 11, 40]:
                    s = m/kappa
                    mass, mean, second = read_moments(
                        np.linalg.matrix_power(step, m)@initial, tr, checks)
                    mse = second/s**2-2*j*mean/s+j*j
                    bound = 2*(D*s+B)/s**2+2*j*j/m
                    checks.close(mass, 1., 2e-9, "Gamma-stop normalization")
                    checks.require(mse >= -1e-9 and mse <= bound+1e-8,
                                   "nonstationary Gamma rate MSE")
                    if name == "stationary":
                        checks.close(mean, j*s, 1e-8*max(1., j*s),
                                     "stationary Gamma-stop mean")
                    max_cal_ratio = max(max_cal_ratio, mse/bound)
            # A separate integral calculation checks the resolvent power.
            m, kappa = 5, .6*g
            initial = np.concatenate([rho_ss, np.zeros(2*q, complex)])
            step = kappa*solve(kappa*np.eye(3*q)-A, np.eye(3*q))
            exact = read_moments(np.linalg.matrix_power(step, m)@initial, tr, checks)
            nodes, weights = roots_genlaguerre(32, m-1)
            integral = np.zeros(3)
            for node, weight in zip(nodes, weights):
                integral += (weight/math.gamma(m))*read_moments(
                    expm(A*(node/kappa))@initial, tr, checks)
            relative_error = float(np.max(np.abs(exact-integral)/np.maximum(1., np.abs(exact))))
            checks.require(relative_error < 3e-8, "Gamma moments: resolvent vs quadrature")
            summaries.append({"a": a, "max_count_mse_over_envelope": max_envelope_ratio,
                              "max_calibration_mse_over_bound": max_cal_ratio,
                              "Gamma_quadrature_relative_error": relative_error})
        cases.append({"core_dimension": d, "g": g, "h": h, "z": z,
                      "nominal_current": j0, "nominal_count_diffusion": D0,
                      "complete_activity": activity, "m0_bound": m0, "m1_bound": m1,
                      "count_transient_bound": B, "eigenbasis_condition": cond,
                      "scales": summaries})
    return cases


def finite_register_joint_check(checks):
    """Keep source state conditional on the actual finite calibration register.

    Fourier inversion gives the exact modulo-register state at the Gamma stop.
    It is then propagated into the unknown interval, retaining the correlation
    between learned current and clock state. The raw reciprocal estimator's
    risk bounds the risk after final projection onto the allowed time window.
    """
    source, tr, rho_ss, j0, D0, activity, _, _, B, _, _ = make_case(
        2, 1., .2, .02, 2718, checks)
    q, n = tr.size, source["n"]
    m, kappa, H, t = 3, .6, 255, 20.
    F, s = 2*H+1, m/kappa
    counts = np.arange(F)
    signed_counts = np.where(counts <= H, counts, counts-F)
    rows = []
    for a in [.7, 1.4]:
        L, plus, minus = a*source["L"], a*source["plus"], a*source["minus"]
        transforms = np.empty((F, q), complex)
        for k in range(F):
            phase = 2*np.pi*k/F
            tilted = L+(np.exp(1j*phase)-1)*plus+(np.exp(-1j*phase)-1)*minus
            step = kappa*solve(kappa*np.eye(q)-tilted, np.eye(q))
            transforms[k] = np.linalg.matrix_power(step, m)@source["start"]
        conditional_states = np.fft.fft(transforms, axis=0)/F
        probabilities = (conditional_states@tr).real
        checks.close(probabilities.sum(), 1., 2e-12, "modulo-register normalization")
        checks.require(probabilities.min() >= -2e-13, "modulo-register nonnegative probabilities")
        min_eigenvalue = min(float(np.linalg.eigvalsh(
            (thermal.unvec(rho, n)+thermal.unvec(rho, n).conj().T)/2).min())
                             for rho in conditional_states)
        checks.require(min_eigenvalue >= -2e-12, "conditional source-state positivity")
        j, D = a*j0, a*D0
        j_min, j_max = .7*j0, 1.4*j0
        estimates = np.clip(signed_counts/s, j_min, j_max)
        checks.require(np.all(estimates >= j_min) and np.all(np.isfinite(1/estimates)),
                       "misleading calibration cannot create a bad reciprocal")
        bad_mass = float(probabilities[signed_counts <= 0].sum())
        checks.require(bad_mass > .01, "test includes substantial zero/negative calibration mass")
        A = moments_block(L, plus-minus, plus+minus)
        propagated = expm(A*t)@np.vstack([conditional_states.T, np.zeros((2*q, F), complex)])
        first = (tr@propagated[q:2*q]).real
        second = (tr@propagated[2*q:]).real
        raw_risk = float(np.sum(second/estimates**2-2*t*first/estimates+t*t*probabilities))
        calibration_mse = float(np.sum((estimates-j)**2*probabilities))
        transfer_bound = 2/j_min**2*(D*t+B+t*t*calibration_mse)
        checks.require(raw_risk >= 0 and raw_risk <= transfer_bound+1e-5,
                       "joint calibration/use transfer with correlated source state")
        # Remove only the calibration/state correlation, keeping the same source
        # marginal. This is stronger than comparing with a stationary restart.
        source_marginal = conditional_states.sum(axis=0)
        independent_y = expm(A*t)@np.concatenate([source_marginal, np.zeros(2*q, complex)])
        _, independent_first, independent_second = read_moments(independent_y, tr, checks)
        discarded_state_risk = float(np.sum(probabilities*(
            independent_second/estimates**2-2*t*independent_first/estimates+t*t)))
        checks.require(abs(raw_risk-discarded_state_risk) > 1e-4,
                       "calibration/use state correlation has a detectable effect")
        # All physical events dominate both signed directions, hence also wraps.
        p = kappa/(kappa+a*activity)
        overflow_bound = float(nbinom.sf(H-1, m, p))
        cal_bound = 2*(D*s+B)/s**2+2*j*j/m+(j_max-j_min)**2*overflow_bound
        checks.require(calibration_mse <= cal_bound+1e-8,
                       "clipped calibration bound with register alias allowance")
        rows.append({"a": a, "reference_events": m, "register_values": F,
                     "probability_zero_or_negative_calibration": bad_mass,
                     "raw_estimator_MSE_with_retained_state": raw_risk,
                     "MSE_with_same_marginals_but_discarded_correlation": discarded_state_risk,
                     "transfer_bound": transfer_bound,
                     "source_event_overflow_bound": overflow_bound,
                     "minimum_conditional_state_eigenvalue": min_eigenvalue})
    return rows


def reference_and_drift_checks(checks):
    oracle, kl_rows, drift_rows = [], [], []
    for m in [3, 5, 20, 100]:
        for coefficient, tag in [(m-1, "unbiased"), (m-2, "biased_MSE_minimizer")]:
            # Integrate against the Gamma density, independently of inverse moments.
            density = lambda x: gamma.pdf(x, a=m)
            mean = quad(lambda x: coefficient/x*density(x), 0., np.inf,
                        epsabs=1e-11)[0]
            mse = quad(lambda x: (coefficient/x-1)**2*density(x), 0., np.inf,
                       epsabs=1e-11)[0]
            predicted_mean = coefficient/(m-1)
            predicted_mse = (1/(m-2) if tag == "unbiased" else 1/(m-1))
            checks.close(mean, predicted_mean, 2e-10, "oracle inverse-Gamma mean")
            checks.close(mse, predicted_mse, 2e-10, "oracle inverse-Gamma MSE")
            oracle.append({"m": m, "estimator": tag, "mean_over_t": mean,
                           "MSE_over_t_squared": mse})
        a0, a1, kappa = .7, 1.4, .6
        nodes, weights = roots_genlaguerre(32, m-1)
        u = nodes*a0/kappa
        log_ratio = (gamma.logpdf(u, a=m, scale=a0/kappa)
                     -gamma.logpdf(u, a=m, scale=a1/kappa))
        integral_kl = float(np.sum(weights*log_ratio)/math.gamma(m))
        predicted_kl = m*(math.log(a1/a0)-1+a0/a1)
        checks.close(integral_kl, predicted_kl, 2e-10, "stopped-reference Gamma KL")
        h = 1/(2*math.sqrt(m))
        checks.require(m*(math.log1p(h)-h/(1+h)) <= 1/8+1e-14,
                       "two-point KL stays below chosen testing threshold")
        kl_rows.append({"m": m, "integrated_KL": integral_kl,
                        "closed_form_KL": predicted_kl})
    for ell_t in [.001, .05, .5, 1.]:
        t0, ell = 7., ell_t/7.
        t1 = 2*t0/(1+math.sqrt(1+2*ell*t0))
        checks.close(t1+ell*t1*t1/2, t0, 2e-13, "drift-pair operational duration")
        exact_floor = (t0-t1)**2/4
        displayed_floor = ell**2*t0**4/81
        checks.require(exact_floor >= displayed_floor*(1-1e-10),
                       "finite Lipschitz-drift lower-bound constant")
        drift_rows.append({"ell_t0": ell_t, "t0": t0, "t1": t1,
                           "two_point_MSE_floor": exact_floor,
                           "displayed_lower_bound": displayed_floor})
    # Directly exercise the deterministic projection inequality on signed records.
    j_min, j_max, j_true, time = .7, 1.4, 1.1, 9.
    for calibration_record in [-10., -1., 0., .3, 2., 20.]:
        estimate_j = float(np.clip(calibration_record, j_min, j_max))
        for use_count in [-8., 0., 5., 10., 100.]:
            estimate_t = float(np.clip(use_count/estimate_j, 0., 12.))
            risk = (estimate_t-time)**2
            bound = 2/j_min**2*((use_count-j_true*time)**2
                               +time*time*(estimate_j-j_true)**2)
            checks.require(risk <= bound+1e-10, "pathwise clipped-reciprocal bound")
    return {"oracle": oracle, "KL": kl_rows, "drift": drift_rows}


def choi_input_output(superoperator, n):
    """Choi matrix with input-tensor-output order and column-vectorization.

    The (i,j) input block is S(|i><j|). Writing the blocks explicitly avoids
    relying on an implicit reshaping convention or a partial transpose.
    """
    choi = np.zeros((n*n, n*n), complex)
    for i in range(n):
        for j in range(n):
            choi[i*n:(i+1)*n, j*n:(j+1)*n] = thermal.unvec(
                superoperator[:, i+n*j], n)
    return choi


def minorization_checks(checks):
    """Numerically inspect the CP remainder in the thermal Doeblin lemma."""
    rows = []
    for d, g, h, z, seed in [(2, 1., .2, .02, 2718),
                              (3, .7, .08, .012, 3141)]:
        source, tr, _, _, _, _, _, _, _, _, _ = make_case(
            d, g, h, z, seed, checks)
        n, L, tau = source["n"], source["L"], 1/g
        epsilon = (source["q_min"]/g)*h*math.exp(-2)/72
        # sigma=(2/tau) int_0^(tau/2) exp(Lu) P_psi du. Gauss--Legendre
        # integrates the actual finite semigroup, not the minorization formula.
        nodes, weights = np.polynomial.legendre.leggauss(32)
        sigma = sum((weight/2)*expm(L*(tau*(node+1)/4))@source["release_state"]
                    for node, weight in zip(nodes, weights))
        sigma_matrix = thermal.unvec(sigma, n)
        sigma_hermitian = (sigma_matrix+sigma_matrix.conj().T)/2
        sigma_min = float(np.linalg.eigvalsh(sigma_hermitian).min())
        checks.close(tr@sigma, 1., 3e-12, "replacement-state trace")
        checks.close(sigma_matrix-sigma_matrix.conj().T, 0., 3e-12,
                     "replacement-state Hermiticity")
        checks.require(sigma_min >= -3e-12, "replacement-state positivity")
        replacement = np.outer(sigma, tr)
        checks.close(choi_input_output(replacement, n), np.kron(np.eye(n), sigma_matrix),
                     1e-14, "Choi replacement-channel convention")
        omega = np.eye(n).reshape(-1)
        checks.close(choi_input_output(np.eye(n*n), n), np.outer(omega, omega),
                     1e-14, "Choi identity-channel convention")
        remainder = expm(L*tau)-epsilon*replacement
        choi = choi_input_output(remainder, n)
        checks.close(choi-choi.conj().T, 0., 3e-12, "minorization-remainder Hermiticity")
        minimum = float(np.linalg.eigvalsh((choi+choi.conj().T)/2).min())
        checks.require(minimum >= -3e-12, "minorization-remainder complete positivity")
        checks.close(tr@remainder, (1-epsilon)*tr, 3e-12,
                     "minorization-remainder trace weight")
        rows.append({"core_dimension": d, "tau": tau, "q_min": source["q_min"],
                     "epsilon": epsilon, "minimum_sigma_eigenvalue": sigma_min,
                     "minimum_remainder_Choi_eigenvalue": minimum,
                     "quadrature": "32-point Gauss-Legendre"})
    return rows


def run():
    checks = Checks()
    cases = finite_source_checks(checks)
    joint = finite_register_joint_check(checks)
    reference = reference_and_drift_checks(checks)
    minorization = minorization_checks(checks)
    root = Path(__file__).resolve().parent
    return {"status": "passed", "check_count": checks.count,
            "versions": {"python": platform.python_version(), "numpy": np.__version__,
                         "scipy": scipy.__version__},
            "source_commit": "46b39e2bc0eb0afc88e2593d5b1cba514bb289a4",
            "input_sha256": {name: hashlib.sha256((root/name).read_bytes()).hexdigest()
                             for name in ["check_calibration.py", "thermal_model.py"]},
            "maximum_absolute_errors": checks.max_errors,
            "thermal_cases": cases, "finite_register_joint_checks": joint,
            "reference_and_drift": reference, "minorization_checks": minorization,
            "limitations": ["Floating-point diagnostics, not certified intervals or a proof checker.",
                            "Finite random thermal cores are not the asymptotic quasiideal family.",
                            "Conservative transient bounds do not demonstrate practical onset.",
                            "No microscopic reservoir, detector engineering, or priority claim."]}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=Path(__file__).with_name("results.json"))
    args = parser.parse_args()
    result = run()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({"status": result["status"], "check_count": result["check_count"],
                      "thermal_cases": len(result["thermal_cases"]),
                      "max_Gamma_quadrature_relative_error": max(
                          x["Gamma_quadrature_relative_error"]
                          for c in result["thermal_cases"] for x in c["scales"])}))


if __name__ == "__main__":
    main()
