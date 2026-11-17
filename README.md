# Quantum Clock Calibration Cost

**A quantum clock's intrinsic precision becomes a useful timing advantage only after its actual speed has been learned.** This project charges a temporary autonomous classical reference for that calibration, removes it during the unknown interval, and establishes the reference exposure and stable reuse needed to preserve an advantage.

The main obstruction applies even to a source that reads its own operational time without noise. For one unknown accessible speed, a reference supplying $`B_{\rm ref}`$ expected physical events leaves minimax elapsed-time risk of order

```math
R\ \gtrsim\ T^2
\min\left\{w^2,\frac1{\max(B_{\rm ref},1)}\right\}.
```

Here $`w>0`$ describes the fixed speed-uncertainty width and unknown intervals lie in $`[T/2,T]`$. The bound covers arbitrary biased decoders and correlated source output. The reference is an independent autonomous finite-state classical Markov device; no external timestamps, known-duration deadline or retained independent time standard is supplied.

## What survives calibration

Let $`G`$ bound complete modeled event activity and suppose calibration has mean duration at most $`cKT`$ for $`K`$ separately reported unknown intervals. For fixed nonzero prior width, the calibration obstruction imposes a universal $`O(K)`$ ceiling on gain over the optimal classical Markov timing scale.

An explicit protocol calibrates the actual signed current against a reference stopped after $`m`$ Poisson events, clips its learned current into a known positive range, then estimates elapsed time from the untimestamped signed count. Applied to the finite thermal-reset quantum family, it achieves

```math
R_{\rm Q}\ \le\ C\frac{T}{G}
\left[d^{-1+\eta}+\frac1K\right]
+\text{controlled finite and stability errors},
\qquad 0\lt \eta\lt 1,
```

and hence an attainable gain $`\Omega(\min\{K,d^{1-\eta}\})`$ over every allowed autonomous classical CTMC. This retains all source reset delays and reverse-event correlations.

| Result | Established scope |
|---|---|
| Universal calibration floor | Any source with one unknown accessible speed and any permitted classical-reference calibration method; finite minimax risk |
| Strong classical alternative | Arbitrary finite CTMC topology, hidden reset activity, complete untimestamped record and even exact rate calibration; optimal risk order $`T/G`$ |
| Explicit quantum protocol | Actual signed current, arbitrary startup state, misleading calibration records, retained calibration/use correlations and finite counters |
| Finite thermal regime | A conservative sufficient onset is $`gT/d^9\to\infty`$, with fixed exponents and $`g=\Theta(G)`$ |
| Reuse | Spreads calibration expense for fixed per-use risk; shared scale error remains correlated |
| Drift and reference bias | Unknown fractional mismatch produces an unavoidable squared-duration error floor |
| Detector | Ideal passive sign resolution is declared; loss and sign errors have explicit corrections |

To retain the displayed target risk, the reference's supplied fractional rate-certification error must satisfy $`\xi^2\lesssim[d^{-1+\eta}+1/K]/(GT)`$. The expense of creating that certification is a declared external-standard resource; the theorem does not derive a finite laboratory preparation cost for it. All gain statements use the same specified certification and detector access for both clock classes.

The universal ceiling is $`O(K)`$. The inherited signed-count construction supplies the displayed achievable gain; no separate claim of unrestricted intrinsic quantum optimality is made.

## Read the science

Start with the [scientific route](science/README.md) or the [worked interpretation](science/worked_example.md).

| To inspect | Read |
|---|---|
| Uncertain family, reference access and complete resource vector | [Model](science/model.md) |
| Stopped-reference relative entropy and arbitrary-decoder risk bound | [Reference converse](science/reference_converse.md) |
| Exact finite moment bound and clipped calibration/use protocol | [Finite protocol](science/finite_protocol.md) |
| Full classical comparison and necessary reuse law | [Classical comparison and reuse](science/classical_and_reuse.md) |
| Retained thermal generator, CP minorization and finite onset | [Thermal application](science/thermal_application.md) |
| Systematic reference error, drift, detector and memory constraints | [Drift and detection](science/drift_and_detection.md) |
| Inherited ingredients and limits of the literature comparison | [Related work](references/RELATED_WORK.md) and [references](references/REFERENCES.md) |

## Learn the project

The single educational anchor is **Landi, Kewming, Mitchison and Potts, Current Fluctuations in Open Quantum Systems (PRX Quantum 5, 020201, 2024)**. The [source bridge](learning/anchor_bridge.md) uses the published version's equation numbering, translates its signed-current and counting-field conventions, and explains the additional calibration and minimax steps supplied here.

The [30-milestone map](learning/milestones.md) builds from individual events and their correlations to the finite reference obstruction, robust signed-count protocol, thermal finite regime and stability-limited reuse. Its 12 background milestones and 18 narrative milestones express common understanding targets. The [learning overview](learning/README.md) gives routes through the source and project.

## Reproduce the finite checks

From the repository root, install [the declared requirements](verification/requirements.txt), then run:

```bash
python verification/check_calibration.py --output verification/results.json
```

The [verification guide](verification/README.md) describes independent moment/quadrature comparisons, a finite calibration register that retains the conditional source state, misleading signed records, reference likelihoods and drift examples. The small thermal examples check finite algebra. They do not certify practical onset, literature priority, or a microscopic detector/bath implementation.

## Scope and attribution

The unknown parameter is one common accessible dynamical speed. An exposed known carrier frequency, a detector with a usable known timing response, a timed gate, or an active reference retained during use changes that premise.

Poisson-reference calibration and signed/nonreset signal reconstruction are inherited from Nurgalieva, Silva and Renner. The quasiideal clock and finite thermal-reset timing advantage are inherited from the cited source accounts. The added account establishes the all-methods calibration obstruction, its necessary reuse consequence, and a finite signed-current route that approaches the bound.

The reference's rate-certification accuracy, finite initialized record memory, detector fidelity, bath resources and any register erasure remain explicit resources. The thermal theorem concerns its effective finite-dimensional GKLS generator and inherited limit order; it does not price a complete laboratory clock. The constructive onset is conservative, and drift during calibration is a separate tracking problem. The recent imperfect-reference characterization comparison is limited to accessible abstracts, as stated in the related-work account; no unqualified priority claim is made.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).

