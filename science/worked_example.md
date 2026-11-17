# What calibration buys

[Model](model.md) · [Classical comparison and reuse](classical_and_reuse.md)

Consider a source whose known-rate timing coefficient would be one hundredth of the best classical scale at the same complete event budget. This is an illustrative coefficient, not a numerically demonstrated thermal device.

Write the classical timing scale as $`T/G`$ and the source's intrinsic coefficient ratio as $`\beta=0.01`$. With reference peak rate a fixed fraction of $`G`$, the finite protocol's leading terms have the form

```math
\frac{R_{\rm Q}}{T/G}
\lesssim \beta+\frac{T}{s}+\beta\frac{T}{s},
```

with fixed constants suppressed and startup, counter, detector and drift allowances handled separately.

If calibration has mean duration $`s\asymp T`$, its stochastic reference error is still of the classical timing order. The source's much more regular ticks do not make the reference interval exact. This is a limitation on every calibration method in the declared classical-reference model, not only on the chosen count estimator.

To expose the full factor-one-hundred intrinsic coefficient, use about one hundred times as much calibration exposure. If the clock then measures one hundred arbitrary intervals separately, each of duration of order $`T`$, that setup cost is comparable to the total useful duration. This is the meaning of amortization.

| Stable future uses | Calibration with $`s\asymp KT`$ | Leading achievable normalized risk |
|---:|---|---|
| $`K=1`$ | One-use setup expense | $`O(1)`$ |
| $`K=10`$ | Ten-use setup expense | $`O(0.01+0.1)`$ |
| $`K=100`$ | One hundred-use setup expense | $`O(0.01+0.01)`$ |
| $`K\gg100`$ | Larger shared calibration | $`O(0.01)`$ |

The table shows scaling, not guaranteed exact improvement factors. Constants and finite startup can matter considerably.

## Shared uncertainty is not independent tick noise

If the same learned current is slightly high, every reported duration tends to be low. Adding the duration estimates adds those errors coherently. For a total elapsed duration $`U=\sum_i t_i`$, calibration contributes order $`U^2/m`$, rather than order $`\sum_i t_i^2/m`$.

Thus one calibration can spread its expense across many separately reported durations at a fixed per-use target. It cannot maintain unlimited cumulative timing precision at a fixed reference-event budget.

## Stability sets the useful lifetime

Suppose the scale can change by an unknown fraction $`\rho`$ before a future interval. Even a perfect initial calibration leaves timing risk of order $`\rho^2T^2`$. To expose an intrinsic variance $`D_{\rm Q}T`$, require $`\rho^2\lesssim D_{\rm Q}/T`$.

Better intrinsic regularity therefore demands both more reference exposure and a tighter stability promise. A very precise device with a drifting unknown rate is not automatically a good stopwatch.

## Finite thermal onset remains conservative

The explicit thermal family supplies a nonempty joint finite regime, but the sufficient bound $`gT/d^9\to\infty`$ is loose. The small matrix checks verify counting and calibration identities; they do not demonstrate a factor-one-hundred practical device or certify this illustrative table as a crossover study.

