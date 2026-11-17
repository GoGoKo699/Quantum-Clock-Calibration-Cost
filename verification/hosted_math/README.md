# Hosted mathematical verification

The read-only workflow captures actual commit-pinned GitHub reader pages at widths 1440 and 760, compares accessible MathML with each exact source expression, and retains screenshots for visual review. It probes the thermal page first, then covers all tracked Markdown reader pages. A structural pass is distinct from scientific proof review and visual inspection.

The collector and checker are retained unchanged with exact hashes in [helper provenance](helper-provenance.json). [The text contract](headline-contract.json) adds explicit checks for central equations. Capture dependencies are installed into the runner's temporary directory. The job uses contents: read, checks out the same-repository PR head, and does not persist credentials or accept secrets.

Generated captures and their source-bound reports are evidence artifacts, not scientific source. Their temporary retention is not durable preservation. The final review must inspect screenshots, retain important observations and bind the final report to the actual merged source.
