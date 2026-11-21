# Private research library — Chrome on Windows

Your GitHub repository and all original research files remain **private**. This is a designed local website, **not** a GitHub Pages publication. The public `github.io` link returns 404 because the site has not been published, and you have explicitly requested privacy.

## Open the private website

1. While logged into GitHub as `btenneson`, [download your private repository ZIP](https://github.com/btenneson/Mathematics-of-certifiable-self-improvement/archive/refs/heads/main.zip).
2. In Windows, right-click the ZIP, choose **Extract All**, and open the extracted folder.
3. Double-click `OPEN_PRIVATE_LIBRARY_WINDOWS.bat`. The browser opens to the actual library website, not GitHub's folder listing.

The batch file uses Python if installed to launch a local server on **127.0.0.1**, accessible only on your laptop. It starts `http://127.0.0.1:8765/docs/`. No Python? It opens the library directly at `docs/index.html`, which supports title/summary search, 2D ratings, PDF reading and finite lab.

To open Chrome specifically rather than the Windows default browser, paste `http://127.0.0.1:8765/docs/` into Chrome after using the launcher. If Python is unavailable, drag the extracted `docs/index.html` file into Chrome.

## Search and privacy details

- The catalog searches PDF **titles and summaries**; it is not full-text passage search.
- Meaning-based search optionally loads an open embedding model over the network when used. To keep the viewer fully offline, don't use that optional feature.
- The 48 available PDF links point to the files in your local extracted copy. They no longer open GitHub's folder UI.
- The W0–W3 theory guide and finite lab are included.
- Seven supporting text/source documents are missing from the source selection, but all 48 PDFs are present.

## Updating your private library

When the repository changes, download and extract the ZIP again. The local copy is a snapshot and does not synchronize automatically. No paid API or public website is needed.

GitHub Pages should **not** be enabled for the private use case. This setup supports local access on the laptop; it does not create a private remotely hosted website for mobile devices.
