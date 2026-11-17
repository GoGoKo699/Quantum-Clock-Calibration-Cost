# Relation to previous work

[Scientific overview](../science/README.md) · [References](REFERENCES.md)

The task here is to calibrate an unknown common dynamical scale using a finite reference record, remove the reference, and estimate an externally specified unknown elapsed time. The contribution is the necessary reference-exposure and stable-reuse law for that task, together with a finite signed-current construction. Neither using a Poisson reference nor propagating a learned-rate error is introduced here.

## Operational calibration is an inherited ingredient

[Nurgalieva, Silva and Renner](REFERENCES.md#nsr24) reconstruct clock signals from their tick order relative to a Poisson reference. Section V gives finite-sample bounds separating target fluctuations from finite reference frequency. Section VI and Appendix D extend the method to nonreset clocks and reversible registers: stop after a prescribed number of reference ticks and observe the target's signed count. Their Eq. (32) recovers the mean current; Eqs. (104)–(113) use the resulting Gamma-distributed observation duration. Section IV also states that an unknown reference rate fixes only relative time units.

The Poisson-stop calibration and its additive source/reference noise terms are therefore credited to that work. The finite bound here additionally controls arbitrary startup states and a clipped reciprocal estimator. The main distinction is a converse over allowed calibration protocols, followed by an elapsed-time comparison after reference removal.

[Wadhia et al.](REFERENCES.md#w25) explicitly uses time tags during calibration and an untimestamped state sequence during clock operation. Its signed-current estimator divides the net count by a calibrated mean frequency. Appendix B.2, Eq. (33), relates finite frequency uncertainty to calibration duration; Appendix C treats rate estimation, detector effects and drift. Its measured operating regime admits a classical master equation. Thus calibration-only access, learned frequency uncertainty and drift awareness are prior ingredients. Its detector thermodynamics also motivates keeping a modeled source-resource advantage separate from a complete laboratory cost claim.

## The classical alternative permits the full record

[Prech et al.](REFERENCES.md#p25) studies time estimation from an entire untimestamped finite-state Markov trajectory. Section II identifies sufficient state-visit statistics and an asymptotically efficient estimator weighted by inverse escape rates. Its variance is controlled by the mean residual time; Eq. (42) gives a finite-time information bound. [Macieszczak](REFERENCES.md#m24) independently develops the tight asymptotic kinetic bound and its semi-Markov extension.

The comparison here grants every allowed classical network its complete event record and even exact rate calibration. Uniformization and a two-point testing argument give a finite minimax lower bound for arbitrary, possibly biased decoders. This is an application of established Markov information limitations, rather than a new classical uncertainty principle. A constant-escape-rate clock supplies an attainable classical benchmark. The reference-exposure converse is a separate bound on the absolute scale missing after calibration.

## What is inherited from quantum clock constructions

[Woods et al.](REFERENCES.md#w22) supplies the quasiideal clock and its near-quadratic dimension-dependent tick accuracy. The input [Thermal-Reset account](REFERENCES.md#thermal-reset) retains a finite thermal bridge, reverse events, reset delay and actual signed-current correlations under a summed source-jump bound. Its elapsed-time diffusion advantage is used as an input theorem. [Meier et al.](REFERENCES.md#meier25) is a prior source for the thermal bridge and the precision–entropy mechanism credited by that input.

The [Restart-Limits account](REFERENCES.md#restart-limits) provides a complementary calibrated clock comparison under hidden complete restarts. Neither input is modified or counted as a new clock construction here.

The present work adds learning the actual accessible speed, charging the temporary reference, controlling finite startup and counter errors, and determining how much stable reuse is needed to retain the inherited timing gain. The effective thermal generator and its inherited microscopic limit order remain explicit assumptions; the calibration theorem does not supply a new reservoir or detector implementation.

## The surviving operational statement

For a common unknown accessible speed, the reference's expected charged event count bounds the distinguishability of nearby absolute scales. This remains true after giving the quantum source noiseless operational-time readout. Pairing a changed scale with an inversely changed elapsed time then gives a timing-risk floor proportional to elapsed-time squared divided by reference exposure.

With a fixed complete activity budget and calibration expense at most a constant times the useful duration of K separate uses, that floor limits the gain over the attainable classical timing scale to order K. The finite signed-current protocol reaches that order until its inherited intrinsic gain is recovered. This is a necessary cost/reuse statement, not merely an error estimate for one calibration algorithm.

The claim concerns fixed per-use risk. Shared scale error remains correlated across uses: estimating a growing cumulative elapsed time requires growing reference exposure. Post-calibration drift further limits the usable lifetime of a calibration. Quantum references, independently known timing auxiliaries, or uncertainty outside the common-scale model require another comparison.

## Recent imperfect-reference characterization

[Domínguez, Chubb and Woods, arXiv:2609.31837](REFERENCES.md#dcw26a), describes precision characterization using multiple imperfect copies of a clock. Their [arXiv:2609.31832](REFERENCES.md#dcw26b) describes single-clock characterization with a splitter and uncertain delayed trigger.

Only their indexed arXiv abstracts and metadata were available for comparison. Their detailed assumptions, guarantees and possible overlap with the disconnected-reference elapsed-time problem have not been verified. The statements in this repository are therefore not accompanied by a claim of priority or demonstrated independence from those two preprints.

The distinction supported by the accessible material is one of task formulation: this work proves a finite minimax condition for absolute elapsed-time estimation after a paid calibration aid is removed; the available abstracts describe clock-precision characterization. A theorem-level non-subsumption claim requires their full texts.

