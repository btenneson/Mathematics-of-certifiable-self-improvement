# FORGE-6-E — Immutable Checkpoint and Handoff Ledger Template

**Fill from actual files and observed runs only.** The following is a template, not an assertion that these events occurred. Duplicate with a unique version label for each checkpoint. Preserve every prior checkpoint and all rejected/provisional results.

```yaml
schema: FORGE6E-CHECKPOINT-1
checkpoint_id: F6E-CP-000
created_at: NOT_RECORDED
research_director: Brian Tenneson
version: F6-E-000
prior_version: FORGE-6-ORIGINAL
execution_level: CHAT-PROTOCOL
restoration_level: R0_DOCUMENTED_SPECIFICATION
runtime_status: NOT_CONNECTED
original_baseline:
  id: F6-BASELINE-000
  source_files: []
  source_sha256: {}
  checkpoint_sha256: UNKNOWN
  repository_commit: UNKNOWN
  model_and_engine: UNKNOWN
  original_mapping: FORGE6-PROTOCOL-1.0
  role_mapping_note: 'B0 coordinator; B1 backward; B2 forward; B3 Eureka; B4 adversarial; B5 SIGNALS'
  actually_observed_role_run_ids: []
contract:
  formal_system_F: NOT_PROVIDED
  original_hypotheses_Gamma: NOT_PROVIDED
  exact_target_T: NOT_PROVIDED
  checker_V: NOT_CONNECTED
  checker_source_sha256: UNKNOWN
  certificate_language: NOT_PROVIDED
  K0_bank_sha256: UNKNOWN
  scheduler_and_fairness: NOT_PROVIDED
  hidden_information: NOT_PROVIDED
  allowed_revision_actions: NOT_PROVIDED
  runtime_and_hardware: NOT_PROVIDED
  budget_and_unit: NOT_PROVIDED
  full_cost_schedule: NOT_PROVIDED
  task_family_W: NOT_PROVIDED
  seeds_and_controls: NOT_PROVIDED
  test_split: NOT_PROVIDED
ledgers:
  K0_immutable_receipts: []
  D_verifier_accepted_separate_receipts: []
  U_provisional_failed_untrusted: []
  H_prior_run_refs: []
  rejected_candidates: []
  open_obligations: []
revision:
  candidate_id: NONE
  generator_code_hash: UNKNOWN
  generated_by_current_running_D: NOT_ESTABLISHED
  proposal_status: NONE
  original_method_replay: NOT_TESTED
  old_proof_handoff: NOT_TESTED
  B0_to_B5_real_execution: NOT_OBSERVED
  independent_verifier_receipt: NONE
  all_branches_covered: NOT_TESTED
  full_cost_check: NOT_TESTED
  operator_install_authorization: NOT_GIVEN
  installed_version: NONE
  rollback_source: UNKNOWN
evaluation:
  comparator_permissions: NOT_PROVIDED
  tasks: []
  Reach_old: NOT_MEASURED
  Reach_new: NOT_MEASURED
  Next_old: NOT_MEASURED
  Next_new: NOT_MEASURED
  ForcedReach_old: NOT_MEASURED
  ForcedReach_new: NOT_MEASURED
  cost_old: NOT_MEASURED
  cost_new_including_upgrade: NOT_MEASURED
  certified_success_old: NOT_MEASURED
  certified_success_new: NOT_MEASURED
  failures_and_variance: NOT_MEASURED
  protected_regressions: NOT_TESTED
  result: UNDETERMINED
next_legal_action: 'restore actual original source and checker, or propose candidate provisionally'
```

## Historical evidence ledger (append entries; never backfill claims)

```markdown
### Entry [unique ID]
- Date/time with time zone:
- Actual actor / B-role / process ID (or 'sequential ChatGPT analysis'):
- Frozen task manifest hash:
- Type: SOURCE | PROPOSAL | CERTIFICATE | CHECKER_RESULT | NEGATIVE_RESULT | COST | HANDOFF | APPROVAL | ROLLBACK
- Claim / exact proposition:
- Source artifact, line/commit, certificate URI or local path:
- Verifier binary/version/hash and exact response:
- Costs, units, repeated work and credits:
- Dependencies and rights:
- Status: OBSERVED | CHECKED | PROVISIONAL | REJECTED | UNDETERMINED | MODEL_REPAIR
- Link to predecessor entry:
- No-hindsight note:
```

## Transfer to another ChatGPT window

Attach (1) `FORGE-6-E_ACTIVATE.md`, (2) this **filled** checkpoint, and (3) any source/checker/certificate files that the claimed state depends on. Request: "FORGE-6-E REMEMBER. Verify the checkpoint's supporting artifacts. Resume at next_legal_action. Do not promote unsupplied receipts to VERIFIED." Keep the old checkpoint intact and create a new one after the session. Never paste secrets/API credentials into the ledger.
