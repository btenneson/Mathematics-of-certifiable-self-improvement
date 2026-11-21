# FORGE-6-E — Part I experimental blueprint (proposal only)

**Research Director:** Brian Tenneson  
**Source:** *Certified Self-Improving Mathematical Discovery*, Part I, foundational integration 001 (November 16, 2026).  
**Status:** NOT EXECUTED. No installed FORGE-6-E binary, proof-kernel receipt, revision, or measured performance is supplied by this file.

## Purpose

Translate Part I into a reproducible process for evaluating whether a FORGE candidate improves a frozen ATP implementation while retaining mathematical correctness. This blueprint does not itself activate or modify a theorem prover. It is an experimental specification that a future FORGE controller, independent checker, and benchmarking harness may implement.

## Freeze before proposing

Create a new immutable experiment ID and capture all of the following:

- Baseline executable/source snapshot, commit or hash, dependency versions, configuration, proof checker version and trusted-base assumptions.
- Precise target, hypotheses, proof calculus, allowable inference rules, output and settlement meanings, and allowed certificate types.
- SIC/ATP type of the tested system. Do not assume every SIC satisfies ATP obligations.
- Simulator and simulated subject identities; record explicitly when the two are distinct (`P != S`).
- Workloads for candidate generation, validation and held-out testing. Disclose selection and any overlap.
- Admitted candidate changes, machine resources, prior knowledge and reuse permissions for **both** comparators.
- Scheduler, branching, hidden-information, failure, restart, and random-seed assumptions.
- Budget, cost accounting units, all incurred search attempts and verification/deployment costs.
- Declared success rule; prohibited silent changes to any frozen field.

## Candidate lifecycle

| Gate | What must be supplied | Possible result |
| --- | --- | --- |
| 0. Baseline | Verifiable frozen snapshot and matching task/cost environment | Ready / blocked |
| 1. Proposal | Candidate code, derivation, prior knowledge use, and all discovery costs | Proposed / aborted |
| 2. Mathematics | Proof or sound checker-accepted certificate in the same scoped calculus | Mathematically accepted / rejected / unresolved |
| 3. Correspondence | Trusted argument or verified check matching installed code to claimed semantics | Implementation accepted / unresolved |
| 4. Behavior | All admitted branches/outputs checked to the scope of the claim | Safe / unsafe / unresolved |
| 5. Economics | Complete total cost for matched baseline and revision, including failed candidate search | Beneficial / not beneficial / unresolved |
| 6. Decision | Independent receipt and explicit authorized adoption / rejection | Installed / not installed / provisional |

**Keep mathematical certificate status separate from experimental performance status.** A fast trace is not a proof. A shorter proof horizon is not necessarily cheaper computation. A frozen baseline is not the best equally informed adaptive rival.

## Quantitative report

Report at least: test-set cardinality; checked target coverage; invalid/unsupported outputs; mean/median/maximum cost on a **common, disclosed instance population**; costs of unsolved instances; setup/discovery/verification/install/restart/storage/communication charges; total benchmark cost; proof-horizon changes; branch coverage; and number and cost of rejected candidates.

For a frozen `N`-episode workload with valid certified bounds, a sufficient economic inequality is:

`B_max + N*q_max < N*p_min`

`B_max` must include **actual unsuccessful search** and every required once-only expense. If no valid bound exists, a claim of strict all-in benefit is unresolved even if the new implementation has a faster observed median.

## Suggested first six experiments

1. **Proof macro reuse:** Three-step derivation vs a checked macro; independently audit checker replay and the marginal lookup charge.
2. **Generalization:** Macro learning on `W_train`, controlled held-out proof-family test on `W_test`; prevent leakage and disclose overlap.
3. **Candidate generator:** Improve the proposer only, leaving the base proof checker unchanged; charge rejected attempts.
4. **Simulator update:** Improve an ATP's simulation method; require a new correspondence witness, especially if simulator `P` differs from subject `S`.
5. **Coordinated revision:** Investigate a pair of individually unattractive changes that may help jointly; require full composition and joint-cost certificates.
6. **Evidence handoff:** Test versioned proof replay or sound translation to a successor without silently changing assumptions or rights.

## Status discipline

- `PROPOSED`: A candidate exists; not a successful revision.
- `PAPER_PROVED`: A mathematical argument has been provided, not yet independently checked.
- `CHECKED`: The declared independent verifier accepted a specified scope, with a recorded receipt.
- `EMPIRICALLY_BENEFICIAL`: A precommitted, fully charged matched comparison supports benefit on the stated workload; not a universal guarantee.
- `REJECTED`: The checker or contract rejected the proposal; record reason and costs.
- `UNDETERMINED`: Investigation incomplete or cost/coverage/certificate missing; not a proof of impossibility.
- `MODEL_REPAIR`: Inconsistent contract, missing essential assumptions, or invalid correspondence; freeze prior record before repair.

These are **experiment workflow labels**, not replacements for the AMLD+0 logical settlement outcomes `P,R,D,I,C,U`. Only genuine accepted theorem certificates belong in a verified mathematical BANK.

## Preservation rule

Never overwrite the pre-revision baseline or prior experiment. Every run is an append-only versioned record. If a candidate is rejected, retain the failed attempt, consumed budget, and rationale. If a later candidate is adopted, preserve both branches of the lineage. Do not start an experiment from this Markdown merely because it appears in a chat window: explicit controller, executable implementation, test harness, and independent verification are still required.

## Minimal concrete sample — NOT AN OBSERVATION

The Part I toy example freezes a chain `a -> b -> c -> d` and a compiler that proposes `a => d` with a derivation witness. Its **stipulated accounting model** gives baseline `3N`, new `5 + N`, and a saving of one unit at `N = 3`. The attached JSON uses these **model numbers only** to illustrate which fields a real test must replace with verified observations. No claims about FORGE running, being modified, or having achieved that saving are made.

## Attribution and verification boundary

The mathematical source papers are Brian Tenneson's August 2026 *Companion Syllabus for the Picard Feedback Loop* and *Certified Operator Dynamics on the Space of Theorem Provers*. The integrated Part I has been prepared by ChatGPT (OpenAI), under the research direction of Brian Tenneson. This blueprint has not been independently checked or executed. Use the Part I paper's PROOFS appendix and verification notice for the exact mathematical assumptions.
