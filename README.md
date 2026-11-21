# Mathematics of Certifiable Self-Improvement

**Status: private staging; not publicly published.** The repository is organized and ready for review before the owner chooses to make it public.

This research collection studies proof-carrying revision, costed self-improvement, finite settlement games, information-aware choice, verifier contracts, and successor evidence. It is a **research library**, not a claim that a production self-improving AI exists.

## Library navigation

- [Research catalog and 2D ratings](docs/index.html) — 48 PDFs, with research rating and relevance to AI improvement.
- [Core theory W0–W3](docs/theory.html) and [the theory guide](core/CORE_THEORY_GUIDE.md).
- [Finite browser lab](docs/lab.html) — illustrative costed-game / quotient / receipt examples.
- [Meaning-based search](docs/semantic-search.html) — optional on-device title-and-summary embeddings, not full-text PDF semantics.
- [2D ratings CSV](ratings/AI_Self_Improvement_2D_Ratings.csv).
- [Curated originals](library/) — four thematic series with their original filenames retained.
- [Missing-source checklist](MISSING_FILES.md) — seven text/source records still awaiting upload.

## Collection status (2026-11-21)

The original selected catalog contains **71 entries: 48 PDF manuscripts and 23 companion/source/metadata files**. **64/71** are present in the organized `library/` paths, including **all 48 PDFs**. Seven non-PDF files remain missing. Five PDFs originally uploaded using shortened `DEPTHS~` and `TRIANG~` names now appear at the intended catalog paths; their stored Git blobs were reused, without rewriting PDFs. The curation manifest records the original selection and hashes; this migration did not independently re-hash the five shortened uploads.

The complete source archive was previously screened from 362 file entries to 69 retained research/support originals, plus two new provenance files. The selection rationale and SHA-256 hashes are preserved in [the original selection note](library/00_README_Selection.md) and [manifest](library/00_Selected_Files_Manifest.csv).

## Organized folders

1. `library/01_Core_Theory/` — 21 files including FDWC W0–W3, Picard dynamics, revision, and successor evidence.
2. `library/02_Formal_Foundations/` — 18 files on awareness, simulations, verification, and formal epistemology.
3. `library/03_Search_Settlement_and_Discovery/` — 15 available files on AMLD, CAMI, elusiveness and settlement (one LaTeX companion missing).
4. `library/04_Protocols_and_Research_Records/` — 8 available files, including retired FORGE-6 research blueprints and finite check code (six related text records missing).

The `FORGE-6` materials are **historical research records**, not an active deployed system. CAMI is the current focus for self-improvement research.

## Preview and eventual publication

On desktop: from the repository root run `python -m http.server 8000`, then visit `http://localhost:8000/docs/`. The layout supports mobile browsers. PDF links intentionally point to their **canonical GitHub file pages**, so they also work on GitHub Pages when this repository becomes public.

After editorial/privacy and attribution review, the owner may change repository visibility to **public**, then open **Settings → Pages → Build and deployment**, choose **Deploy from a branch**, `main`, `/docs`, and save. The expected public site address will be `https://btenneson.github.io/Mathematics-of-certifiable-self-improvement/` **only after GitHub Pages has been enabled and the deployment succeeds**. See [publishing checklist](PUBLISHING.md).

## Research-status boundaries

Scores are **provisional editorial assessments** and not peer review. Manuscript-level proof claims, finite sanity checks, independent formal certification, and real-world machine improvements are distinct. The Python checker in `library/04_Protocols_and_Research_Records/Finite_Example_Checks/` contains seven finite examples and does not validate the general program. Browser examples are likewise illustrative. Ordinary catalog search runs without external services; semantic search optionally downloads an open model from a third-party CDN. **Full-PDF passage indexing has not yet been installed.**

Historical paths have been moved into `library/` while preserving the Git commit history. No original PDF contents were edited in the reorganization.
