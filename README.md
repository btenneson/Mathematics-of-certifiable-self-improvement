# Mathematics of Certifiable Self-Improvement

**Status: public-facing website prepared in `docs/`; actual deployment depends on GitHub settings.**

This research collection studies proof-carrying revision, costed self-improvement, finite settlement games, information-aware choice, verifier contracts, and successor evidence. It is a **research library**, not a claim that a production self-improving AI exists.

## Picard papers — featured slots 1 and 2 (24 November 2026)

The library front page now features two articles **by Picard**: [The Geometry of Mathematical Obstruction](docs/picard-geometry.html) and [Depths of a Possible Machine](docs/picard-depths.html). Each has a full-text web edition and original LaTeX source in `docs/library/01_Core_Theory/Picard/`. Their PDF compilation is managed by the narrowly scoped `.github/workflows/build-picard-pdfs.yml` workflow.

**About Picard:** Picard is a named ChatGPT mathematical drafting and analysis role working under Brian Tenneson's research direction, not a separate autonomous computer or a proof-certified intelligence. It proposes, analyzes, and revises formal mathematics, including potential counterexamples and verifier obligations. The earlier formal Picard Protocol is a mathematical topic, not evidence this research role implements a self-modifying machine.

## Library navigation

- [Research catalog and full manuscript reader](docs/index.html) — 52 PDFs, searchable by title and category, each with a full-page viewer and separate download link.
- [Core theory W0–W3](docs/theory.html) and [the theory guide](core/CORE_THEORY_GUIDE.md).
- [Finite browser lab](docs/lab.html) — illustrative costed-game / quotient / receipt examples.
- [Meaning-based search](docs/semantic-search.html) — optional on-device title-and-summary embeddings, not full-text PDF semantics.
- [Internal editorial 2D ratings CSV](ratings/AI_Self_Improvement_2D_Ratings.csv) — private working scores, deliberately absent from the reader-facing site.
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

## Website publication

The `docs/` website contains 52 cataloged PDFs and 20 available supporting files, with seven missing archival records. See [Pages activation instructions](DEPLOY_GITHUB_PAGES.md). Publishing from a private repository requires an eligible paid GitHub plan; publishing from a public repository is available on GitHub Free. Public repository visibility also exposes the repository history and internal ratings outside `docs/`.

## Optional local Chrome preview on Windows

**Local preview remains available independently of GitHub Pages.** GitHub's folder listing is not the research website. To open the actual website, make a local copy of your private repository:

1. While signed into GitHub, [download the ZIP from your private repository](https://github.com/btenneson/Mathematics-of-certifiable-self-improvement/archive/refs/heads/main.zip).
2. In Windows File Explorer, choose **Extract All** (do not open from inside the ZIP).
3. Open the extracted folder and double-click **OPEN_PRIVATE_LIBRARY_WINDOWS.bat**. This launches a local website in Chrome or your default browser.

If Python is available, the launcher starts a small HTTP server bound only to `127.0.0.1` (your laptop), at `http://127.0.0.1:8765/docs/`. If Python is not available, it opens `docs/index.html` as a local file. In that fallback mode, the library catalog, full PDF reader, original PDFs and finite lab are available; optional semantic search requires an HTTP server and an additional model download.

All document links are **relative links into the website's `docs/library` folder**, working both online through Pages and in local preview. The current website catalog includes 52 available PDFs. Seven supporting text/source files are still missing from the curated selection. [Private viewer setup](PRIVATE_PREVIEW.md).

## Research-status boundaries

Internal scores are **provisional editorial assessments**, not peer review, and are not displayed to readers. If the entire repository is later made public, remove the internal scorecard first if it should stay private. Manuscript-level proof claims, finite sanity checks, independent formal certification, and real-world machine improvements are distinct. The Python checker in `library/04_Protocols_and_Research_Records/Finite_Example_Checks/` contains seven finite examples and does not validate the general program. Browser examples are likewise illustrative. Ordinary catalog search runs without external services; semantic search optionally downloads an open model from a third-party CDN. **Full-PDF passage indexing has not yet been installed.**

Historical paths have been moved into `library/` while preserving the Git commit history. No original PDF contents were edited in the reorganization.
