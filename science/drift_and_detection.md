# Drift, reference accuracy and detection

[Finite calibration protocol](finite_protocol.md) · [Reference converse](reference_converse.md) · [Thermal application](thermal_application.md)

A calibrated clock has two distinct uncertainties: fluctuations in its event record and uncertainty in the conversion from that record to physical time. Longer calibration reduces sampling noise. It does not remove an unknown fixed error in the reference's rate or an unknown later change in the source's speed. This page gives exact indistinguishability statements for those errors and states the detector and memory assumptions under which the signed-count guarantees apply.

## 1. Uncertain reference rate

Let the actual source generator be $`a\mathcal L_0`$. Suppose the calibration reference is Poisson with actual rate $`b\kappa_0`$, while the supplied rate certification is only $`b\in[1-\xi,1+\xi]`$, with $`0\leq\xi<1`$. No other absolute-time standard is accessible.

In source operational time $`u=at`$, the reference rate is $`b\kappa_0/a`$. Thus the two parameter choices

```math
(a_+,b_+)=\bigl(a_0(1+\delta),1+\delta\bigr),
\qquad
(a_-,b_-)=\bigl(a_0(1-\delta),1-\delta\bigr)
```

produce the same calibration experiment when $`0<\delta\leq\xi`$ and both source speeds lie in the source prior. This holds for event-adapted stopping rules: in operational coordinates, the reference intensity and all parameter-independent decision rules coincide.

Pair those choices with the unknown use durations

```math
t_+=\frac{T}{1+\delta},
\qquad
t_-=\frac{T}{1-\delta}.
```

Both uses have operational duration $`a_0T`$. Their untimestamped output laws coincide, including any allowed calibration-conditioned source memory. The two durations must fit the declared time window; the central value $`T`$ can be chosen in that window's interior.

For every estimator, equality of the two data laws implies

```math
\max_{\sigma\in\{+,-\}}
\mathbb E_\sigma[(\widehat t-t_\sigma)^2]
\geq
\frac{(t_--t_+)^2}{4}
=
\frac{\delta^2T^2}{(1-\delta^2)^2}.
```

Under the common data law, the average of the two squared losses equals the squared deviation from their midpoint plus $`(t_--t_+)^2/4`$. This exact minimax statement permits biased estimators. It survives arbitrarily many reference events and even noiseless source operational-time readout.

The result concerns a shared unknown reference scale. Independently resampled zero-mean reference jitter is different: finite event jitter and fixed rate-certification error must be charged separately.

### Finite upper bound with imperfect certification

For calibration stopped after $`m`$ reference events, put $`s_0=m/\kappa_0`$. Its actual duration satisfies

```math
S\sim\operatorname{Gamma}(m,b\kappa_0),
\qquad
\mathbb ES=\frac{s_0}{b},
\qquad
\operatorname{Var}S=\frac{s_0^2}{b^2m}.
```

Let the source have constant parameters during calibration, actual current $`j`$, diffusion $`D_N`$, and the finite envelope

```math
\mathbb E_\rho[(N(v)-jv)^2]\leq D_Nv+B_0
```

uniformly over initial states. For $`\widetilde j=N(S)/s_0`$, decompose the error into $`[N(S)-jS]/s_0+j(S/s_0-1)`$. The squared-sum inequality yields

```math
\mathbb E[(\widetilde j-j)^2]
\leq
\frac{2D_N}{b s_0}
+\frac{2B_0}{s_0^2}
+\frac{2j^2}{b^2m}
+2j^2\left(\frac1b-1\right)^2.
```

Projection into a known positive source-current interval cannot increase this loss. The last term is at most $`2j^2\xi^2/(1-\xi)^2`$. The [clipped inversion bound](finite_protocol.md) therefore adds time risk of order $`\xi^2t^2`$, with constants depending on the fixed prior ratios and $`1/(1-\xi)`$.

The systematic floor has a matching constructive order. Setting $`\xi=0`$ is an explicit ideal rate-certification assumption, not a claim to prepare an exactly rate-calibrated laboratory reference at a proved finite energy or fabrication cost.

## 2. Post-calibration speed changes

Assume the source speed was constant, equal to $`a_{\rm c}`$, during calibration. After calibration let

```math
\mathcal L(v)=a(v)\mathcal L_0.
```

For a use beginning at physical age $`A`$ and lasting $`t`$, define

```math
U_{A,t}=\int_0^t a(A+v)\,dv,
\qquad
\overline\delta_{A,t}
=
\frac{U_{A,t}}{a_{\rm c}t}-1.
```

For deterministic drift paths, or drift independent of source jump noise, the output is the nominal source output at operational duration $`U_{A,t}`$. If $`|a(A+v)/a_{\rm c}-1|\leq\rho`$ throughout use, then $`|\overline\delta_{A,t}|\leq\rho`$.

A fixed-time moment envelope cannot automatically be applied at an operational stopping time selected through the source's own noisy record. Output-adaptive drift or feedback requires a separate stopped-time analysis and is not assumed here.

### Exact mismatch obstruction

Even grant perfect knowledge of $`a_{\rm c}`$. If the use speed may be $`a_{\rm c}(1+\rho)`$ or $`a_{\rm c}(1-\rho)`$, the corresponding durations $`T/(1+\rho)`$ and $`T/(1-\rho)`$ have identical operational time. When both speed and time points are allowed,

```math
\inf_{\widehat t}\max_{\sigma\in\{+,-\}}
\mathbb E_\sigma[(\widehat t-t_\sigma)^2]
\geq
\frac{\rho^2T^2}{(1-\rho^2)^2}.
```

This two-point model permits a speed change between calibration and use. It does not assert that an instantaneous change satisfies a continuous drift-rate constraint. The continuous model below has its own exact obstruction.

### Correlation-safe upper bound

Let $`j_{\rm c}=a_{\rm c}j_0`$, and let $`\widehat j\geq j_{\min}>0`$ be the stored calibration estimate. Clip $`N_{\rm use}/\widehat j`$ into a known time interval containing $`t`$. Decompose

```math
N_{\rm use}-\widehat j\,t
=
\bigl(N_{\rm use}-j_0U_{A,t}\bigr)
+j_{\rm c}t\,\overline\delta_{A,t}
+(j_{\rm c}-\widehat j)t.
```

The inequality $`(x+y+z)^2\leq3(x^2+y^2+z^2)`$ and the uniform finite moment envelope give, for a deterministic drift path,

```math
\mathbb E[(\widehat t-t)^2]
\leq
\frac{3}{j_{\min}^2}
\left[
D_{N,0}U_{A,t}+B_0
+j_{\rm c}^2t^2\overline\delta_{A,t}^{\,2}
+t^2\mathbb E[(\widehat j-j_{\rm c})^2]
\right].
```

The source initial state may depend on calibration, because the first term is bounded uniformly over that state. Calibration and use need not be independent. For independent random drift one may condition on the drift path and average, with the corresponding conditional calibration-error term if needed.

Keeping the mismatch term within an intrinsic timing-risk scale $`D_Qt`$ requires

```math
\rho^2t^2=O(D_Qt),
\qquad
\rho=O\!\left(\sqrt{D_Q/t}\right).
```

The uncertainty here is in the conversion scale; it is not independent tick noise.

## 3. Continuous drift and calibration lifetime

Suppose calibration ends with $`a(0)=a_{\rm c}`$ and later drift satisfies

```math
\left|\frac{d}{dv}\log a(v)\right|\leq\ell.
```

A use at age $`A`$ of duration at most $`T`$ obeys

```math
|\overline\delta_{A,t}|
\leq e^{\ell(A+T)}-1.
```

A sufficient condition to keep drift risk within order $`D_QT`$ is

```math
e^{\ell(A+T)}-1
=O\!\left(\sqrt{D_Q/T}\right).
```

For small drift this reduces to $`\ell(A+T)=O(\sqrt{D_Q/T})`$. For $`K`$ sequential uses occupying time of order $`T`$ each, with $`D_Q=\beta/G`$, a sufficient full-gain condition is

```math
K
\lesssim
\frac{\sqrt{\beta}}
{\ell\sqrt G\,T^{3/2}}.
```

This is a sufficient lifetime bound for the declared protocol and drift envelope, not an assertion that every path attains its worst-case envelope at every age. It must coexist with the [amortization requirement](classical_and_reuse.md): $`K`$ must be of order $`\beta^{-1}`$ to spread calibration expense while retaining the full inherited signed-count gain.

### Drift inside the measured interval is already an obstruction

There is an exact lower bound even after perfect initial calibration with continuous drift. Compare

```math
a_{\rm A}(v)=a_0,
\qquad
a_{\rm B}(v)=a_0(1+\ell v).
```

Both start at $`a_0`$ and satisfy the logarithmic drift bound, since $`d\log a_{\rm B}/dv=\ell/(1+\ell v)\leq\ell`$. Compare time $`t_0`$ in model A with the positive $`t_1`$ solving

```math
t_1+\frac{\ell t_1^2}{2}=t_0.
```

Their operational durations are identical. For $`0<\ell t_0\leq1`$, one has $`t_1\geq2t_0/3`$, and thus

```math
t_0-t_1=\frac{\ell t_1^2}{2}
\geq\frac{2\ell t_0^2}{9}.
```

The identical-data two-point argument gives

```math
\inf_{\widehat t}
\max\{\operatorname{MSE}_{\rm A},\operatorname{MSE}_{\rm B}\}
\geq\frac{\ell^2t_0^4}{81}.
```

The two durations and the ramp's speed range must lie in the allowed task family. Calibration alone cannot remove unknown within-use drift.

### Stability during calibration is a separate assumption

The calibration theorem assumes constant speed during calibration. If that speed also drifts while calibration is collected, the source count describes an accumulated operational duration and hence a past average, rather than the endpoint speed.

For a realized calibration duration $`S`$, let $`\overline a_S=S^{-1}\int_0^S a(v)\,dv`$. A logarithmic drift bound gives the pathwise estimate

```math
\left|\frac{\overline a_S}{a(S)}-1\right|
\leq e^{\ell S}-1.
```

For $`\ell S\ll1`$, this permits bias of order $`\ell S`$. Poisson-stop calibration has an unbounded Gamma duration, so its mean $`s`$ cannot simply replace the realized $`S`$ in a deterministic bound; its tails must also be controlled. A general optimal tracking or calibration-window theorem is not established here.

## 4. Imperfect signed-event detection

Let $`N=N_+-N_-`$ be the true signed capture count and $`A=N_++N_-`$ its total capture count. Their stationary rates are $`j=j_+-j_->0`$ and $`k=j_++j_-`$. All correlations in the true record remain present.

Consider this explicit response channel:

- Each true capture is independently detected with probability $`e\in(0,1]`$.
- Conditional on detection, its sign is independently reversed with probability $`p\in[0,1/2)`$.
- Response variables are independent of the full source trajectory, calibration, and one another.
- The detector adds no false events, deadtime, recovery delay, or timestamps.

A true sign $`s\in\{+1,-1\}`$ contributes $`sZ`$, where $`Z=+1,-1,0`$ with probabilities $`e(1-p),ep,1-e`$. Put $`c=e(1-2p)>0`$. Conditional on the true record,

```math
\mathbb E[N_{\rm obs}\mid\text{record}]=cN,
\qquad
\operatorname{Var}(N_{\rm obs}\mid\text{record})
=(e-c^2)A.
```

Total expectation and variance give exact finite-time identities,

```math
\mathbb EN_{\rm obs}=c\,\mathbb EN,
\qquad
\operatorname{Var}N_{\rm obs}
=c^2\operatorname{Var}N+(e-c^2)\mathbb EA.
```

Hence

```math
j_{\rm obs}=cj,
\qquad
D_{N,\rm obs}=c^2D_N+(e-c^2)k,
```

and the signed-current estimator's timing diffusion is

```math
D_{\rm time,obs}
=
\frac{D_N}{j^2}
+\left[\frac{1}{e(1-2p)^2}-1\right]\frac{k}{j^2}.
```

For perfect sign labels,

```math
D_{\rm time,obs}
=
D_{\rm time}+\frac{1-e}{e}\frac{k}{j^2}.
```

No independent-source-tick or independent-positive/negative-count approximation is used. Independent marking is the detector assumption. Detector response parameters must have declared accuracy or be learned with additional charged resources; the source-rate calibration theorem does not automatically provide them.

At finite times the same calibration proof can be applied to the observed marked jump maps: $`\mathcal J_{1,\rm obs}=c\mathcal J_1`$ and $`\mathcal J_{2,\rm obs}=e\mathcal J_2`$, while the physical source generator and its complete activity bound remain unchanged. Missed captures remain physical source events even when they give no observed record increment.

For the thermal family, $`j=\Theta(g/d)`$ and $`k=\Theta(g/d)`$, so $`k/j^2=\Theta(d/g)`$. Keeping the added detector noise within order $`d^{-1+\eta}/g`$ requires

```math
\frac{1}{e(1-2p)^2}-1=O(d^{-2+\eta}).
```

For small errors, this means $`1-e+p=O(d^{-2+\eta})`$ up to fixed constants. A fixed nonzero loss or sign-error probability destroys this family's dimension-improving signed-count diffusion law. This calculation is not a converse for every decoder of a more informative detector record.

A detector with a known recovery time, driven local oscillator, or periodic polling can itself provide an independent absolute-time scale. Accessible during the unknown interval, that scale changes the model of the reference converse.

## 5. Complete-device accounting and finite-session memory

“Complete-device” means the explicitly modeled source, reference, and record interface. A timing-active detector, controller, or memory is not omitted from that account.

| Resource | Charged account |
|---|---|
| Source events | $`\sum_\alpha L_\alpha^\dagger L_\alpha\leq\Lambda I`$, including hidden events, thermal recycling, reverse capture/release and all modeled reset or fault channels |
| Reference | Nominal model, certified rate-error interval, actual event count/exposure, complete peak activity at most $`\kappa`$, and finite state space |
| Simultaneous calibration | Independent source-plus-reference capacity at most $`\Lambda+\kappa`$; both fit within the common budget $`G`$ |
| Coherent dynamics | All source and retained ancillary Hamiltonian strengths; any independent known frequency is another declared reference |
| Detection | Efficiency, sign fidelity, false-event/deadtime assumptions, and timing-active physical detector dynamics |
| Records | Finite integer counters, static calibration data, offsets, overflow/alias error, initialized bits and output precision |
| Preparation/reset | Initial source/reference/register resources, every in-run physical reset, and terminal erasure or fresh-memory schedule |
| Thermal resources | Actual bath ratios, energy width, coupling channels and modeled entropy/heat under the effective-model scope |

A counter update can be attached to its source event. For a unitary cyclic shift $`U_\alpha`$,

```math
(L_\alpha\otimes U_\alpha)^\dagger
(L_\alpha\otimes U_\alpha)
=
L_\alpha^\dagger L_\alpha\otimes I.
```

The ideal passive record therefore adds memory dimension without adding a separate jump intensity. This is not a proof that laboratory detector amplification or memory updates have zero energy cost.

One may use a finite cumulative use register with externally marked snapshots or offsets and size it for the entire session, or allocate fresh initialized bits to successive uses. Both avoid an uncharged instantaneous record reset between unknown intervals. The bit count and overflow budget concern the whole finite session, not merely one interval.

A reference stopped at its $`m`$-th event can be a finite $`m+1`$-state countdown chain, of rate $`\kappa`$ until it reaches an absorbing state. This produces the Gamma-stop law without a deterministic timer; it is not retained as an active known-rate clock during use.

The stored calibration information can be the integer source count and the known count $`m`$. No infinitely precise real-valued frequency register is required. Ratio decoding can occur after the end signal without using computation as an elapsed-time standard. Rounding the final answer to a grid of spacing $`\Delta_t`$ gives

```math
\mathbb E[(\widehat t_{\rm rounded}-t)^2]
\leq
2\,\mathbb E[(\widehat t-t)^2]+\frac{\Delta_t^2}{2}.
```

A finite implementation must allocate arithmetic/output precision so this fits its risk target.

The clockwork is cyclic through its modeled thermal reset. An entire finite-memory measurement apparatus is cyclic only when record resetting or erasure is also supplied and paid. Terminal erasure or fresh memory is a separate resource, matched between quantum and classical devices. The timing theorem does not claim a complete laboratory thermodynamic optimum.

