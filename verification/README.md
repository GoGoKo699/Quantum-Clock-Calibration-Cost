# Finite verification

[Scientific overview](../science/README.md) · [Finite protocol](../science/finite_protocol.md)

These diagnostics check finite counting formulas and consequential failure modes
of the calibration estimator. They support the conventions and implementations;
the written arguments establish the general lower bounds and asymptotic claims.

## Reproduce

The recorded run used Python 3.12.14 and the exact library versions in
[requirements.txt](requirements.txt). From the repository root:

```bash
python -m pip install -r verification/requirements.txt
python verification/check_calibration.py --output verification/results.json
```

The command exits with an error if a declared tolerance fails. The saved
[results](results.json) include the source hashes, library versions, residuals,
and numerical scope. They are finite floating-point diagnostics, rather than
interval certificates.

## What is tested

| Calculation | Independent comparison or failure mode |
|---|---|
| Finite signed-count mean and second moment | Different initial states, finite reverse captures, actual reset delays, and three common speed scales |
| Uniform transient envelope | Centered count moments are compared with the diffusion-plus-transient bound; the bound is invariant under a common speed change |
| Gamma-stopped calibration | Resolvent powers of the moment generator agree with direct generalized Gauss–Laguerre integration over the reference duration |
| Retained calibration/use correlation | An exact finite modulo register retains the source state conditioned on its calibration count, then propagates that state into the unknown interval |
| Misleading calibration records | The finite register has substantial zero or negative signed calibration probability; clipping keeps every reciprocal current finite |
| Finite counter error | The mixed-Poisson/negative-binomial physical-event tail bounds the possibility of a signed-register wrap |
| Thermal CP minorization | The replacement state is integrated from the actual release-state semigroup; its trace/positivity and the complete positivity and trace weight of the subtracted channel are inspected |
| Reference lower bound | Integrating Gamma likelihood ratios agrees with the stopped-reference KL expression and its finite two-point threshold |
| Sharp oracle example | Integrating inverse-Gamma estimators gives both the unbiased variance and the lower-MSE biased estimator |
| Unknown drift | Two different physical durations with a Lipschitz speed change have equal operational durations and satisfy the displayed two-point risk bound |

The finite thermal examples use core dimensions 2 and 3. Their random full-rank
cores are deliberately small algebra tests, not instances of the large-dimension
quasiideal advantage construction. A positive core absorption floor, all reverse
channels, and both reset states remain in their generators.

The correlated calculation uses a 511-value modulo calibration register stopped
at three reference events. It compares the actual retained source state with a
product reconstruction having exactly the same source and calibration marginals.
This checks the effect of the correlation itself. It does not assume a
stationary restart after calibration. Its use estimate is evaluated before the
final projection onto the allowed time window, so it also upper-bounds the risk
after that projection.

The minorization diagnostic constructs the Choi matrix in explicit
input-tensor-output order: its input block `(i,j)` is the image of
`|i><j|`. Identity and replacement-channel conventions are checked before
testing the thermal remainder. These floating-point finite Choi checks support
the implementation; they do not replace the analytical CP minorization proof.

## Limits of the evidence

The spectral transient bounds are conservative: the two tested bounds are about
39,741 and 276,640 in squared-count units. Passing them is not evidence that a
laboratory clock reaches its asymptotic accuracy quickly. The sufficient
dimension-dependent onset is an analytical result in the
[thermal application](../science/thermal_application.md), not a fit to these
examples.

Neither test count nor numerical agreement establishes literature priority,
asymptotic optimality, a microscopic reservoir implementation, or an efficient
detector. Detector efficiency, reference certification accuracy, and memory
preparation/erasure remain explicit model assumptions and resources in the
scientific account.

## Source attribution

[thermal_model.py](thermal_model.py) vendors the finite generator and linear
algebra helpers from Ruge Lin's
[Quantum-Clock-Thermal-Reset verification code](https://github.com/GoGoKo699/Quantum-Clock-Thermal-Reset/blob/46b39e2bc0eb0afc88e2593d5b1cba514bb289a4/verification/check_clock.py),
pinned to commit `46b39e2bc0eb0afc88e2593d5b1cba514bb289a4`.
The upstream copyright and license notice are retained in this directory's
third-party notice. The calibration, finite-register, reference-KL and drift
diagnostics are specific to this repository.
