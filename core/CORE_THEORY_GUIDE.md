# The mathematics of certifiable self-improvement — working theory map

**Status: private staging draft.** This is a navigation and experimentation guide to a collection of manuscripts, not an independent theorem audit, formal-verification report, or claim that a self-improving AI has been built.

## Central problem

Can a theorem-proving or mathematical-discovery system *improve its procedures* while preserving what its verifier can actually certify—and can the improvement still be worthwhile once all costs of constructing, checking, and installing the revision are charged?

A useful sequence is:

**W0 (base architecture) → W1 (costed revision game) → W2 (future-sufficient quotient) → W3 (information and receipts) → successor handoff / measured improvement.**

### W0 — Certified self-improving mathematical discovery

The unifying foundation examines proof-producing revisions, conservative theoremhood, fully charged search and compilation costs, and the boundary between a proposed revision, a verified certificate, and the installed change. The source manuscript is `Certified_Self_Improving_Mathematical_Discovery_Strengthened_002(1)v2(5).pdf` in `library/01_Core_Theory/FDWC_W0/`.

**Boundary:** A mathematical construction about an improver does not establish that a deployed system improves itself.

### W1 — Certified revision as a costed game

An accepted revision is an edge in a finite contract-dependent game only when every mandatory verification requirement succeeds. Controller/adversary turns, costs and certified target states determine a *forced* settlement value—not merely a possible path. Under the stated assumptions, conservative certified macros preserve base-calculus theoremhood along finite accepted revision paths.

A frozen contract is named in the source as `K=(F,Γ,W,I,E,R,O,κ,B,Q,V)`; interpretation of the components and all theorem conditions belongs to the source paper.

**Important:** Finite reachability tests do not certify the correctness or completeness of the modeled machine or its real costs.

### W2 — Future-sufficient revision quotients

Given a finite labeled costed game, refine partitions until states in one block have the same contract-relevant label and matching costed successor-block signatures. A stable quotient preserves the specified forcing values for the *explicit finite game*. The quotient is not necessarily the smallest abstraction under every weaker criterion.

**Important:** Preserving a model's value is distinct from proving the model captures real deployed behavior.

### W3 — The price of knowing which revision to make

For a partially observed game, policies act on observable histories and admissible belief states. The proposed finite belief-game translation preserves the sure-forced settlement value under the stated conditions. A finer observation can weakly improve a forcing policy when its acquisition is free; a paid observation must be compared with its full acquisition cost.

**Important:** More information is not automatically worth its price, nor does an abstract receipt validate an external sensor.

### Cross-cutting themes

* **Verifier boundary:** A proof object, verifier acceptance, deployment, and empirical performance are different events.
* **Full-charge economics:** Search, verification, migration, amortization and measurement matter when comparing procedures.
* **Successor handoff:** A machine-state or method improvement must retain the evidence and contracts needed to justify it.
* **Fixed points, cycles, and stationarity:** A decreasing cost or revision sequence requires explicit assumptions; it is not evidence of unlimited self-improvement.
* **Adversarial search:** Attainment, finite forcing, and indefinite avoidance are different settlement outcomes.

## Runnable, bounded example

`library/04_Protocols_and_Research_Records/Finite_Example_Checks/finite_sanity_checks.py` contains seven standard-library Python tests for finite W1–W3 examples. Run from the repository root:

```bash
python library/04_Protocols_and_Research_Records/Finite_Example_Checks/finite_sanity_checks.py
```

Passing those tests confirms only their implemented finite scenarios. The browser lab (`docs/lab.html`) offers a separate toy-model demonstration; neither constitutes verification of the general theorems.

## Research-quality caveat

The 2D assessments are provisional editorial triage, not peer review. Scores and interpretations are intended to be revised by the research director. Original documents and their hashes are preserved under `library/`.
