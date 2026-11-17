# Classical timing and the cost of reuse

[Reference converse](reference_converse.md) · [Overview](../README.md)

The comparison is with complete autonomous classical Markov clocks, including hidden states, resets, all physical event channels, and the whole untimestamped output record. A simple event clock already attains the relevant classical order. Complicated Markov networks cannot evade the comparison by choosing a better decoder.

## 1. Complete-device classical benchmark

Let a finite-state time-homogeneous continuous-time Markov clock have total physical event intensity at most $G$ in every internal state. Observable marked self-events are included. The state may include its clockwork, reset machinery, counters, and any retained timing-active auxiliary. Grant its decoder every visited state and every physical event label, without external timestamps. Any actually supplied coarser record is less informative.

The initialization and static calibration record may be arbitrary but cannot encode the unknown task duration. For the strongest benchmark, give the decoder exact knowledge of all rates at no calibration cost. Bounds for this stronger experiment apply also when rates must first be learned.

**Uniformization lemma.** For a duration $t$, the full untimestamped record is a parameter-independent channel of

```math
Z\sim\mathrm{Poisson}(Gt).
```

**Proof.** Generate opportunity events at rate $G$. In state $x$, use the fixed probabilities $q_{xy}/G$ for physical marked events and use the remaining probability for an unobserved null event. Given $Z$, draw the discrete marked chain for exactly $Z$ opportunities and delete null events. These transition probabilities and the deletion rule do not depend on $t$. The final state can also be revealed. This constructs the asserted channel.

The same construction covers calibration-dependent initial states by conditioning on the calibration record. An arbitrary initial state distribution supplies no task-time information if it is independent of the unknown duration. For several externally delimited uses with retained classical memory, the full joint record is a channel of independent opportunity counts $Z_i\sim\mathrm{Poisson}(Gt_i)$ and parameter-independent randomness. Internal memory makes their processing correlated, not their opportunity rates.

## 2. A finite bound for arbitrary biased decoders

Consider $K$ arbitrary durations in $[T/2,T]$, with $GT\ge1$. Define average squared loss as in the [reference theorem](reference_converse.md#4-unknown-time-minimax-bound). For every such complete classical clock and every joint decoder,

```math
\sup_{\boldsymbol t\in[T/2,T]^K}
\frac1K\sum_{i=1}^K\mathbb E(\widehat t_i-t_i)^2
\ge\frac{3T}{512G}.
```

The statement is finite and allows bias. It does not require stationarity or an asymptotic central limit theorem.

**Proof.** The uniformization oracle is more informative than the clock. In that oracle choose a product prior with independent equal probabilities on

```math
t_i\in\{\tau,\tau+h\},
\qquad \tau=T/2,
\qquad h=\frac14\sqrt{T/G}.
```

Both alternatives lie in the time window. For the two scalar Poisson laws,

```math
D_{\mathrm{KL}}
\bigl(\mathrm{Pois}(G\tau)
\Vert\mathrm{Pois}(G(\tau+h))\bigr)
=G\left[h-\tau\log(1+h/\tau)\right]
\le\frac{Gh^2}{2\tau}=\frac1{16}.
```

Their total variation is therefore at most $1/4$. The nearest-point testing bound makes the scalar Bayes squared error at least $3h^2/32=3T/(512G)$. Under the product prior the oracle posterior factors by coordinate, so all other opportunity counts give no information about $t_i$. The same lower bound holds for each coordinate of any joint estimator and hence for their average. The worst-point risk exceeds the Bayes risk, proving the claim.

For one use this is the usual two-point lower bound. For $K$ uses, the product prior is essential: changing only one duration in a single two-point argument would incorrectly lose a factor $K$ in the average loss.

A counted Poisson event process of known rate $G$, equivalently a constant-escape marked two-state telegraph clock, gives $\widehat t=Z/G$ and

```math
\mathbb E(\widehat t-t)^2=\frac{t}{G}\le\frac{T}{G}.
```

Thus the optimal classical minimax order is $T/G$, subject to sufficient finite count memory. The lower bound permits arbitrary dimension, so allowing the classical device every state and register used by the quantum implementation cannot improve this order.

This benchmark credits the known classical information limitation. In particular, [Prech et al., *Optimal Time Estimation and the Clock Uncertainty Relation for Stochastic Processes*, PRX 15, 031068 (2025)](https://doi.org/10.1103/rpls-mp8z) derives the asymptotically optimal untimestamped estimator and finite-time information bounds. Uniformization supplies the elementary finite biased-minimax form needed here; it is not presented as a new classical uncertainty relation.

## 3. Equivalent calibration access for the classical device

The oracle-calibrated comparison deliberately favors the classical device. There is also a matching classical protocol when its source speed is uncertain in the same fixed interval $[a_-,a_+]$ and it receives the same finite classical reference.

Take a Poisson source with actual rate $\lambda=a\lambda_0$. Choose $\lambda_0$ and reference rate $\kappa$ so that

```math
a_+\lambda_0+\kappa\le G,
\qquad a_-\lambda_0=\Theta(G),
\qquad\kappa=\Theta(G).
```

Thus simultaneous source and reference activity during calibration obeys the same complete budget. Stop at reference event $m$, set $s=m/\kappa$, clip the learned source rate into $[a_-\lambda_0,a_+\lambda_0]$, and use the clipped reciprocal count estimator for each unknown interval. Direct Poisson moments, or the general signed-count bound with $D_N=\lambda$ and zero startup remainder, give

```math
\mathrm{risk}_{\mathrm C}
\le C\left[
\frac{T}{G}+
\frac{T^2}{Gs}+
\frac{T^2}{\kappa s}
\right]
+\text{finite-counter error}.
```

Here $C$ depends only on the fixed prior ratio and chosen rate fractions. For $s=cKT$ with fixed $c>0$ and $K\ge1$, this is $O(T/G)$. The previous lower bound still applies because even exact calibration cannot do better in order. Consequently the equally uncertain classical comparator also has minimax order $T/G$ under this access and overhead convention.

The finite reference and source registers are charged on both sides. A finite Poisson counter suffices after allocating an explicit overflow error; a known infinite counter is not being supplied as a free device. If a proposed physical realization adds detector or register-reset events, their activity must be included in $G$.

## 4. A universal ceiling from calibration overhead

Suppose calibration must satisfy

```math
\sup_a\mathbb E_a S\le cKT,
\qquad\kappa\le G,
```

where $c>0$ is fixed. It follows that its expected charged reference-event count is at most $cGKT$. The [reference converse](reference_converse.md#4-unknown-time-minimax-bound) therefore gives, for every admissible globally scale-uncertain source,

```math
\mathrm{risk}_{\mathrm Q}
\ge\frac3{512}T^2
\min\left\{w^2,
\frac1{\max\{cGKT,1\}}\right\},
\qquad
w=\min\left\{1,\frac{a_+}{a_-}-1\right\}.
```

For fixed nonzero prior width and $cGKT\ge\max\{1,w^{-2}\}$ this becomes

```math
\mathrm{risk}_{\mathrm Q}\ge\frac3{512c}\frac{T}{GK}.
```

Let $R^*_{\mathrm C}$ and $R^*_{\mathrm Q}$ denote the optimal minimax average per-use risks in the corresponding allowed classical and quantum classes, under the stated resource and calibration restrictions. The attainable classical upper bound $R^*_{\mathrm C}\le C_cT/G$ and the reference lower bound imply

```math
\frac{R^*_{\mathrm C}}{R^*_{\mathrm Q}}\le C'_{c,a_+/a_-}K.
```

This is a universal $O(K)$ ceiling on the exploitable quantum gain in this model. A classical lower bound alone would not establish this ceiling: its proof also needs the attainable classical upper bound.

The exact bound retains its prior-width branch. If the source speed is supplied with uncertainty much smaller than the scale $1/\sqrt{GKT}$, this supplied knowledge can remove the calibration limitation; one cannot assert the same ceiling with constants uniform in a shrinking prior width.

For $K=1$, comparable setup and use time therefore prevent a gain growing without bound with clock dimension, even for an intrinsically noiseless source. This does not exclude a constant-factor improvement. Longer calibration or a reference with larger explicitly paid activity can change the comparison.

## 5. An attainable quantum regime

For a specified quantum family let $\beta_d$ be an upper bound on its known-current dimensionless time-diffusion coefficient under fixed complete source strength. The finite thermal family used here has

```math
\beta_d\le C_\eta d^{-1+\eta},
\qquad 0\lt \eta\lt 1\text{ fixed}.
```

All source reset delays and reverse events are included in this coefficient. Choose source and reference activities as fixed fractions of $G$ and take mean calibration duration $s=\Theta(KT)$. The finite signed-count calibration-and-estimation theorem has the form

```math
\mathrm{risk}_{\mathrm{Q,construction}}
\le C\frac{T}{G}
\left[\beta_d+\frac1K\right]
+\text{startup, counter, detector, reference-bias and drift terms}.
```

The startup term is controlled in an explicit sufficient thermal regime $gT/d^9\to\infty$, with $g=\Theta(G)$ and fixed exponents. This is a conservative guarantee of a nonempty regime, not a claim that this observation horizon is necessary or practical. Every other displayed error term must be made no larger than the target risk under its declared resource assumption.

The classical lower bound then implies the achievable gain

```math
\frac{R^*_{\mathrm C}}{R^*_{\mathrm Q}}
\ge \frac{c'}{\beta_d+1/K}
=\Omega\!\left(\min\{K,d^{1-\eta}\}\right).
```

Combined with the universal ceiling, this matches the $K$ dependence while $K$ does not exceed the scale of the inherited intrinsic gain. For larger $K$, the construction recovers its full known-current signed-count advantage.

There is no converse here asserting that $\beta_d^{-1}$ limits every quantum source or every estimator using its full record. The upper bound on $\beta_d$ describes this construction. An unrestricted $\Theta(\min\{K,\beta_d^{-1}\})$ claim would require a separate intrinsic quantum lower bound.

## 6. What can be amortized

The calibration accuracy is shared by all intervals. With a reference count $m$, the noiseless-source example has

```math
\mathrm{Cov}(\widehat t_i-t_i,\widehat t_j-t_j)
=\frac{t_it_j}{m-2}.
```

Thus $K$ uses can amortize the resource expense of one calibration when each interval has a fixed individual accuracy target. They do not create $K$ independent calibrations. For the cumulative duration $V=\sum_i t_i$, the shared error is of order $V^2/m$. Preserving diffusion-scale risk $D_QV$ as $V$ grows instead requires reference exposure of order $V/D_Q$.

Unknown durations cannot serve as known-duration calibration samples merely because there are many of them. The parameter transformation $a\mapsto a(1+h)$ and $t_i\mapsto t_i/(1+h)$ preserves every operational interval. Additional known durations, a supplied probabilistic duration standard, or access to another clock would be extra calibration information.

Reuse also requires stability. Unknown speed changes after calibration introduce a common scale error that can dominate the small intrinsic diffusion. The finite drift bounds must be checked over the whole intended reuse age. Stationarity during a long calibration and stability after it are separate assumptions; extending calibration indefinitely does not solve a tracking problem with continuing drift.
