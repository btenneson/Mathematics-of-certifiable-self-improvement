@echo off
setlocal
cd /d "%~dp0"
title Private Research Library
echo Your research stays on this computer. No public hosting.
echo.
py -3 --version >nul 2>&1
if not errorlevel 1 goto py_launcher
python --version >nul 2>&1
if not errorlevel 1 goto py_direct
goto html_fallback

:py_launcher
echo Starting local site at http://127.0.0.1:8765/docs/
start "Private Research Library Server" /min cmd /k "py -3 -m http.server 8765 --bind 127.0.0.1"
goto browser

:py_direct
echo Starting local site at http://127.0.0.1:8765/docs/
start "Private Research Library Server" /min cmd /k "python -m http.server 8765 --bind 127.0.0.1"
goto browser

:browser
timeout /t 2 /nobreak >nul
start "" "http://127.0.0.1:8765/docs/"
echo.
echo To stop the server, close the minimized server window.
exit /b 0

:html_fallback
echo Python is not installed. Opening the library directly.
echo Catalog, PDFs, ratings and finite lab work without Python.
echo Optional semantic search requires a local HTTP server.
start "" "%CD%\docs\index.html"
echo.
pause
