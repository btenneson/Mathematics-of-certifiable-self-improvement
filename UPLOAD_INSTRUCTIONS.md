# Remaining upload instructions

The 64 available catalog files are already organized under `library/`. **Do not re-upload or rename those files.**

Only seven source records remain absent. Read [MISSING_FILES.md](MISSING_FILES.md) for their exact destination paths. Their expected filenames and SHA-256 values can be found in [library/00_Selected_Files_Manifest.csv](library/00_Selected_Files_Manifest.csv).

Upload the exact original files at the indicated `library/` paths and update `docs/catalog.js` entries from `available:false` to `available:true` with correct canonical GitHub links. Do not overwrite a different revision or invent missing content. Full-PDF passage search remains a separate, not-yet-built feature.
