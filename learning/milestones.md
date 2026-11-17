# Thirty milestones for calibration-paid timekeeping

[Learning route](README.md) · [Selected source bridge](anchor_bridge.md) · [Scientific account](../science/README.md)

The map follows one question: how does a finite calibration turn an autonomous device's output into a useful estimate of physical elapsed time?

**M01–M12 are background/preliminaries.** They build from individual events and their fluctuations to the complete calibration-and-use experiment. **M13–M30 are narrative/innovation.** They assemble the information obstruction, the matched classical comparison, a finite quantum protocol, and its reuse and stability conditions. This 12/18 allocation reflects the project's connection between open-system counting and statistical calibration.

Each milestone is a reader-independent understanding target. Dependencies identify earlier ideas needed for that step; the canonical science pages contain the full proofs. Landi et al.'s 2024 tutorial is the single educational anchor, through the [source bridge](anchor_bridge.md). Primary research citations remain attribution and proof inputs.

## Background and preliminaries

### M01 — An elapsed interval and an output record

**Central question:** What does the device actually reveal when an unknown interval ends?

**Understanding target:** Distinguish physical duration from a sequence of observed events. Start and end signals delimit a task without revealing numerical timestamps. A counter reading is evidence about duration, but needs a model relating events to time.

**Dependencies and story role:** None. This sets the operational question before introducing a clock equation.

**Conceptual connection:** A stopwatch is an inference device: output, supplied information and the requested estimate are separate objects.

**Sources:** [Model section 3](../science/model.md#3-use-after-removal-of-the-reference); [worked interpretation](../science/worked_example.md).

### M02 — Autonomous evolution

**Central question:** What makes the source autonomous in the model?

**Understanding target:** Read a time-independent generator as a rule that evolves the source from its present state. Its Hamiltonian and dissipative jumps are parts of that rule. Autonomy excludes a hidden timed schedule that already supplies the duration being measured.

**Dependencies and story role:** M01. Introduces the physical source behind the record.

**Conceptual connection:** Open-system dynamics connects the source state to the statistics of accessible events; autonomous operation alone does not imply known speed.

**Sources:** [Model section 1](../science/model.md#1-one-unknown-accessible-speed); [finite protocol section 1](../science/finite_protocol.md#1-generator-output-and-finite-mixing-integrals); [anchor II.A, via the bridge](anchor_bridge.md#1-a-source-to-project-route).

### M03 — Physical jumps and signed marks

**Central question:** Why are counted events different from all physical events?

**Understanding target:** Assign each physical jump a mark of plus one, minus one or zero. The signed record subtracts reverse captures from forward captures. Zero-mark jumps still change the state, consume activity and can delay future captures.

**Dependencies and story role:** M02. Makes the observed record and the charged dynamics concrete.

**Conceptual connection:** Measurement choice determines a current, while complete-device accounting retains the processes the decoder does not observe.

**Sources:** [Finite protocol section 1](../science/finite_protocol.md#1-generator-output-and-finite-mixing-integrals); [thermal jump table](../science/thermal_application.md#1-pinned-source-and-physical-jumps); [anchor II.C–D, via the bridge](anchor_bridge.md#1-a-source-to-project-route).

### M04 — Stationary mean current

**Central question:** What does a positive mean current tell us about time?

**Understanding target:** Understand $`j`$ as the long-time mean signed count per unit duration. A stationary state gives a constant average current, even though individual events remain random. A positive current gives a direction for the count-to-time conversion; finite startup can still bias a short record.

**Dependencies and story role:** M02–M03. Connects local jumps to a sustained source output.

**Conceptual connection:** Average flow is a property of both the generator and its stationary state, rather than the rate of one selected jump channel.

**Sources:** [Finite protocol sections 1–2](../science/finite_protocol.md); [model section 1](../science/model.md#1-one-unknown-accessible-speed); [anchor II.A and the notation bridge](anchor_bridge.md#2-translate-the-notation-before-using-a-formula).

### M05 — Noise retains correlations

**Central question:** Why does the signed-count variance require more than event frequencies?

**Understanding target:** Read $`D_N=\lim_{t\to\infty}\mathrm{Var}N(t)/t`$ as a variance growth rate. A jump can change the probability of later jumps, so time correlations contribute. Positive- and negative-count fluctuations cannot generally be added as independent noises.

**Dependencies and story role:** M03–M04. Adds the fluctuation information needed to judge a clock.

**Conceptual connection:** The tutorial's output-current correlations connect individual measurement records to full counting statistics.

**Sources:** [Finite protocol section 1](../science/finite_protocol.md#1-generator-output-and-finite-mixing-integrals); [thermal signed record](../science/thermal_application.md#1-pinned-source-and-physical-jumps); [anchor III.A/C and the signed-record bridge](anchor_bridge.md#3-a-signed-record-contains-more-than-positive-ticks).

### M06 — Tick regularity and elapsed-time risk

**Central question:** How does count noise become a timing error?

**Understanding target:** If the actual mean current is known, $`N(t)/j`$ estimates duration, with long-time variance coefficient $`D_{\rm time}=D_N/j^2`$. A source that ticks less often must compensate with sufficient regularity to improve this coefficient. Tick precision alone does not settle useful elapsed-time accuracy.

**Dependencies and story role:** M04–M05. Puts the physical output into the task's units.

**Conceptual connection:** A calibration factor transforms both the signal and its noise; useful performance must include the actual tick rate.

**Sources:** [Model section 1](../science/model.md#1-one-unknown-accessible-speed); [count-to-time bridge](anchor_bridge.md#4-turning-a-count-into-time-requires-a-scale); [worked interpretation](../science/worked_example.md).

### M07 — One unknown speed

**Central question:** What ambiguity remains if every accessible source rate has the same unknown multiplier?

**Understanding target:** For $`\mathcal L_a=a\mathcal L_0`$, the source's operational duration is $`u=at`$. A faster source observed for a proportionally shorter physical interval has the same output law. This is uncertainty in one common speed, not independent uncertainty in every parameter.

**Dependencies and story role:** M02 and M06. Identifies exactly what calibration must learn.

**Conceptual connection:** An identifiable output progression can still lack an absolute conversion to physical time.

**Sources:** [Model section 1](../science/model.md#1-one-unknown-accessible-speed); [reference converse section 1](../science/reference_converse.md#1-the-calibration-experiment).

### M08 — A finite classical reference

**Central question:** What resource does the temporary reference contribute?

**Understanding target:** A classical continuous-time Markov reference waits randomly between events. Bound its aggregate event intensity by $`\kappa`$, including hidden transitions and resets. More states or more labeled channels do not create extra rate allowances.

**Dependencies and story role:** M02–M03 and M07. Introduces a separately charged physical-time standard.

**Conceptual connection:** The reference has its own dynamics, finite accuracy, memory and initialization; it is not a free list of exact timestamps.

**Sources:** [Model section 2](../science/model.md#2-calibration-without-free-timestamps); [reference converse section 1](../science/reference_converse.md#1-the-calibration-experiment).

### M09 — Stopping after reference events

**Central question:** What is known when calibration ends at the reference's m-th event?

**Understanding target:** For a Poisson reference, the event count is fixed while the physical calibration duration is random: $`S\sim\mathrm{Gamma}(m,\kappa)`$. Its mean is $`m/\kappa`$ and its fractional duration standard deviation is $`1/\sqrt m`$. The actual realized duration is not supplied to the decoder.

**Dependencies and story role:** M08. Turns finite reference access into a concrete calibration experiment.

**Conceptual connection:** Event-based termination avoids inserting a free exact physical deadline.

**Sources:** [Finite protocol section 4](../science/finite_protocol.md#4-calibration-without-a-known-physical-deadline); [reference converse section 5](../science/reference_converse.md#5-sharpness-in-the-noiseless-source-limit).

### M10 — Sampling uncertainty and scale bias

**Central question:** Which reference errors can more events reduce?

**Understanding target:** Separate stochastic variation of a finite reference record from a fixed uncertainty in its actual mean rate. Increasing the number of reference events reduces sampling uncertainty. It does not reveal an unknown systematic multiplier shared by the entire reference record.

**Dependencies and story role:** M07–M09. Prevents the reference's certification assumption from disappearing into its sample count.

**Conceptual connection:** Precision of repeated observations and accuracy of their physical unit are different resources.

**Sources:** [Model section 2](../science/model.md#2-calibration-without-free-timestamps); [reference accuracy](../science/drift_and_detection.md#1-uncertain-reference-rate).

### M11 — Risk over an uncertainty set

**Central question:** Why is a minimax claim needed for an impossibility bound?

**Understanding target:** Squared timing risk averages the squared estimation error over the device's random record. A decoder that always returns one fixed duration is exact at that particular duration, so a positive lower bound for every biased decoder cannot hold pointwise. Minimax risk takes the worst case over a declared speed and time window.

**Dependencies and story role:** M01, M06 and M07. Establishes the meaning of the later lower bounds.

**Conceptual connection:** Statistical distinguishability limits a uniform estimation task, rather than forbidding an estimator from being lucky at one parameter point.

**Sources:** [Reference converse section 4](../science/reference_converse.md#4-unknown-time-minimax-bound); [classical comparison section 2](../science/classical_and_reuse.md#2-a-finite-bound-for-arbitrary-biased-decoders).

### M12 — The complete calibration-and-use task

**Central question:** Which information and costs must the comparison hold fixed?

**Understanding target:** Combine a common-speed-uncertain source, a temporary classical reference, finite records and externally chosen unknown intervals. Remove the active reference during use. Count all modeled source/reference activity and declare coherent strength, thermal resources, detection, certification and memory preparation or erasure separately.

**Dependencies and story role:** M01–M11. Integrates the background into the exact research task.

**Conceptual connection:** A useful quantum comparison matches the complete modeled resource vector and equivalent calibration access, rather than selected visible ticks.

**Sources:** [Model sections 3–5](../science/model.md); [resource account](../science/drift_and_detection.md#5-complete-device-accounting-and-finite-session-memory).

## Narrative and innovation

### M13 — A stronger source oracle

**Central question:** Why can the lower-bound proof grant perfect operational-time readout?

**Understanding target:** Conditional on operational histories, the allowed source dynamics and readout channel are independent of the unknown speed. Exact operational information can therefore generate the original source observations, including an allowed final quantum state. An obstruction for that more informative experiment also applies to the source.

**Dependencies and story role:** M07, M11–M12. Begins the converse with a controlled improvement of the experiment.

**Conceptual connection:** Statistical information ordering replaces a device-specific accuracy calculation; it does not assert efficient classical simulation of quantum dynamics.

**Sources:** [Reference converse section 2](../science/reference_converse.md#2-an-operational-time-oracle).

### M14 — Information in a stopped reference record

**Central question:** What part of the enlarged calibration experiment distinguishes nearby speeds?

**Understanding target:** In operational coordinates the reference rates become $`q_{xy}/a`$. Its likelihood includes both observed events and time with no event. At an integrable event-adapted stop, relative entropy between nearby speed hypotheses is bounded by expected charged reference events times a known scale function.

**Dependencies and story role:** M08–M09 and M13. Converts finite reference exposure into a quantitative information bound.

**Conceptual connection:** The compensator accounts for waiting and absence of events; those are not omitted from the reference's information.

**Sources:** [Stopped-record lemma](../science/reference_converse.md#3-stopped-record-relative-entropy).

### M15 — A calibration floor for every decoder

**Central question:** How does limited scale information force a timing-risk floor?

**Understanding target:** Pair a changed speed with inversely changed unknown durations, keeping every operational interval unchanged. The use output then cannot distinguish the paired hypotheses. A two-point testing argument turns the calibration relative-entropy bound into risk of order $`T^2/B_{\rm ref}`$ when reference exposure dominates the fixed-prior-width branch.

**Dependencies and story role:** M07, M11 and M14. Assembles the universal calibration obstruction.

**Conceptual connection:** The exact bound retains the uncertainty width; a shrinking speed prior is additional supplied accuracy and can change the conclusion.

**Sources:** [Finite minimax theorem](../science/reference_converse.md#4-unknown-time-minimax-bound).

### M16 — The full classical record

**Central question:** Could a complicated classical network or a better untimestamped decoder evade the benchmark?

**Understanding target:** Uniformization generates all bounded-rate CTMC trajectories from rate-$`G`$ Poisson opportunities and parameter-independent transition choices. Deleting unobserved opportunities yields even the full state/mark record. Hidden states, resets and retained classical memory do not create a faster opportunity process.

**Dependencies and story role:** M08, M11–M12. Builds the strongest relevant classical alternative independently of a chosen clock architecture.

**Conceptual connection:** Granting complete observations and exact calibration makes the classical comparator stronger; a quantum construction that beats it does not depend on a weak classical decoder.

**Sources:** [Uniformization and complete device](../science/classical_and_reuse.md#1-complete-device-classical-benchmark).

### M17 — Classical risk for K arbitrary intervals

**Central question:** Why does the classical per-use risk remain of order $`T/G`$ under joint decoding?

**Understanding target:** Independent Poisson opportunity counts give an informative oracle for the K intervals. A product prior over separate unknown durations keeps each coordinate uncertain even after all other counts are revealed. This gives a finite lower bound for arbitrary biased joint decoders, while a constant-escape event clock attains the same order.

**Dependencies and story role:** M11 and M16. Completes both sides of the classical benchmark.

**Conceptual connection:** A lower bound alone does not prove the later gain ceiling; that ceiling also uses an attainable classical upper bound.

**Sources:** [Classical finite bound and matching protocol](../science/classical_and_reuse.md#2-a-finite-bound-for-arbitrary-biased-decoders); [equivalent calibration access](../science/classical_and_reuse.md#3-equivalent-calibration-access-for-the-classical-device).

### M18 — Exact signed-count moments

**Central question:** How can finite count moments be obtained without independent-tick assumptions?

**Understanding target:** A counting field weights each physical jump by its signed mark. Differentiating the tilted generator gives exact first and second moment identities. The second moment contains the physical event contribution and a two-time propagation term, retaining reset and reverse-event correlations.

**Dependencies and story role:** M02–M05. Starts the constructive proof from finite dynamics rather than an assumed long-time approximation.

**Conceptual connection:** The anchor's full counting statistics becomes a finite analytical tool for the actual observable.

**Sources:** [Finite protocol sections 1–2](../science/finite_protocol.md); [anchor IV–V, via the bridge](anchor_bridge.md#1-a-source-to-project-route); [finite diagnostics](../verification/README.md).

### M19 — Startup and conditional states

**Central question:** How can a long-time diffusion coefficient support a finite observation?

**Understanding target:** Mixing integrals bound the stationary correlation tail and the nonstationary corrections. The resulting envelope $`\mathbb E_\rho[(N(t)-jt)^2]\le D_Nt+B_0`$ holds for every initial state. It allows a finite startup bias and need not assume that calibration prepares a stationary source.

**Dependencies and story role:** M04–M05 and M18. Supplies the finite guarantee needed after a random calibration stop.

**Conceptual connection:** Uniformity over the initial density matrix protects later risk bounds when the source state depends on the calibration record.

**Sources:** [Uniform signed-count bound](../science/finite_protocol.md#2-a-uniform-bound-for-every-initial-state).

### M20 — Thermal recycling remains inside the clock

**Central question:** Which physical processes does the inherited quantum timing law include?

**Understanding target:** Follow capture, reverse capture, hot excitation/relaxation and release through the core and two auxiliary states. Their finite delays and every physical jump remain in the generator and complete activity bound. The useful source law concerns the actual signed current, not positive captures alone.

**Dependencies and story role:** M03, M06 and M19. Identifies the concrete quantum source to which the finite calibration protocol will apply.

**Conceptual connection:** A source can recycle autonomously while its external finite record apparatus still needs declared preparation or erasure resources.

**Sources:** [Thermal model and inherited performance](../science/thermal_application.md#1-pinned-source-and-physical-jumps); [source attribution](../references/RELATED_WORK.md).

### M21 — An explicit finite thermal regime

**Central question:** How is finite mixing justified without a dimension-independent gap?

**Understanding target:** Selected release trajectories have a common positive effect on every initial sector and prepare the same release state. Their common component gives a completely positive replacement-channel minorization, hence explicit mixing and startup bounds. The conservative sufficient joint regime $`gT/d^9\to\infty`$ controls the remainder for the inherited family.

**Dependencies and story role:** M19–M20. Connects a physical recycling path to a finite-horizon mathematical guarantee.

**Conceptual connection:** A nonempty proved regime and a practical onset estimate are different conclusions.

**Sources:** [CP minorization](../science/thermal_application.md#3-a-completely-positive-minorization); [mixing and joint regime](../science/thermal_application.md#4-explicit-mixing-and-startup-remainder).

### M22 — Robust calibration of the signed current

**Central question:** What should the decoder do with a zero, negative or misleading calibration count?

**Understanding target:** Divide the signed calibration count by the reference's mean duration, then project the learned current into its known positive interval. The mean squared calibration error has separate source, reference and startup terms. Projection prevents a misleading record from producing a zero or negative reciprocal denominator.

**Dependencies and story role:** M09–M10 and M19. Turns the finite reference experiment into a well-defined rate estimate.

**Conceptual connection:** Robust inversion needs prior bounds as well as small typical fluctuations; rare bad records cannot simply be discarded.

**Sources:** [Calibration protocol](../science/finite_protocol.md#4-calibration-without-a-known-physical-deadline).

### M23 — Correlation-safe use of calibration

**Central question:** Why can the source continue directly from calibration into the unknown interval?

**Understanding target:** Estimate time by the use count divided by the clipped learned current, with a final projection into the known time window. A pathwise squared-error inequality separates count error from rate error. The uniform initial-state envelope then controls the count term even when calibration and use are correlated.

**Dependencies and story role:** M19 and M22. Completes the finite calibration-and-estimation protocol.

**Conceptual connection:** Conditional source states are retained explicitly; independent calibration/use samples are unnecessary.

**Sources:** [Finite use-risk bound](../science/finite_protocol.md#5-estimating-an-unknown-interval); [correlated-register diagnostics](../verification/README.md).

### M24 — Finite counters and finite sessions

**Central question:** How can the record fit in finite memory without silently assuming perfect counters?

**Understanding target:** A finite cyclic register agrees with the unbounded signed record on a specified good event. Complete activity bounds control the probability of enough events to alias the register. Final time clipping limits the loss on the bad event. Include countdown states, offsets, initialized bits, output precision and any erasure schedule.

**Dependencies and story role:** M03, M08–M09 and M23. Makes the estimator's record resources finite.

**Conceptual connection:** Attaching a unitary register shift to a source jump preserves that jump's effect bound; this effective record model does not establish a zero-cost laboratory detector.

**Sources:** [Finite record memory](../science/finite_protocol.md#6-finite-record-memory); [complete-device memory account](../science/drift_and_detection.md#5-complete-device-accounting-and-finite-session-memory).

### M25 — A matched finite quantum risk bound

**Central question:** Which terms must be controlled before the inherited source advantage survives?

**Understanding target:** Combine source diffusion, uncertainty in the random reference duration, startup remainder and counter errors under the common source-plus-reference activity budget. Thermal dimension, bare energy width and coherent strength remain separate charges. Each error must fit within the desired elapsed-time risk; a favorable source coefficient alone is insufficient.

**Dependencies and story role:** M12, M20–M24. Integrates the constructive components into one finite resource statement.

**Conceptual connection:** The quantum result is a paid operational protocol in an effective GKLS model, conditional on declared certification and detector resources.

**Sources:** [Joint thermal calibration/use guarantee](../science/thermal_application.md#5-joint-finite-calibration-and-use-regime); [model resource vector](../science/model.md#4-complete-modeled-resource-vector).

### M26 — Necessary reuse and attainable gain

**Central question:** How does bounded calibration overhead limit exploitable quantum improvement?

**Understanding target:** If mean calibration time is at most a fixed multiple of $`KT`$ and the reference peak activity fits within $`G`$, reference exposure is at most of order $`GKT`$. Once exposure reaches the fixed nonzero speed prior's sampling regime, the calibration floor and attainable classical benchmark give a universal $`O(K)`$ gain ceiling. The thermal protocol attains $`\Omega(\min\{K,d^{1-\eta}\})`$ in its stated finite regime.

**Dependencies and story role:** M15, M17 and M25. Joins the converse and construction into the central consequence.

**Conceptual connection:** The universal ceiling concerns K; the inherited construction does not prove a universal intrinsic quantum ceiling at $`d^{1-\eta}`$.

**Sources:** [Reuse ceiling](../science/classical_and_reuse.md#4-a-universal-ceiling-from-calibration-overhead); [attainable regime](../science/classical_and_reuse.md#5-an-attainable-quantum-regime).

### M27 — Expense amortization and cumulative accuracy

**Central question:** What does one calibration share across repeated uses?

**Understanding target:** The same learned conversion factor affects every duration. The noiseless-source Gamma example has shared error covariance proportional to the product of the two durations. Reuse spreads calibration expense at a fixed per-use target, while the calibration error for a cumulative duration grows with that total duration squared.

**Dependencies and story role:** M09, M23 and M26. Establishes the operational meaning and limit of amortization.

**Conceptual connection:** More arbitrary unknown intervals are not additional known-duration calibration samples.

**Sources:** [What can be amortized](../science/classical_and_reuse.md#6-what-can-be-amortized); [sharp oracle example](../science/reference_converse.md#5-sharpness-in-the-noiseless-source-limit).

### M28 — Certification and detector requirements

**Central question:** Which supplied accuracies must improve to expose a smaller source diffusion?

**Understanding target:** An unknown fixed reference multiplier creates an exact scale ambiguity and a squared-duration floor. Independent detector loss or sign flips adds noise proportional to total capture activity, even when the true signed current is highly regular. Match the required certification and detector accuracies to the target risk; their preparation cost is not derived by the source theorem.

**Dependencies and story role:** M03, M10, M25–M26. Makes the remaining accuracy resources visible beside the gain.

**Conceptual connection:** Reduced observed-source fluctuations do not automatically certify an accurate physical time unit or a sufficiently faithful detector.

**Sources:** [Reference-rate obstruction](../science/drift_and_detection.md#1-uncertain-reference-rate); [detector response](../science/drift_and_detection.md#4-imperfect-signed-event-detection); [thermal requirements](../science/thermal_application.md#6-detector-requirement-and-the-physical-scope).

### M29 — Drift and calibration lifetime

**Central question:** How long can a learned speed remain useful?

**Understanding target:** Later speed mismatch is indistinguishable from a changed unknown duration, producing risk of order squared fractional mismatch times duration squared. A logarithmic drift-rate promise yields a sufficient reuse-age condition. Continuous drift during an interval already creates an obstruction after perfect initial calibration; drift during calibration itself requires a separate tracking analysis.

**Dependencies and story role:** M07, M10 and M26–M28. Limits the stable lifetime needed by the amortization argument.

**Conceptual connection:** The proved upper bounds use deterministic drift or drift independent of source noise; output-adaptive changes cannot be inserted into a fixed-time moment bound without another argument.

**Sources:** [Post-calibration drift](../science/drift_and_detection.md#2-post-calibration-speed-changes); [continuous drift and lifetime](../science/drift_and_detection.md#3-continuous-drift-and-calibration-lifetime).

### M30 — The complete operational conclusion

**Central question:** When does paid calibration preserve a consequential quantum timing advantage?

**Understanding target:** State the reference floor, the complete classical benchmark, the finite signed-current construction and the stable-reuse conditions as one qualified result. Keep the common unknown accessible speed, classical-reference restriction, prior width, finite onset, supplied certification/detection and effective-model limit order together. Distinguish finite diagnostic evidence from general proofs and unresolved priority or implementation claims.

**Dependencies and story role:** M13–M29. Synthesizes the narrative into its useful conclusion and boundaries.

**Conceptual connection:** An accurate autonomous source becomes a useful calibrated stopwatch only when its reference exposure, record resources and stability meet the full task's error budget.

**Sources:** [Scientific route](../science/README.md); [model](../science/model.md); [matched consequence](../science/classical_and_reuse.md); [scope and attribution](../references/RELATED_WORK.md); [verification limits](../verification/README.md).

## Coverage of the map

The first phase culminates in the complete task at M12. The second phase develops two connected strands: the universal information limit (M13–M17) and the finite constructive protocol (M18–M25), joined by the reuse law at M26. M27–M30 integrate cumulative accuracy, certification, detection, drift and the final qualified result.

These targets support global understanding of this project. Specialist proofs, numerical details and neighboring topics remain in their authoritative sources; this map does not claim to cover every technical detail.

