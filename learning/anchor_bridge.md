# From current fluctuations to calibrated timekeeping

[Learning route](README.md) · [30 milestones](milestones.md) · [Scientific route](../science/README.md)

The educational anchor is **Gabriel T. Landi, Michael J. Kewming, Mark T. Mitchison and Patrick P. Potts, _Current Fluctuations in Open Quantum Systems: Bridging the Gap Between Quantum Continuous Measurements and Full Counting Statistics_, PRX Quantum 5, 020201 (2024)**, DOI [10.1103/PRXQuantum.5.020201](https://doi.org/10.1103/PRXQuantum.5.020201).

The section and equation numbers below refer to the **published article of 2 April 2024**, not the later revised arXiv text. They were checked against the [author-hosted published version](https://www.pas.rochester.edu/~gtlandi/download/prxquantum.5.020201.pdf). This route uses the jump-current, correlation, counting-statistics and auxiliary-equation parts. It does not require reading every application in the tutorial.

## 1. A source-to-project route

| Published source | Use in this project |
|---|---|
| II.A, Eqs. (5)–(7): master equation and stationary state | Specify the complete source generator in [model](../science/model.md). |
| II.C–D, especially Eq. (37); II.D.1 | Assign signed capture weights and state the detection instrument. |
| III.A, Eqs. (67)–(70) | Separate instantaneous count noise from delayed source correlations. |
| III.C, Eqs. (85)–(92) | Relate integrated-count variance, noise and a current average. |
| IV.A, Eqs. (113)–(118); IV.C–D | Differentiate a tilted generator for signed-count moments. |
| V.A, Eqs. (148)–(152); V.B–C | Connect moment propagation and stationary linear solves to [verification](../verification/README.md). |

Sections VI.A–B provide optional context on waiting times, path probabilities and renewal processes. The present source's signed record requires the joint reverse-event/duration account; positive-capture waiting times alone do not determine its noise.

## 2. Translate the notation before using a formula

Use $`\mathcal J_\alpha(X)=L_\alpha X L_\alpha^\dagger`$ for a physical jump map. A mark $`s_\alpha`$ records what the decoder counts: $`+1`$, $`-1`$ or $`0`$. Define

```math
\mathcal J_1=\sum_\alpha s_\alpha\mathcal J_\alpha,
\qquad
\mathcal J_2=\sum_\alpha s_\alpha^2\mathcal J_\alpha.
```

| Source notation | Project notation or convention |
|---|---|
| Channel weight $`\nu_k`$ | Signed increment $`s_\alpha`$ |
| Current superoperator $`\mathcal J`$ in Eq. (69) | $`\mathcal J_1`$ |
| Mean current $`J`$ | $`j=\mathrm{Tr}\mathcal J_1(\rho_{\rm ss})`$ |
| White-noise coefficient $`K`$ in Eq. (68) | $`k=\mathrm{Tr}\mathcal J_2(\rho_{\rm ss})`$; project $`K`$ instead counts future uses |
| Smooth part of the stationary current covariance | $`C(v)`$ below; the singular zero-lag term is kept separately |
| Long-time noise $`D`$ | Signed-count diffusion $`D_N`$ |
| Generalized state $`\rho_\chi`$ with Fourier field | Translate to the real moment-generating field used here before differentiating |

The diffusion convention is

```math
D_N=\lim_{t\to\infty}\frac{\mathrm{Var}N(t)}t,
\qquad D_{\rm time}=\frac{D_N}{j^2}.
```

There is no extra factor of two in $`D_N`$. Also, $`k`$ is the activity of the **counted marks**. The complete physical event bound $`\Lambda`$ additionally includes jumps with mark zero, such as thermal recycling.

For the tilted generator, this project's real field gives

```math
\mathcal L(\chi)=\mathcal L+
\sum_\alpha(e^{s_\alpha\chi}-1)\mathcal J_\alpha,
\qquad
\mathcal L'(0)=\mathcal J_1,\qquad
\mathcal L''(0)=\mathcal J_2.
```

The source's Fourier convention has $`e^{i\nu_k\chi_{\rm F}}`$ instead. At zero field its derivatives are $`i\mathcal J_1`$ and $`-\mathcal J_2`$. Equivalently set $`\chi_{\rm F}=-i\chi`$. Mixing these conventions would give incorrect signs or imaginary factors in a real variance.

## 3. A signed record contains more than positive ticks

Suppose a record contains four captures with signs $`+1,-1,+1,+1`$. Its net count is $`N=2`$, although four capture events occurred. The opposite signs cancel in the mean record. They do not erase their waiting time, their effect on the clock state, or their contribution to detector noise.

The map $`\mathcal J_2`$ squares each individual event's mark. A reverse capture therefore contributes positively to it. It is not the product $`\mathcal J_1^2`$, which describes two successive marked actions.

For a mixing source put $`\mathcal P(X)=\rho_{\rm ss}\mathrm{Tr}X`$ and define

```math
C(v)=\mathrm{Tr}\!\left[
\mathcal J_1(e^{v\mathcal L}-\mathcal P)
\mathcal J_1(\rho_{\rm ss})\right].
```

Then the actual signed noise is

```math
D_N=k+2\int_0^\infty C(v)\,dv.
```

The integral can increase or reduce the noise. Independence of positive ticks, reverse ticks and reset delays is not assumed. The [finite protocol](../science/finite_protocol.md#1-generator-output-and-finite-mixing-integrals) gives the exact moment identities used in this repository.

## 4. Turning a count into time requires a scale

If the actual current $`j`$ were known, dividing the count by $`j`$ would convert source progress to physical time. Its long-time variance would grow as $`D_{\rm time}t`$. This is the calibrated-clock starting point.

Here $`\mathcal L_a=a\mathcal L_0`$ with unknown $`a`$. All allowed source observations depend on physical duration through $`u=at`$. Without an independent standard, speeding the source up and shortening the interval can leave the entire accessible record unchanged. A narrow tick distribution does not remove that ambiguity.

Calibration supplies that standard temporarily. Stop an independent Poisson reference after $`m`$ events, with declared actual rate $`\kappa`$. Its physical duration is random:

```math
S\sim\mathrm{Gamma}(m,\kappa),
\qquad s=\mathbb ES=m/\kappa,
\qquad \mathrm{Var}S=s^2/m.
```

The decoder knows $`m`$ and the reference specification, not the actual $`S`$. Thus the current average over an exactly known observation time cannot simply be used with $`S=s`$.

The constructive estimate is $`\widetilde j=N(S)/s`$, projected into a known interval $`[j_{\min},j_{\max}]`$ with $`j_{\min}>0`$. This projection keeps the reciprocal finite even when a short signed calibration record is zero or negative. Reference rate-certification error remains a separate systematic resource. The Poisson-reference calibration architecture is inherited from the [cited clock-signal reconstruction work](../references/RELATED_WORK.md).

## 5. The bridge beyond the anchor

The following steps belong to the present scientific account, rather than being conclusions imported from the tutorial:

| Additional step | Why it is needed | Proof route |
|---|---|---|
| Operational-time oracle and stopped reference likelihood | Bound every admissible calibration method, even for a noiseless quantum source | [Reference converse](../science/reference_converse.md) |
| Arbitrary-startup finite envelope | Control finite records and the state retained after calibration | [Finite protocol, section 2](../science/finite_protocol.md#2-a-uniform-bound-for-every-initial-state) |
| Clipped reciprocal estimator | Include misleading calibration records without dividing by zero | [Finite protocol, sections 4–5](../science/finite_protocol.md#4-calibration-without-a-known-physical-deadline) |
| Complete classical comparison | Permit a full untimestamped CTMC record and its best decoder | [Classical comparison](../science/classical_and_reuse.md) |
| Reference exposure and stable reuse | Determine when the inherited quantum timing gain can survive its setup expense | [Reuse consequence](../science/classical_and_reuse.md#4-a-universal-ceiling-from-calibration-overhead) |
| Drift, detector and finite-memory allowances | State when a small intrinsic noise coefficient remains useful | [Drift and detection](../science/drift_and_detection.md) |

The finite envelope has the form

```math
\mathbb E_\rho[(N(t)-jt)^2]\le D_Nt+B_0
```

for **every** initial density matrix. Conditioning on calibration leaves some source state, so this uniform bound applies even when that state and the learned current are correlated. It avoids treating calibration and use as independent experiments.

The reference converse instead needs no source mixing assumption. It gives a finite minimax floor of order $`t^2/B_{\rm ref}`$ at fixed nonzero scale uncertainty, where $`B_{\rm ref}`$ is paid expected reference activity. Combined with the classical benchmark, bounded setup expense across $`K`$ arbitrary uses yields the universal $`O(K)`$ gain ceiling.

The thermal signed-count construction reaches that order until its inherited gain is recovered, under its explicit finite-onset and supplied-resource conditions. Reuse spreads expense; the shared scale error remains correlated and limits cumulative elapsed-time precision. These qualifications belong beside the result, including when approaching it through the selected source.

