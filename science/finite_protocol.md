# A finite calibration-and-estimation protocol

[Model](model.md) · [Reference converse](reference_converse.md) · [Thermal application](thermal_application.md) · [Classical comparison and reuse](classical_and_reuse.md)

The protocol uses a finite reference record to learn the clock's actual signed current. It then removes the reference and estimates elapsed time from an untimestamped signed count. The bounds below retain the dependence between reverse events, internal reset delays and the initial state. A positive lower current bound and clipping make the estimator well defined even after a misleading calibration record.

Poisson-reference reconstruction of signed, nonreset clock statistics is inherited from Nurgalieva, Silva and Renner, especially their section VI and Appendix D. The [related-work comparison](../references/RELATED_WORK.md) separates that method from the universal calibration converse and its elapsed-time/reuse consequences here.

## 1. Generator, output and finite mixing integrals

Let a finite-dimensional clock have a time-independent GKLS generator

```math
\mathcal L(\rho)=-i[H,\rho]
+\sum_\alpha\left(L_\alpha\rho L_\alpha^\dagger
-\tfrac12\{L_\alpha^\dagger L_\alpha,\rho\}\right),
\qquad
\sum_\alpha L_\alpha^\dagger L_\alpha\leq\Lambda I.
```

Each physical jump has an output increment $`s_\alpha\in\{-1,0,1\}`$. Define its recycling map $`\mathcal J_\alpha(\rho)=L_\alpha\rho L_\alpha^\dagger`$ and

```math
\mathcal J_1=\sum_\alpha s_\alpha\mathcal J_\alpha,
\qquad
\mathcal J_2=\sum_\alpha s_\alpha^2\mathcal J_\alpha.
```

The signed count $`N(u)`$ starts at zero. Unobserved jumps with increment zero remain in $`\mathcal L`$ and in the complete activity bound $`\Lambda`$.

Assume the source mixes to one stationary density matrix $`\rho_{\rm ss}`$. Set

```math
\mathcal P(X)=\rho_{\rm ss}\operatorname{Tr}X,
\qquad
\mathcal R(u)=e^{u\mathcal L}-\mathcal P,
\qquad
r(u)=\|\mathcal R(u)\|_{{\rm H},1\to1},
```

where the norm is induced trace norm restricted to Hermitian inputs. Assume the finite integrals

```math
m_0=\int_0^\infty r(u)\,du<\infty,
\qquad
m_1=\int_0^\infty u\,r(u)\,du<\infty.
```

At each fixed dimension, exponential mixing suffices. These constants need not be uniform in dimension. The [thermal application](thermal_application.md#3-a-completely-positive-minorization) proves explicit bounds rather than presuming a uniform spectral gap.

For positive $`X`$, the triangle inequality and the complete jump bound give

```math
\|\mathcal J_1(X)\|_1
\leq\sum_\alpha |s_\alpha|\operatorname{Tr}\mathcal J_\alpha(X)
\leq\Lambda\operatorname{Tr}X.
```

Applying this to the positive and negative parts of a Hermitian input proves
$`\|\mathcal J_1\|_{{\rm H},1\to1}\leq\Lambda`$. The same argument gives the bound for $`\mathcal J_2`$.

Write

```math
j=\operatorname{Tr}\mathcal J_1(\rho_{\rm ss})>0,
\qquad
k=\operatorname{Tr}\mathcal J_2(\rho_{\rm ss}),
\qquad
C(v)=\operatorname{Tr}\!\left[
\mathcal J_1\mathcal R(v)\mathcal J_1(\rho_{\rm ss})\right].
```

The actual signed-count diffusion, with no factor of two in its definition, is

```math
D_N:=\lim_{u\to\infty}\frac{\operatorname{Var}N(u)}u
=k+2\int_0^\infty C(v)\,dv.
```

In particular, $`|C(v)|\leq\Lambda^2r(v)`$. This definition includes the correlations of the signed record; a variance of positive-capture waiting times is a different quantity when reverse captures occur.

## 2. A uniform bound for every initial state

**Finite signed-count bound.** For every initial density matrix $`\rho`$ and every $`u\geq0`$,

```math
\boxed{\quad
\mathbb E_\rho[(N(u)-ju)^2]\leq D_Nu+B_0,
\qquad
B_0=\Lambda m_0+4\Lambda^2m_1+2\Lambda^2m_0^2.
\quad}
```

This is a centered second-moment bound, not an assertion that the finite-time count is unbiased.

To prove it, differentiate the finite-dimensional tilted generator
$`\mathcal L(\chi)=\mathcal L+\sum_\alpha(e^{s_\alpha\chi}-1)\mathcal J_\alpha`$. Duhamel's formula gives the exact moment identities

```math
\begin{aligned}
\mathbb E_\rho N(u)
&=\int_0^u\operatorname{Tr}\mathcal J_1e^{s\mathcal L}(\rho)\,ds,\\
\mathbb E_\rho N(u)^2
&=\int_0^u\operatorname{Tr}\mathcal J_2e^{s\mathcal L}(\rho)\,ds\\
&\quad+2\int_{\substack{s,v\geq0\\s+v\leq u}}
\operatorname{Tr}\mathcal J_1e^{v\mathcal L}
\mathcal J_1e^{s\mathcal L}(\rho)\,dv\,ds.
\end{aligned}
```

Under stationary initialization these imply

```math
\operatorname{Var}_{\rm ss}N(u)
=ku+2\int_0^u(u-v)C(v)\,dv.
```

Subtracting $`D_Nu`$ leaves
$`-2\int_0^u vC(v)\,dv-2u\int_u^\infty C(v)\,dv`$, whose absolute value is at most $`2\Lambda^2m_1`$.

For a general initial state put $`f(s)=\operatorname{Tr}\mathcal J_1\mathcal R(s)(\rho)`$. Then

```math
\mathbb E_\rho N(u)=ju+b(u),
\qquad b(u)=\int_0^u f(s)\,ds,
\qquad |b(u)|\leq\Lambda m_0.
```

Expand the second-moment identities using $`e^{v\mathcal L}=\mathcal P+\mathcal R(v)`$. The difference
$`\mathbb E_\rho[(N(u)-ju)^2]-\operatorname{Var}_{\rm ss}N(u)`$ is exactly

```math
\begin{aligned}
&\int_0^u\operatorname{Tr}\mathcal J_2\mathcal R(s)(\rho)\,ds
-2j\int_0^u s f(s)\,ds\\
&\quad+2\int_{\substack{s,v\geq0\\s+v\leq u}}
\operatorname{Tr}\mathcal J_1\mathcal R(v)
\mathcal J_1\mathcal R(s)(\rho)\,dv\,ds.
\end{aligned}
```

Its three terms have absolute values at most $`\Lambda m_0`$, $`2\Lambda^2m_1`$ and $`2\Lambda^2m_0^2`$. Adding the stationary remainder proves the bound. Only Hermitian inputs occur in these norm estimates.

## 3. An uncertain common speed

Let the family be $`\mathcal L_a=a\mathcal L_0`$ for
$`a\in[a_-,a_+]`$, where $`0<a_-<a_+<\infty`$ are known constants. All physical jump rates, reverse transitions and source resets share this scale. Then

```math
j_a=aj_0,\qquad D_{N,a}=aD_{N,0},\qquad
\Lambda_a=a\Lambda_0,\qquad
m_{0,a}=m_{0,0}/a,\qquad m_{1,a}=m_{1,0}/a^2.
```

The constant $`B_0`$ in the boxed bound is therefore exactly scale invariant. Define known uniform bounds

```math
j_-=a_-j_0>0,\qquad j_+=a_+j_0,
\qquad \overline D=a_+D_{N,0},\qquad
\overline\Lambda=a_+\Lambda_0.
```

The [model](model.md) specifies which outputs obey this common-speed condition. An accessible unscaled phase standard is an additional reference.

## 4. Calibration without a known physical deadline

Use an independent reference whose successive marked events have independent exponential waiting times of known actual rate $`\kappa`$. Stop at its $`m`$th event. The actual calibration duration is not revealed:

```math
S\sim\operatorname{Gamma}(m,\kappa),
\qquad s:=\mathbb ES=m/\kappa,
\qquad \operatorname{Var}S=s^2/m.
```

The reference runs only during calibration. The stochastic fractional uncertainty of its duration is $`1/\sqrt m`$, and it supplies exactly $`m`$ counted events. A finite countdown has $`m+1`$ logical values and can stop the reference autonomously. This is an effective finite-state reference model with explicit event, time and memory costs, not a detector or bath implementation theorem.

Let $`C=N(S)`$ be the source's signed calibration count. Define

```math
\widetilde j=C/s,
\qquad
\widehat j=\Pi_{[j_-,j_+]}(\widetilde j),
```

where $`\Pi`$ denotes Euclidean projection onto the stated interval. Since the true current lies in that interval, projection cannot increase its squared estimation error. Decompose
$`C-js=(C-jS)+j(S-s)`$. Independence of reference and source, the uniform finite-time bound, and $`(x+y)^2\leq2x^2+2y^2`$ yield

```math
\boxed{\quad
\mathbb E_a(\widehat j-j_a)^2
\leq\mathcal E_{\rm cal}
:=\frac{2\overline D}s+\frac{2B_0}{s^2}
+\frac{2j_+^2}{m}.
\quad}
```

No stationary initialization or independence between positive and negative source events is required. Negative, zero or anomalously large calibration counts are permitted. Clipping always returns a positive denominator. For example, a direct consequence is
$`\Pr(|\widehat j-j_a|\geq\delta j_-)\leq\mathcal E_{\rm cal}/(\delta^2j_-^2)`$.

## 5. Estimating an unknown interval

For a deterministic, externally chosen unknown duration $`t\in[0,T_{\max}]`$, read its signed count increment $`N_{\rm use}`$ and return

```math
\widehat t=\Pi_{[0,T_{\max}]}
\left(\frac{N_{\rm use}}{\widehat j}\right).
```

Projection reduces error because the true time lies in the interval. Pathwise,

```math
(\widehat t-t)^2
\leq\frac2{j_-^2}
\left[(N_{\rm use}-j_at)^2+t^2(\widehat j-j_a)^2\right].
```

Conditional on any calibration record, the source begins the unknown interval in some density matrix. The future generator is unchanged, so the uniform initial-state bound applies. Thus calibration and use may be correlated:

```math
\boxed{\quad
R_a(t):=\mathbb E_a(\widehat t-t)^2
\leq\frac2{j_-^2}
\left[\overline D t+B_0+t^2\mathcal E_{\rm cal}\right].
\quad}
```

Writing $`B_{\rm time}=B_0/j_-^2`$ and using the fixed prior ratio, this has the scaling

```math
R_a(t)\leq C\left[
D_{\rm time}\left(t+\frac{t^2}s\right)
+\frac{t^2}{\kappa s}
+B_{\rm time}\left(1+\frac{t^2}{s^2}\right)
\right],
\qquad D_{\rm time}=D_{N,a}/j_a^2,
```

with a numerical constant depending only on $`a_+/a_-`$. The $`t^2/(\kappa s)`$ term is reference uncertainty, rather than source diffusion. A single calibration can be reused for separately reported unknown intervals; the common rate error remains shared between them.

## 6. Finite record memory

Let $`A(v)`$ count every physical source jump. Its predictable intensity is at most $`\overline\Lambda`$, regardless of the conditional source state. Exponential supermartingale bounds give

```math
\mathbb E e^{\chi A(v)}
\leq\exp\{\overline\Lambda v(e^\chi-1)\},
\qquad \chi>0.
```

At the independent Gamma calibration stop,

```math
\mathbb E e^{\chi A(S)}
\leq\left[
1-\frac{\overline\Lambda}{\kappa}(e^\chi-1)
\right]^{-m},
\qquad
\overline\Lambda(e^\chi-1)<\kappa.
```

Consequently a calibration count capacity $`H_c`$ and use capacity $`H_u`$ have explicit failure bounds

```math
\begin{aligned}
p_c&\leq e^{-\chi_c H_c}
\left[1-\frac{\overline\Lambda}{\kappa}
(e^{\chi_c}-1)\right]^{-m},\\
p_u&\leq\exp\{-\chi_u H_u+
\overline\Lambda T_{\max}(e^{\chi_u}-1)\}.
\end{aligned}
```

A signed cyclic register with $`2H+1`$ values returns the true signed increment whenever the total number of physical events in the relevant interval is at most $`H`$. The source jump
$`L_\alpha\otimes U^{s_\alpha}`$, with $`U`$ a cyclic shift, has effect $`L_\alpha^\dagger L_\alpha\otimes I`$. Thus recording does not conceal additional jump intensity or change the reduced source dynamics in this ideal register model. A wrapped result can be wrong, but after final time clipping its squared loss is at most $`T_{\max}^2`$. Relative to the unlimited-record protocol,

```math
R_a^{\rm finite}(t)
\leq\frac2{j_-^2}
\left[\overline D t+B_0+t^2\mathcal E_{\rm cal}\right]
+T_{\max}^2(p_c+p_u).
```

This argument does not require an overflow flag. It couples the finite and unlimited records and charges the event on which they can disagree. For a guarantee covering all $`K`$ uses simultaneously, replace $`p_c+p_u`$ by $`p_c+\sum_i p_{u,i}`$.

The calibration register needs $`\lceil\log_2(2H_c+1)\rceil`$ bits. A cumulative cyclic use register and its stored starting value need two registers of $`\lceil\log_2(2H_u+1)\rceil`$ bits. Centered modular differences recover each interval increment on its good event even if the cumulative register wrapped before that interval. Previous outputs can be streamed; retaining all $`K`$ outputs requires their additional static memory. The finite reference countdown and routing flags are included separately. Initial pure register states are supplied and charged; no in-run erasure is needed for the stated protocol. Any physical terminal erasure or extra reset mechanism carries its own preparation, dissipation and activity costs. Fixed event-triggered register routing introduces no calibrated time signal.

## 7. Reference certification and detector assumptions

Known actual $`\kappa`$ is an explicit rate-certification assumption. If the declared nominal rate is $`\kappa_0`$ and the actual rate is $`\kappa_0(1+e)`$ with $`|e|\leq\xi<1`$, use $`s_0=m/\kappa_0`$ in the estimator. A three-term squared-sum bound gives the replacement

```math
\mathbb E(\widehat j-j_a)^2
\leq\frac{3\overline D}{(1-\xi)s_0}
+\frac{3B_0}{s_0^2}
+\frac{3j_+^2}{m(1-\xi)^2}
+\frac{3j_+^2\xi^2}{(1-\xi)^2}.
```

The last term is systematic; collecting more events does not remove it. In the counter tail use the smallest possible reference rate $`\kappa_0(1-\xi)`$. A physical rate-certification procedure is not derived here; its guaranteed accuracy and expense are declared input resources available to both comparisons.

The base protocol assumes ideal passive detection of source signs and reference events. If each source capture is independently recorded with the same known efficiency $`e_{\rm det}>0`$, and signs are correct, then

```math
j_{\rm obs}=e_{\rm det}j,
\qquad
D_{N,\rm obs}=e_{\rm det}^2D_N
+e_{\rm det}(1-e_{\rm det})(r_++r_-),
```

where $`r_+`$ and $`r_-`$ denote the stationary positive and negative capture intensities. Equivalently,

```math
D_{{\rm time},\rm obs}
=\frac{D_N}{j^2}
+\frac{1-e_{\rm det}}{e_{\rm det}}
\frac{r_++r_-}{j^2}.
```

These identities follow by conditioning on the full signed capture record and include its correlations. Apply the finite protocol to the observed instrument, with its actual mixing integrals and current interval. Sign errors, deadtime, correlated missed events and a detector carrying an accessible known timing scale require a different instrument/resource model. Detector amplification, microscopic readout engineering and physical memory erasure are not inferred from the source's effective GKLS description.
