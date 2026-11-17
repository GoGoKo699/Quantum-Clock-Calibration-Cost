# Model, observations and charged resources

[Scientific route](README.md) · [Reference converse](reference_converse.md) · [Finite protocol](finite_protocol.md)

A regular tick train need not be an accurate physical stopwatch when its actual speed is unknown. This project separates learning that speed from using the device after the calibration reference has been removed.

## 1. One unknown accessible speed

Let $`\mathcal L_0`$ be a specified finite-dimensional GKLS generator with marked physical jump maps
$`\mathcal J_{\alpha,0}(\rho)=L_{\alpha,0}\rho L_{\alpha,0}^{\dagger}`$.
An unknown constant $`a\in[a_-,a_+]`$, with $`0<a_-<a_+<\infty`$, determines

```math
\mathcal L_a=a\mathcal L_0,\qquad
H_a=aH_0,\qquad L_{\alpha,a}=\sqrt a\,L_{\alpha,0}.
```

Every accessible source time scale shares this unknown factor. Its trajectory over physical time $`t`$ is the nominal trajectory over operational time $`u=at`$. The initial state and any untimed observation instrument are independent of $`a`$.

More generally, the converse requires only this scaling property for the allowed source observations. It can include an arbitrary quantum state readout when the entire accessible generator scales. For the thermal realization used here the constructive decoder reads signed capture events only. Its carrier Hamiltonian is invisible to that record; arbitrary measurements that expose a known unscaled carrier are additional reference access and do not belong to that count-only model.

The family holds the nominal generator's shape fixed. It does not allow independently uncertain thermal ratios, Hamiltonian matrix elements and detector parameters and then treat them as identified by one scalar estimate.

Assign increments $`s_\alpha\in\{-1,0,+1\}`$ and let $`N_a(t)`$ be their signed sum. For a unique mixing stationary state $`\rho_{\rm ss}`$, write

```math
j_a=aj_0>0,\qquad
D_{N,a}=aD_{N,0},\qquad
D_{{\rm time},a}=\frac{D_{N,a}}{j_a^2}.
```

There is no factor of two in the diffusion convention:
$`D_{N,a}=\lim_{t\to\infty}{\rm Var}(N_a(t))/t`$.
The useful timing variance coefficient is $`D_{\rm time}`$, rather than tick regularity at fixed tick number alone.

## 2. Calibration without free timestamps

An independent autonomous finite-state classical Markov reference is available only during calibration. Its known transition structure includes a declared absolute rate certification. Its aggregate instantaneous event intensity is bounded by $`\kappa`$. All physical reference transitions, resets and recorded self-events are included; multiple channels do not receive independent copies of the rate allowance.

Calibration can read interleaved source/reference marks and use an integrable stopping rule adapted to those observations. A physical duration $`S`$ exists, but the experimenter receives neither exact physical timestamps nor a free deterministic-duration stopping signal. Denote

```math
s=\mathbb E S,\qquad
B_{\rm ref}=\mathbb E A_{\rm ref}(S)\le\kappa s.
```

The constructive reference stops after $`m`$ Poisson events, so $`B_{\rm ref}=m`$ exactly and $`S\sim{\rm Gamma}(m,\kappa)`$. Its duration standard deviation is $`s/\sqrt m`$. This specifies a finite stochastic timer, not an exact calibration interval.

A certified fractional reference-rate error $`\xi`$ is distinct from this stochastic uncertainty. The exact-rate model sets $`\xi=0`$ as a declared input assumption. For $`\xi>0`$, the [scale obstruction](drift_and_detection.md) must be included. No finite-resource laboratory certification of an exactly known transition rate is claimed.

## 3. Use after removal of the reference

After calibration the reference has no active dynamics accessible to the decoder. Static calibration data and the source's conditional state may be retained. A retained known-rate oscillator, detector response time or external schedule would be another reference and changes the experiment.

The task supplies external start and end markers for $`K`$ durations $`t_1,\ldots,t_K`$. These markers carry no numerical timestamps. The durations are arbitrary fixed values in a declared window such as $`[T/2,T]`$, or externally sampled independently of clock noise. They are not stopping times chosen from the source jump record. No known duration distribution, known sum, known equality, or label encoding an interval's value is supplied.

During each interval the decoder obtains untimestamped source marks or their finite signed-counter value. It returns one estimate per duration. The comparison uses average per-use squared risk, with a supremum over the allowed source scale and duration vector. This makes statements about biased estimators meaningful; no nonzero pointwise risk lower bound could hold at every individual time.

The [reference converse](reference_converse.md) gives even more source information than this protocol uses: exact operational durations and operational-coordinate source histories. The impossibility result therefore does not depend on restricting a quantum decoder to a linear count estimate.

## 4. Complete modeled resource vector

| Resource | Charge or assumption |
|---|---|
| Source physical activity | $`\sum_\alpha L_{\alpha,a}^{\dagger}L_{\alpha,a}\le\Lambda I`$, including all reset and reverse channels |
| Simultaneous calibration activity | Source plus reference and any timing-active auxiliaries obey a common bound $`G`$; the construction uses fixed fractions for $`\Lambda`$ and $`\kappa`$ |
| Coherent dynamics | Bound the active source Hamiltonian separately; a thermal carrier's bare energy width is a further resource |
| Reference exposure | $`B_{\rm ref}`$, $`s`$, peak $`\kappa`$, certification error $`\xi`$, finite reference state count and initialization |
| Source implementation | Core dimension, static engineered channels, bath temperatures/ratios and energy gaps |
| Record memory | Finite signed-counter ranges, countdown states, saved offsets and integer calibration record; declare overflow/alias probability |
| Record preparation and reuse | Fresh initialized registers or an explicit reset/erasure schedule; no free cyclic memory reset |
| Detector | Ideal passive sign-resolving marks for the main construction; efficiency and sign errors are treated separately |
| Numerical output | Finite arithmetic and output resolution can be charged by a deterministic approximation allowance |

The register update may be part of the same physical jump: replacing $`L_\alpha`$ by $`L_\alpha\otimes U_\alpha`$ for a finite cyclic shift leaves its effect $`L_\alpha^\dagger L_\alpha\otimes I`$ unchanged. This accounts for ideal passive record routing within the effective model. It does not manufacture a physical detector amplifier or establish a thermodynamic erasure protocol.

Store integer $`C`$ and $`m`$; the construction does not require a perfect real-valued memory of an estimated frequency. With a final deterministic time-rounding error at most $`\epsilon_{\rm out}`$, an ideal-decoder risk bound $`R`$ becomes at most $`2R+2\epsilon_{\rm out}^2`$. Approximating rate-certification constants also needs its own systematic error allowance.

## 5. Matched classical clocks

The classical class consists of arbitrary finite-state autonomous continuous-time Markov networks, with arbitrary topology and hidden transitions, subject to the same complete modeled event-rate, memory and initialization limits. Give them perfect access to their entire untimestamped state/mark sequence and equivalent calibration access. The proof can also grant exact known rates: this strengthens the benchmark against which the quantum construction succeeds.

A deterministic classical phase oscillator or non-Markov memory kernel is outside this CTMC class. An unobserved reset is still a physical event and consumes the rate budget. Static extra states cannot evade a bound on the total rate out of each complete-device state.

The comparison is a theorem in this explicit resource model. It is not a claimed advantage over every macroscopic classical oscillator or over a laboratory clock with unlimited calibration and detector resources.

