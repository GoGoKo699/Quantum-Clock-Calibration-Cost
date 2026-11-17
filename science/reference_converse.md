# A finite reference limits every calibration method

[Classical comparison and reuse](classical_and_reuse.md) · [Overview](../README.md)

An accurate source can reveal its own progress without knowing how fast that progress runs in physical units. This page bounds the information that a finite classical reference can supply about that missing scale. The result allows arbitrary decoders and correlated source output. Its restriction is operational: every accessible source time scale must share the same unknown multiplier.

## 1. The calibration experiment

Let $a\in[a_-,a_+]$, where $0<a_-<a_+<\infty$. The source has **operational time** $u=at$. Its accessible experiment, conditional on operational-time histories, is independent of $a$. A concrete example has

```math
\mathcal L_a=a\mathcal L_0,
\qquad H_a=aH_0,
\qquad L_{\alpha,a}=\sqrt a\,L_{\alpha,0}.
```

The initial source state and all supplied static memory are independent of $a$. State preparation, measurements, and feedback may depend on observed events through fixed parameter-independent rules. They cannot introduce an independent known physical frequency or a known-duration delay. The independent reference described below is the only supplied physical-time standard.

During calibration, grant an independent finite-state continuous-time Markov reference. Its physical transition rates $q_{xy}$ and initial distribution are specified and independent of $a$. Include every physical reference transition, reset, and observable marked self-event. Write $q(x)$ for its total event intensity, and suppose

```math
q(x)\le\kappa.
```

A finite collection of references is covered by treating its joint state and the sum of all its event intensities as one reference. The complete peak-activity resource is the aggregate bound, rather than a separate allowance for each channel.

Calibration ends at a stopping rule determined by available event records. There is no supplied physical timestamp or known deterministic physical deadline. Denote its physical duration by $S$, its reference-event count by $M$, and require finite expected duration throughout the parameter range. For the event-budget theorem assume

```math
\sup_{a\in[a_-,a_+]}\mathbb E_a M\le B.
```

It is sufficient instead to impose $\sup_a\mathbb E_a S\le s$, since $\mathbb E_a M\le\kappa\mathbb E_a S$. Event counters, detectors, and controls with their own nonzero timing dynamics must be included in the reference resource if they supply an independent time scale.

After calibration the reference is unavailable. The clock estimates externally chosen unknown durations $\boldsymbol t=(t_1,\ldots,t_K)$ from untimestamped source output. Start and end signals delimit the tasks but reveal no numerical times. The durations do not depend on the source noise. Static calibration memory and the clock state may be retained, and the decoder may act jointly on all allowed outputs.

The scale condition is a substantive assumption. A known unscaled carrier Hamiltonian, detector dead time, controlled phase, or retained known-rate clock can supply another reference. Such access changes the experiment. The thermal signed-capture record satisfies the scale condition even when an unobserved carrier has no effect on that record; this does not authorize arbitrary additional measurements exposing that carrier.

## 2. An operational-time oracle

For a lower bound, improve the source by granting exact operational timestamps and unrestricted parameter-independent processing of them. Conditional on an operational history and reference events, the original source records and any final quantum state are produced by an $a$-independent classical or quantum channel. Thus the enlarged experiment is at least as informative as the specified source.

This is a statistical comparison, not a claim of efficient classical simulation of a quantum clock. In particular, an $a$-dependent state produced during calibration is covered: conditional on the enlarged operational history, its preparation channel is parameter independent. A state carrying an additional independent physical time scale is not covered.

In operational coordinates the reference jump intensities are

```math
\lambda_a(u,x\to y)=\frac{q_{xy}}a.
```

The source dynamics and the normalized reference jump-label probabilities are parameter free. The stopping rule is the same functional of the enlarged paths at every $a$; it does not acquire an $a$-dependent physical deadline.

## 3. Stopped-record relative entropy

**Lemma.** Let $\mathsf P_a$ be the enlarged stopped calibration experiment. For any $a_0,a_1$ in the allowed range,

```math
D_{\mathrm{KL}}(\mathsf P_{a_0}\Vert\mathsf P_{a_1})
\le \mathbb E_{a_0}M
\left[\log\frac{a_1}{a_0}-1+\frac{a_0}{a_1}\right].
```

For the fully revealed classical reference path with a common parameter-independent stopping rule, the reference likelihood gives equality. The inequality permits coarsening and additional parameter-independent source channels. In particular,

```math
D_{\mathrm{KL}}(\mathsf P_{a_0}\Vert\mathsf P_{a_1})
\le \kappa\mathbb E_{a_0}S
\left[\log\frac{a_1}{a_0}-1+\frac{a_0}{a_1}\right].
```

**Proof.** Let $U=aS$ be the operational stopping time. On the enlarged path space, the only parameter-dependent intensities are those of the reference. Its stopped log likelihood ratio is

```math
\log\frac{d\mathsf P_{a_0}}{d\mathsf P_{a_1}}
=M\log\frac{a_1}{a_0}
-\left(\frac1{a_0}-\frac1{a_1}\right)
\int_0^U q(X_u)\,du.
```

The compensator identity and $u=a_0t$ under $a_0$ give

```math
\mathbb E_{a_0}M
=\mathbb E_{a_0}\int_0^U\frac{q(X_u)}{a_0}\,du
=\mathbb E_{a_0}\int_0^S q(X_t)\,dt.
```

Taking expectations yields the asserted expression. One may first stop at a bounded operational horizon and bounded event count. Bounded physical intensity and finite expected $S$ make the stopped compensators and likelihood terms integrable, allowing removal of these cutoffs. Relative entropy cannot increase when inaccessible reference events are discarded or source outputs are generated through parameter-independent channels. This proves the lemma.

For $a_1=a_0(1+h)$, $0<h\le1$,

```math
\log(1+h)-\frac{h}{1+h}\le\frac{h^2}{2}.
```

Unlike an asymptotic Cramér–Rao bound, the lemma applies before taking a long-time limit and does not require an unbiased estimator.

## 4. Unknown-time minimax bound

Fix $T>0$ and let every unknown duration belong to $[T/2,T]$. Define average per-use squared loss by

```math
\ell(\widehat{\boldsymbol t},\boldsymbol t)
=\frac1K\sum_{i=1}^K(\widehat t_i-t_i)^2.
```

Set

```math
w=\min\left\{1,\frac{a_+}{a_-}-1\right\}>0,
\qquad \overline B=\max\{B,1\}.
```

**Theorem.** For every admissible source, calibration protocol, and joint decoder,

```math
\sup_{a\in[a_-,a_+]}
\sup_{\boldsymbol t\in[T/2,T]^K}
\mathbb E_{a,\boldsymbol t}
\ell(\widehat{\boldsymbol t},\boldsymbol t)
\ge
\frac3{512}T^2
\min\left\{w^2,\frac1{\overline B}\right\}.
```

The same lower bound holds after taking the infimum over all admissible calibration methods and decoders, including biased ones. Its constant is deliberately conservative.

**Proof.** Choose

```math
h=\min\left\{w,\frac1{2\sqrt{\overline B}}\right\},
\qquad a_0=a_-,\quad a_1=a_-(1+h),
```

and compare the two duration vectors

```math
\boldsymbol t^{(0)}=(T,\ldots,T),
\qquad
\boldsymbol t^{(1)}=\left(\frac{T}{1+h},\ldots,
\frac{T}{1+h}\right).
```

Both lie in the allowed box. At every use their operational durations coincide:
$a_0t_i^{(0)}=a_1t_i^{(1)}$. Conditional on the enlarged stopped calibration history, the entire subsequent source experiment is therefore the same parameter-independent channel at the two points. This includes retained source memory and joint measurements. The unknown-use output cannot increase their relative entropy beyond that of calibration.

The lemma gives relative entropy at most $Bh^2/2\le1/8$, so total variation is at most $1/4$. The two duration vectors have normalized Euclidean separation

```math
\Delta=\frac{Th}{1+h}\ge\frac{Th}{2}.
```

Turn any estimator into the nearest-vector test. A testing error implies squared loss at least $\Delta^2/4$. Hence its average risk over the two points is at least

```math
\frac{\Delta^2}{8}(1-\mathrm{TV})
\ge\frac{3T^2h^2}{128}
\ge\frac3{512}T^2
\min\left\{w^2,\frac1{\overline B}\right\}.
```

The worst-point risk is at least this average, completing the proof.

The theorem is a minimax claim over an uncertainty set. A pointwise positive lower bound for all biased estimators would be false: a decoder that always outputs one fixed time has zero risk at that time. The prior-width branch also matters. When the speed is already known extraordinarily accurately, that supplied prior knowledge can be more useful than further reference events.

## 5. Sharpness in the noiseless-source limit

Take a Poisson reference of known physical rate $\kappa$ and stop at its $m$-th event. Then

```math
S\sim\operatorname{Gamma}(m,\kappa),
\quad U_{\mathrm{cal}}=aS,
\quad U_{\mathrm{use}}=at.
```

The oracle knows $U_{\mathrm{cal}}$ and $U_{\mathrm{use}}$, not $S$. For $m>2$ the estimator

```math
\widehat t_{\mathrm{unb}}
=\frac{(m-1)U_{\mathrm{use}}}{\kappa U_{\mathrm{cal}}}
```

is unbiased and obeys

```math
\operatorname{Var}\widehat t_{\mathrm{unb}}
=\frac{t^2}{m-2}.
```

The biased estimator with $m-2$ in place of $m-1$ has exact mean squared error $t^2/(m-1)$. These identities follow from the first two inverse-Gamma moments. Thus the order $t^2/B$ lower bound is sharp even when the source has no intrinsic timing noise.

If the same calibration serves several intervals, the oracle returns $\widehat t_i=F t_i$ with the same random multiplier $F=(m-1)/(\kappa S)$. In particular,

```math
\operatorname{Cov}(\widehat t_i-t_i,\widehat t_j-t_j)
=\frac{t_it_j}{m-2}.
```

Reuse spreads calibration expense; it does not divide this shared statistical error by the number of uses. For the cumulative duration $V=\sum_i t_i$, this example has variance $V^2/(m-2)$.

## 6. Scope of the obstruction

The result remains true after finite-counter coarsening, missed records, or loss of source access: those changes cannot increase information. Its constructive counterpart must still account for those errors explicitly.

The theorem assumes the reference's specified physical rates. Unknown fixed rate bias is a separate scale ambiguity and cannot be reduced by collecting more of the same reference events. A quantum reference, a deterministic phase oscillator, a known delayed trigger, or an independent Hamiltonian standard is not an autonomous finite-state classical Markov reference under this theorem. The bound assigns no cost to such an alternative until its own dynamics, accuracy, and resource metric are specified.

Poisson-reference calibration and finite sampling have direct antecedents in [Nurgalieva, Silva and Renner](https://arxiv.org/html/2406.12973v1). The claim established here concerns every allowed calibration method and the timing risk after the reference is removed. The [reuse analysis](classical_and_reuse.md) explains its consequence under matched complete-device activity bounds.
