# Mathematics of Certifiable Self-Improvement

**Status: private source repository. The publicly readable website is ready for Pages activation.**

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

## Private repository, publicly readable website

The requested arrangement is a **private GitHub source repository with a publicly accessible GitHub Pages site**. The `docs/` website now includes the research files and 2D ratings needed to display them through GitHub Pages. Do not change repository visibility. See [Pages activation instructions](DEPLOY_GITHUB_PAGES.md). Publishing from a private repository requires a GitHub Pro, Team, or Enterprise plan; GitHub Free cannot activate this Pages arrangement.

## Optional local Chrome preview on Windows

**The repository and the papers remain private. No GitHub Pages site is configured or requested.** GitHub's folder listing is not the research website. To open the actual website, make a local copy of your private repository:

1. While signed into GitHub, [download the ZIP from your private repository](https://github.com/btenneson/Mathematics-of-certifiable-self-improvement/archive/refs/heads/main.zip).
2. In Windows File Explorer, choose **Extract All** (do not open from inside the ZIP).
3. Open the extracted folder and double-click **OPEN_PRIVATE_LIBRARY_WINDOWS.bat**. This launches a local website in Chrome or your default browser.

If Python is available, the launcher starts a small HTTP server bound only to `127.0.0.1` (your laptop), at `http://127.0.0.1:8765/docs/`. If Python is not available, it opens `docs/index.html` as a local file. In that fallback mode, the library catalog, original PDFs, ratings and finite lab are available; optional semantic search requires an HTTP server and an additional model download.

All document links are **relative links into the website's `docs/library` folder**, working both online through Pages and in local preview. The catalog includes 48 available PDFs. Seven supporting text/source files are still missing from the curated selection. [Private viewer setup](PRIVATE_PREVIEW.md).

## Research-status boundaries

Scores are **provisional editorial assessments** and not peer review. Manuscript-level proof claims, finite sanity checks, independent formal certification, and real-world machine improvements are distinct. The Python checker in `library/04_Protocols_and_Research_Records/Finite_Example_Checks/` contains seven finite examples and does not validate the general program. Browser examples are likewise illustrative. Ordinary catalog search runs without external services; semantic search optionally downloads an open model from a third-party CDN. **Full-PDF passage indexing has not yet been installed.**

Historical paths have been moved into `library/` while preserving the Git commit history. No original PDF contents were edited in the reorganization.
