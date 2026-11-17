"""Finite thermal-clock generator used by the calibration diagnostics.

The functions below are vendored from Ruge Lin's Quantum-Clock-Thermal-Reset,
verification/check_clock.py at commit
46b39e2bc0eb0afc88e2593d5b1cba514bb289a4:
https://github.com/GoGoKo699/Quantum-Clock-Thermal-Reset/blob/46b39e2bc0eb0afc88e2593d5b1cba514bb289a4/verification/check_clock.py

The original random finite cores test counting conventions; they are not the
asymptotic quasiideal clock family. The upstream license is preserved in the
repository's third-party notice. No source-repository changes are made here.
"""
from __future__ import annotations

import numpy as np
from scipy.linalg import solve

def vec(matrix: np.ndarray) -> np.ndarray:
    return np.asarray(matrix, dtype=complex).reshape(-1, order="F")


def unvec(vector: np.ndarray, n: int) -> np.ndarray:
    return vector.reshape((n, n), order="F")


def recycling(jump: np.ndarray) -> np.ndarray:
    return np.kron(jump.conj(), jump)


def dissipator(jump: np.ndarray) -> np.ndarray:
    n = jump.shape[0]
    effect = jump.conj().T @ jump
    return recycling(jump) - 0.5 * (
        np.kron(np.eye(n), effect) + np.kron(effect.T, np.eye(n))
    )


def commutator_generator(hamiltonian: np.ndarray) -> np.ndarray:
    n = hamiltonian.shape[0]
    return -1j * (
        np.kron(np.eye(n), hamiltonian)
        - np.kron(hamiltonian.T, np.eye(n))
    )


def constrained_solve(generator: np.ndarray, rhs: np.ndarray,
                      trace_value: float) -> tuple[np.ndarray, complex]:
    """Solve L x = rhs with tr(x) fixed, retaining every original row."""
    n = int(round(np.sqrt(rhs.size)))
    trace = vec(np.eye(n)).conj()
    reference = vec(np.eye(n) / n)
    bordered = np.zeros((rhs.size + 1, rhs.size + 1), dtype=complex)
    bordered[:-1, :-1] = generator
    bordered[:-1, -1] = reference
    bordered[-1, :-1] = trace
    target = np.concatenate((rhs, np.array([trace_value], dtype=complex)))
    solution = solve(bordered, target)
    return solution[:-1], solution[-1]


def make_core(d: int, g: float, seed: int) -> dict[str, np.ndarray]:
    """A reproducible full-rank, noncommuting, nonorthogonal-channel core."""
    rng = np.random.default_rng(seed)

    def random_complex(rows: int, columns: int) -> np.ndarray:
        return rng.normal(size=(rows, columns)) + 1j * rng.normal(
            size=(rows, columns)
        )

    raw_h = random_complex(d, d)
    hamiltonian = (raw_h + raw_h.conj().T) / 2
    spectrum = np.linalg.eigvalsh(hamiltonian)
    hamiltonian -= (spectrum[0] + spectrum[-1]) * np.eye(d) / 2
    hamiltonian *= 0.23 * g / np.linalg.norm(hamiltonian, 2)

    basis, _ = np.linalg.qr(random_complex(d, d))
    effect_eigenvalues = g * np.linspace(0.15, 0.72, d)
    root_effect = (basis * np.sqrt(effect_eigenvalues)) @ basis.conj().T
    isometry, _ = np.linalg.qr(random_complex(d + 2, d), mode="reduced")
    vectors = root_effect @ isometry.conj().T
    effect = vectors @ vectors.conj().T

    psi = random_complex(d, 1)[:, 0]
    psi /= np.linalg.norm(psi)
    return {"H": hamiltonian, "Q": effect, "vectors": vectors, "psi": psi}


def build_generator(core: dict[str, np.ndarray], g: float,
                    h: float, z: float) -> dict[str, np.ndarray | int | float]:
    d = core["H"].shape[0]
    n = d + 2
    m, e = d, d + 1
    ket = np.eye(n, dtype=complex)
    psi = np.zeros(n, dtype=complex)
    psi[:d] = core["psi"]
    carrier_gap = 0.9 * g
    carrier = np.diag([carrier_gap] * d + [0.0, 2 * carrier_gap])
    hamiltonian = carrier.astype(complex)
    hamiltonian[:d, :d] += core["H"]

    captures = []
    for column in core["vectors"].T:
        v = np.zeros(n, dtype=complex)
        v[:d] = column
        captures.append(np.outer(ket[:, m], v.conj()))
    hot_up = np.sqrt(g * h) * np.outer(ket[:, e], ket[:, m])
    hot_down = np.sqrt(g) * np.outer(ket[:, m], ket[:, e])
    release = np.sqrt(g) * np.outer(psi, ket[:, e])

    shape = (n * n, n * n)
    plus = sum((recycling(a) for a in captures), np.zeros(shape, complex))
    minus = z * sum((recycling(a.conj().T) for a in captures),
                    np.zeros(shape, complex))
    hot_current = recycling(hot_up) - recycling(hot_down)
    release_current = recycling(release) - z * recycling(release.conj().T)
    generator = commutator_generator(hamiltonian)
    effect = np.zeros((n, n), dtype=complex)
    pair_generators = []
    for a in captures:
        pair = dissipator(a) + z * dissipator(a.conj().T)
        generator += pair
        pair_generators.append(pair)
        effect += a.conj().T @ a + z * a @ a.conj().T
    hot_pair = dissipator(hot_up) + dissipator(hot_down)
    release_pair = dissipator(release) + z * dissipator(release.conj().T)
    generator += hot_pair + release_pair
    pair_generators.extend((hot_pair, release_pair))
    effect += hot_up.conj().T @ hot_up + hot_down.conj().T @ hot_down
    effect += release.conj().T @ release + z * release @ release.conj().T
    return {
        "n": n, "L": generator, "plus": plus, "minus": minus,
        "hot_current": hot_current, "release_current": release_current,
        "effect": effect, "start": vec(np.outer(ket[:, m], ket[:, m])),
        "pair_generators": np.array(pair_generators),
        "carrier_gap": carrier_gap,
    }


