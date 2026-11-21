# FORGE-6-E — Certified Self-Upgrade Engine and Test Contract

**Status:** protocol for proposing and checking upgrades, not an installed general ATP. Companion to the standalone activation Markdown. Core mathematical justification is conditional and model-relative, following *What Survives the Successor?* (audited v2).

## 1. Frozen experiment instance

Freeze before any candidate is scored:

`ID, F, Γ, exact T (or predeclared task-family W), V checker/hash, K0/hash, B0..B5 mapping, original source hash, `
`permitted edits, scheduler/fairness, branch ownership and observations, seeds, model/hardware, budget, `
`time/step metric, verification rights, communication semantics, permitted reuse, test partition, trial plan, `
`tie-break priorities, stopping rules, and all charge categories.`

A change to any frozen field creates a **new experiment ID**, not a stealth continuation. Preserve exact old configuration read-only.

## 2. Version transition

`F6-BASELINE-000 -> candidate C_n -> qualified proposal Q_n -> certified admissibility audit A_n ->`
`operator authorization -> versioned candidate installation F6-E-n -> independent matched evaluation -> ACCEPT / ROLLBACK.`

New version is a separate artifact with stable provenance. Do not imply same identity until a method-preserving handoff is evidenced; machine lineage and philosophical identity are not equivalent.

### Candidate must be self-generated, not externally handed in

Proposals must name an actual generator method *present in the current architecture*: e.g. (a) compose two already installed derived rules, (b) discover a low-fan-in bridge candidate from B1/B2 obligations via B3, (c) solve a fully certified cost/reward graph for a two-token coordinated revision, (d) revise a legal SIGNALS routing heuristic based on verified frontier records. If the candidate was invented directly by ChatGPT instead of run by the described generator, mark **externally proposed / not self-generated**. A proposal drafted in a ChatGPT-only session is not evidence the FORGE-6 executable produced it.

## 3. Three-pass generator/adversary/verifier loop

**A — SEARCH:** B0 freezes and schedules. B1 requests subgoals; B2 forwards consequences; B3 proposes Eureka lemmas/architecture edits; B4 attempts counterexamples, negative branches, and fairness challenges; B5 emits costed, typed SIGNALS. Store *every* candidate and route as provisional until a real checker receipt arrives.

**B — AUDIT:** check soundness; macro expansion to original calculus; exact proof dependencies; old code/new code semantics; checker independence; all finite nondeterministic branch outcomes; hidden-information legality; cost units; all failed attempts; evidence-hand-off, method handoff and realistic budget. No unknown or denied gate can be called PASS. Genuine insufficient evidence = UNDETERMINED.

**C — MEASURE / ADOPT:** evaluate old-architecture optimum or sufficiently strong predeclared policy against the proposed successor on the same frozen tasks and rights. Unless actually executed and recorded, provide only mathematical *predictions*, never empirical findings. Installation is a separate explicitly authorized step on a versioned copy; do not self-approve as B0, B3 or verifier.

## 4. Independent upgrade acceptance tests

**Nonnegotiable invariants:** base checker trust boundary retained or separately qualified; no changed target/hypotheses; initial BANK immutable; old accepted certificate scope preserved; no unauthorized new failing branches; old generative methods available or explicitly recorded as withdrawn with operator consent (then not claim strict method-preserving succession); all source/ledger history intact. Safety gate is independent of economic gate.

**Primary score vector on fixed W, b and resource budget:**

- `Reach` = size/set of verifier-accepted targets discovered within b legal search actions; compare set containment or documented priorities, not just count.
- `Next` = verifier-eligible new architecture candidates discoverable by the original generator within generation budget b.
- `ForcedReach` = branch-complete objectives settled, with certified worst-case bound when applicable.
- `KnowledgeTransport` = fraction/set of old scoped proofs and old finite generation traces reproducible under a checked handoff.
- `CostAllIn` = candidate discovery + failed proposals + verification + code/macro creation + signalling + scheduling + communication + I/O + storage + installation + maintenance + restart + old and new execution, with no double-counting or omissions.
- `Reliability` = certified success rate on held-out frozen tasks, failure count, task-to-task variance and worst-case observed loss.
- `Robustness` = response to adversarial controls and poisoned certificates under same checker and observation rules.

Do not pretend that all coordinates can be compared by one scalar without declaring weights/priority and units. Declare protected monotonic coordinates (including correctness) and prove or test **no protected regression**; prefer Pareto-dominant changes with at least one strict improvement. Ties, incomparabilities and underpowered experiments do not count as improvements. A finite suite does not establish global mathematical monotonicity. Test observable capability, not merely latency.

## 5. Proof and economic gates

For a conservative macro, replay every use in the original calculus. For a branchwise settlement strategy, demonstrate *every* adversarial successor matches a valid predecessor continuation and that the successor can compute its old-policy state/observations (or provide a proven compatible quotient); check transition charges and terminal evidence. For an improved policy, compare against a fair old-architecture adaptive optimum, not a disabled straw man. If a rival can adopt the same update at equal/full cost, never assert strict global superiority.

Use the manuscript's abstract theorem only inside its cost semantics:

`R_j: P(t) => P(f^(2^j)(t))`, candidate `R_(j+1)` generated by composing `R_j` twice; `B_j=2^(j+1)+4`; `C_old=2N`, `C_new=B_j+N`, beneficial iff `N>B_j` on that frozen workload. The corresponding real program may have different term/encoding, checking, lookup and I/O costs. Recompute thresholds if those change.

For repeated tasks, old-policy per-episode **lower bounds** and new-policy per-episode **upper bounds** must hold uniformly over admissible prior histories and reuse. Do not assume an expensive one-off certificate amortizes over a workload that is not actually frozen or permissible.

## 6. Plateau and coordinated escape

Detect plateau only against a declared revision menu and resource horizon. A failed local search is not a global fixed-point certificate. Allow a batch `{u,v,...}` when the exact permitted bundle family and interactions are certified. Verify sign, hyperedge prerequisites and **all** costs; a max-closure/min-cut result applies only when feasibility is exactly prerequisite closure and interaction rewards are nonnegative. On arbitrary unknown interactions, retain uncertainty. Do not revise target, checker or hidden information to escape.

Example controlled calculation: `C(empty)=10, C({u})=11, C({v})=11, C({u,v})=4`. A certified table plus internal solver can choose a beneficial bundle. This is a **paper example**, not FORGE-6-E run evidence. If cost of discovering coefficients is not included, no full-economy claim follows.

## 7. Outcomes and automated stopping rules

- `ACCEPT`: independent proof/checker gate passed, explicit operator authorization, required protected invariants, predeclared improvement criterion passed with receipts; archive both versions.
- `REJECT`: an actual falsifying counterexample, failed certificate, protected regression or negative full-cost result; retain reasons.
- `DEFER`: legal revision but budget, data or economic horizon inadequate; preserve candidate.
- `UNDETERMINED`: insufficient evidence, exhausted search, unavailable checker, no admissible comparison.
- `MODEL_REPAIR`: inconsistent cost types, missing branch, unverifiable code correspondence, incompatible assumptions; stop claims until repaired under *new* manifest.

Never convert failure to find a solution into a proof of impossibility. Do not claim independence without the necessary two-sided evidence. Always state what was actually executed.

## 8. Export format and upgrade handoff

Emit append-only records with old/new hashes, role mapping, exact target, model/runtime, D/U/H ledgers, code diff summary, proof and method replay logs, checker receipts, budget, all charged costs, results for each protected coordinate, rejected alternatives, branch coverage, candidate status, operator authorization, rollback snapshot pointer and next eligible action. See `FORGE-6-E_CHECKPOINT_TEMPLATE.md`.
