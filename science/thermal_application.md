# A finite thermal clock with paid calibration

[Model](model.md) · [Finite protocol](finite_protocol.md) · [Reference converse](reference_converse.md) · [Classical comparison and reuse](classical_and_reuse.md)

The finite thermal-reset family supplies a source whose calibrated signed-count diffusion decreases with core dimension. This page proves a finite mixing estimate for that source and applies the paid-calibration protocol. The quantum core and thermal reset conversion are inherited; the finite-horizon bound makes their use in the two-stage estimation task explicit.

## 1. Pinned source and physical jumps

Use [Quantum-Clock-Thermal-Reset at revision 46b39e2bc0eb0afc88e2593d5b1cba514bb289a4](https://github.com/GoGoKo699/Quantum-Clock-Thermal-Reset/tree/46b39e2bc0eb0afc88e2593d5b1cba514bb289a4), especially its model, counting-statistics and quasiideal-application pages. Its reconstruction of the core follows Woods et al., *Quantum Clocks are More Accurate Than Classical Ones*, PRX Quantum 3, 010319 (2022), Appendix F. [Quantum-Clock-Restart-Limits at revision 4e275bdc621e7fa250a19c2e29f122499095bdfc](https://github.com/GoGoKo699/Quantum-Clock-Restart-Limits/tree/4e275bdc621e7fa250a19c2e29f122499095bdfc) is an additional calibrated-clock antecedent.

The source Hilbert space is a $`d`$-level core and two auxiliary levels $`m,e`$. Let $`A_k=\lvert m\rangle\langle v_k\rvert`$, $`Q=\sum_k\lvert v_k\rangle\langle v_k\rvert`$, and let $`\psi`$ be the core release state. The source contains all of these physical jumps:

| Physical transition | Jump operator | Signed capture increment |
|---|---|---:|
| Core capture | $`A_k`$ | $`+1`$ |
| Reverse capture | $`\sqrt z A_k^\dagger`$ | $`-1`$ |
| Hot excitation | $`\sqrt{gh}\lvert e\rangle\langle m\rvert`$ | $`0`$ |
| Hot relaxation | $`\sqrt g\lvert m\rangle\langle e\rvert`$ | $`0`$ |
| Release | $`\sqrt g\lvert\psi\rangle\langle e\rvert`$ | $`0`$ |
| Reverse release | $`\sqrt{zg}\lvert e\rangle\langle\psi\rvert`$ | $`0`$ |

The Hamiltonian preserves the core/$`m`$/$`e`$ sectors. Assume $`0<h\leq1`$, $`0<q_{\min}\leq g`$, $`Q\geq q_{\min}I_C`$, and

```math
\sum_\alpha L_\alpha^\dagger L_\alpha
=(Q+zgP_\psi)\oplus
(gh+z\operatorname{Tr}Q)P_m\oplus2gP_e
\leq2gI.
```

All hot backtracking and cold reverse events remain in this bound and in the output law. In particular, release is not an instantaneous free reset. The source output is $`N=N_+-N_-`$, not the number of positive captures alone.

## 2. Inherited asymptotic source performance

For each fixed $`0<\eta<1`$ and all sufficiently large even $`d`$, the pinned source provides

```math
\begin{gathered}
q_{\min}\geq gd^{-3},\qquad Q\leq gI_C,
\qquad \min_c\|H_C-cI_C\|<g/4,\\
j_d=\Theta_\eta(g/d),\qquad
D_{{\rm time},d}:=D_{N,d}/j_d^2
\leq C_\eta d^{-1+\eta}/g.
\end{gathered}
```

There is no factor of two in $`D_{N,d}=\lim_{t\to\infty}\operatorname{Var}N(t)/t`$. Its derivation retains the joint duration/reverse-count law of complete regeneration blocks. At a finite reverse rate it is not recovered by replacing this law with the waiting-time variance of positive captures.

One fixed-bath realization chooses

```math
\theta:=\beta_H/\beta_C\leq\eta/44,
\qquad z_d=d^{-11},\qquad h_d=d^{-22\theta},
\qquad q_d=11\log d/\beta_C.
```

The temperatures are fixed for the chosen $`\eta`$ while $`d`$ grows. The core and thermal bridge use $`d+2`$ source states, $`O(d)`$ engineered channels, bare energy width $`2q_d=O(\log d)`$, and bath entropy per net tick $`22(1-\theta)\log d`$ in the stated tightly coupled effective model. These are resource costs, not constants hidden in the jump-activity bound.

## 3. A completely positive minorization

The following finite estimate supplies the mixing integrals in the [finite protocol](finite_protocol.md#1-generator-output-and-finite-mixing-integrals). It holds for every source of the displayed thermal form, without needing its asymptotic precision law.

Set

```math
\tau=1/g,\qquad
\alpha=\frac{q_{\min}h}{36}e^{-2},
\qquad
\varepsilon=\alpha\tau/2
=\frac{q_{\min}}g\frac{he^{-2}}{72}.
```

**Minorization.** There is a density matrix $`\sigma`$ and a quantum channel $`\Psi`$ such that

```math
e^{\tau\mathcal L}
=\varepsilon\Phi+(1-\varepsilon)\Psi,
\qquad \Phi(X)=\sigma\operatorname{Tr}X.
```

Here is a direct trajectory-instrument proof. Write $`V(t)`$ for the no-physical-jump propagator. Since the complete jump effect is at most $`2gI`$,

```math
\|V(t)x\|^2\geq e^{-2gt}\|x\|^2.
```

Indeed its derivative is minus the expectation of the total jump effect, bounded below by $`-2g\|V(t)x\|^2`$. The propagator preserves the three source sectors. For an initial core component, a capture at time $`r`$ therefore has effect
$`V_C(r)^\dagger QV_C(r)\geq q_{\min}e^{-2gr}I_C`$.

Fix a first-release time $`s\in[\tau/2,\tau]`$ and retain only these disjoint classes of trajectories before that release:

1. From the core: a capture in $`[0,\tau/6]`$, a hot excitation in $`[\tau/6,\tau/3]`$, and no other physical jump before release.
2. From $`m`$: a hot excitation in $`[\tau/6,\tau/3]`$ and no other physical jump before release.
3. From $`e`$: no earlier physical jump.

The release itself has rate $`g`$. Lower-bounding survival on the successive intervals by $`e^{-2g\,\text{duration}}`$ gives the following lower bounds on the selected first-release effect density, on its three initial sectors:

```math
\begin{array}{c|c}
\text{initial sector}&\text{effect density at }s\\ \hline
C&q_{\min}g^2h(\tau/6)^2e^{-2gs}I_C\\
m&g^2h(\tau/6)e^{-2gs}P_m\\
e&ge^{-2gs}P_e.
\end{array}
```

Every entry is at least $`\alpha`$ times its sector projector: use $`s\leq\tau`$, $`q_{\min}\leq g`$ and $`h\leq1`$. Each selected effect is block diagonal, so the combined effect $`E_s`$ obeys $`E_s\geq\alpha I`$ even for initial states with inter-sector coherences.

Each release prepares the same state $`P_\psi`$. Its selected instrument map is consequently $`X\mapsto P_\psi\operatorname{Tr}(E_sX)`$. The difference obtained by replacing $`E_s`$ with $`E_s-\alpha I`$ is completely positive. After release retain the full, trace-preserving source evolution, including all subsequent jumps. It follows that subtracting

```math
\alpha\int_{\tau/2}^{\tau}
e^{(\tau-s)\mathcal L}(P_\psi)\,ds\;\operatorname{Tr}(\cdot)
```

from $`e^{\tau\mathcal L}`$ leaves a completely positive map. The integral has trace $`\alpha\tau/2=\varepsilon`$. Taking

```math
\sigma=\frac2\tau\int_{\tau/2}^{\tau}
e^{(\tau-s)\mathcal L}(P_\psi)\,ds
```

and normalizing the residual map proves the claimed decomposition. This establishes a completely positive minorization, rather than merely a lower bound on survival probabilities.

## 4. Explicit mixing and startup remainder

A replacement channel vanishes on trace-zero Hermitian inputs. Trace-norm contraction of quantum channels therefore gives

```math
\|e^{\tau\mathcal L}(X)\|_1
\leq(1-\varepsilon)\|X\|_1,
\qquad X=X^\dagger,\quad\operatorname{Tr}X=0.
```

This proves uniqueness of the stationary state and convergence from every initial state. For the Hermitian induced trace norm,

```math
r(t)=\|e^{t\mathcal L}-\mathcal P\|_{{\rm H},1\to1}
\leq2(1-\varepsilon)^{\lfloor t/\tau\rfloor}.
```

The factor two bounds $`I-\mathcal P`$ on general Hermitian inputs. Integrating the geometric envelope yields

```math
m_0\leq\frac{2\tau}{\varepsilon},
\qquad
m_1\leq\frac{2\tau^2}{\varepsilon^2}.
```

Substituting $`\Lambda=2g`$ into the finite signed-count theorem gives, for every initial density matrix and every finite $`t\geq0`$,

```math
\boxed{\quad
\mathbb E[(N(t)-j_dt)^2]\leq D_{N,d}t+B_{0,d},
\qquad
B_{0,d}\leq\frac4\varepsilon+\frac{64}{\varepsilon^2}.
\quad}
```

These constants are conservative. They control startup and a calibration-conditioned initial state without imposing stationary preparation or a dimension-independent gap.

## 5. Joint finite calibration and use regime

Now let $`a\in[a_-,a_+]`$ multiply the source's accessible time scale. The prior interval is fixed as dimension grows. The finite protocol uses $`j_-=a_-j_d`$, $`j_+=a_+j_d`$, and one independent reference stopped after $`m`$ events.

For the count-only realization, suppress the bare carrier and use the exact scaled generator $`a\mathcal L_d`$ for the counted instrument. This does not discard output information promised to the decoder: every counted and uncounted jump map preserves the block-diagonal algebra, and the carrier is scalar on each sector. Inter-sector coherences never feed the signed-count probabilities. Thus the count law is identical to that obtained after projecting the initial state onto the three sectors, for which removing the carrier changes no output probabilities. Access to the carrier's phase is not part of this instrument.

All source jump effects scale with $`a`$. Choose $`\kappa`$ and $`g`$ so that

```math
2a_+g+\kappa\leq G.
```

Thus the complete simultaneous source-plus-reference event capacity during calibration is at most $`G`$. Taking $`g`$ and $`\kappa`$ to be fixed comparable fractions of $`G`$ does not increase the peak reference rate with $`d`$.

For the inherited family,

```math
\varepsilon^{-1}=O(d^{3+22\theta}),
\qquad B_{0,d}=O(d^{6+44\theta}),
\qquad B_{{\rm time},d}:=B_{0,d}/j_-^2
=O(d^{8+44\theta}/g^2).
```

The protocol therefore gives, uniformly for arbitrary externally chosen $`t\in[T/2,T]`$,

```math
R_a(t)\leq C_{\eta,a_\pm}\left[
\frac{d^{-1+\eta}}g\left(T+\frac{T^2}s\right)
+\frac{T^2}{\kappa s}
+\frac{d^{8+44\theta}}{g^2}
\left(1+\frac{T^2}{s^2}\right)
\right]+T^2p_{\rm cnt}.
```

Here $`s=m/\kappa`$ is paid expected calibration time and $`p_{\rm cnt}`$ is the specified finite-register failure bound. Reference rate-certification and drift errors are added separately; the displayed bound uses exact rate certification and source parameters that remain constant throughout calibration and use. The initial source state can be arbitrary.

Because $`44\theta\leq\eta`$, a sufficient joint asymptotic regime making the startup term negligible relative to the target intrinsic timing risk is

```math
\frac{gT}{d^9}\longrightarrow\infty,
\qquad s\geq cT\quad(c>0\text{ fixed}).
```

Indeed the ratio of the startup term to $`d^{-1+\eta}T/g`$ is at most a constant times $`d^{9+44\theta-\eta}/(gT)`$. This explicit polynomial condition is sufficient, not necessary. It does not identify a practical crossover or a sharp onset exponent.

For $`K`$ separate uses choose $`m=\lceil\kappa cKT\rceil`$ with fixed $`c>0`$ and $`\kappa\asymp g\asymp G`$, so $`s=m/\kappa\asymp KT`$ in the stated large-horizon regime. With finite counters accurate enough that
$`p_{\rm cnt}\leq C(d^{-1+\eta}+K^{-1})/(GT)`$, this gives

```math
R_a(t)\leq C\frac TG
\left(d^{-1+\eta}+\frac1K\right)
```

after the stated onset. The comparison with all bounded-rate classical networks, the universal $`O(K)`$ gain ceiling and its scope are in [Classical comparison and reuse](classical_and_reuse.md). There is no assertion that this source attains the best possible quantum risk among all devices and decoders.

If the reference's actual rate is certified only to a fractional error $`\xi`$, the [finite certification bound](finite_protocol.md#7-reference-certification-and-detector-assumptions) adds a contribution of order $`\xi^2T^2`$. Retaining the displayed target therefore requires

```math
\xi^2\lesssim\frac{d^{-1+\eta}+K^{-1}}{GT}.
```

For the full inherited diffusion scale, the sufficient requirement is $`\xi^2\lesssim d^{-1+\eta}/(GT)`$. This certified-accuracy promise and its expense are supplied reference resources; no finite-cost physical procedure for preparing that frequency standard is derived here. Increasing the reference event count reduces stochastic jitter, not an unknown fixed certification bias.

Finite registers suffice in this regime. For any fixed positive Chernoff parameter satisfying the Gamma moment condition, the [counter bounds](finite_protocol.md#6-finite-record-memory) permit
$`H_c=O(m+\log p_c^{-1})`$ and $`H_u=O(gT+\log p_u^{-1})`$. Their bit costs are logarithmic in these capacities; retaining all outputs requires the additional static output memory.

## 6. Detector requirement and the physical scope

The thermal source has $`r_++r_-=\Theta(g/d)`$ and $`j=\Theta(g/d)`$, where $`r_\pm`$ denote directional capture intensities. Independent detection efficiency $`e_{\rm det}`$ therefore adds

```math
\frac{1-e_{\rm det}}{e_{\rm det}}
\frac{r_++r_-}{j^2}
=\Theta\!\left(\frac{1-e_{\rm det}}{e_{\rm det}}\frac d g\right)
```

to the observed timing diffusion. Fixed nonzero loss can erase the advantage of this signed-count construction. To retain the displayed $`d^{-1+\eta}/g`$ scale one needs, in particular, $`1-e_{\rm det}=O(d^{-2+\eta})`$ in the high-efficiency regime. Ideal sign-resolving detection is the base theorem's declared assumption; it is not supplied by the thermal reset compiler.

More generally, retaining the per-use target $`(T/G)(d^{-1+\eta}+K^{-1})`$ under this independent-loss model requires

```math
\frac{1-e_{\rm det}}{e_{\rm det}}
\lesssim\frac{d^{-1+\eta}+K^{-1}}d.
```

The declared memory, reference-certification and detector thresholds are distinct resources. The finite-register term must obey $`T^2p_{\rm cnt}\lesssim(T/G)(d^{-1+\eta}+K^{-1})`$; Chernoff capacities above ensure this with finite memory. These conditions do not price the physical amplification or fabrication required to meet the detector threshold.

The resource statements have different meanings:

| Resource | Account |
|---|---|
| Complete source jump effect | At most $`2agI`$, including every modeled reset and reverse event |
| Simultaneous calibration activity | At most $`2a_+g+\kappa\leq G`$ |
| Active core coherent strength | At most $`ag/4`$ after centering |
| Bare carrier energy width | $`O(\log d)`$ for the fixed-bath source, separately charged |
| Source size and channels | $`d+2`$ source states and $`O(d)`$ engineered coupling channels |
| Reference and records | $`m`$ reference events, expected duration $`s`$, countdown and finite register bits |
| Detector and physical memory | Ideal instrument/prepared registers in the effective model; certification accuracy, loss, erasure and microscopic engineering are separate resources |

In particular, bounded active core strength does not assert a dimension-independent norm for the full bare carrier Hamiltonian. The carrier is invisible to signed capture statistics, but an additional measurement exposing its known unscaled phase would supply another calibration reference and invalidate the common-accessible-speed premise.

The exact source theorem concerns the specified finite-dimensional thermal GKLS generator. Its thermodynamic interpretation uses a clustered weak-coupling limit at each fixed dimension, followed by long-time counting and then the dimension limit. The finite bounds above are exact for that effective generator; they do not establish uniform infinite-time counting accuracy at fixed microscopic coupling, a finite-bath detector, physical reference-rate certification or a complete laboratory clock. Scaling the effective generator is a specified parameter family; its realization as a microscopic family requires its own bath/coupling calibration account.
