# Remaining upload instructions

The public-facing catalog currently has 72 available files under `docs/library/`. **Do not re-upload or rename those files.**

Only seven source records remain absent. Read [MISSING_FILES.md](MISSING_FILES.md) for their exact destination paths. Their expected filenames and SHA-256 values can be found in [library/00_Selected_Files_Manifest.csv](library/00_Selected_Files_Manifest.csv).

Upload the exact original files at the corresponding `docs/library/` paths (and preserve an archive copy under `library/` if desired) and update `docs/catalog.js` entries from `available:false` to `available:true` with relative local-viewer links (`library/...`). Do not overwrite a different revision or invent missing content. Full-PDF passage search remains a separate, not-yet-built feature.
