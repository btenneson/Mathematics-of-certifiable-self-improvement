# Finish importing the private library — one browser upload

The library's responsive interface and theory guide are already installed in this private repository. The 75 remaining source and index files are in the companion archive:

**Certifiable_AI_Improvement_GitHub_Completion_Upload.zip**

1. On your Windows computer, download the companion ZIP from the ChatGPT conversation and select **Extract All**.
2. Open the extracted folder. You should see four top-level folders: `library`, `docs`, `ratings`, and `scripts`. **Drag those four folders, not the outer enclosing folder.**
3. In this private GitHub repository, choose **Add file → Upload files**. Drop the four folders together; GitHub supports folder drag-and-drop and up to 100 files in one browser upload. This package contains 75 files, and none exceeds 25 MiB.
4. Review the list of file paths: they should begin with `library/`, `docs/`, `ratings/`, or `scripts/`. Then commit to `main`.
5. The original 71 files should now be present under `library/`. The 48 PDFs and full-text search data are required for the catalog's document links and passage search to work.

To preview the site **without making anything public**, download the repository locally, run `python -m http.server 8000` in the repository root, and open `http://localhost:8000/docs/`. For a mobile browser on the same trusted Wi-Fi, the PC can temporarily serve the site to its LAN address, with appropriate firewall restrictions.

Do not enable GitHub Pages until ready to publish: Pages sites are generally public even when the underlying repository is private. Until then the repository's content stays private, while a private hosted/mobile site would require a separate authenticated hosting setup.

The `core/CORE_THEORY_GUIDE.md` and `docs/lab.html` cover W0–W3, with a small independent browser demonstration. The included seven Python finite checks are not a formal proof of a deployed self-improving theorem prover.
