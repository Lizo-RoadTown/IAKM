@echo off
REM build_preprint.bat - Build the Preprints.org submission version
REM
REM Target venue: Preprints.org (MDPI). Uses the MDPI class in
REM preprint\Definitions\, which ships with the Preprints.org LaTeX template.
REM
REM Body prose, tables, and references are identical to the IEEE conference
REM version in paper_v7\. Only the container differs, so a change to the
REM paper must be made in BOTH .tex files.
setlocal

set "MIKTEX_BIN=%LOCALAPPDATA%\Programs\MiKTeX\miktex\bin\x64"
set "PATH=%MIKTEX_BIN%;%PATH%"
cd /d "%~dp0.."

set "TEX=IAKM_Preprints.tex"
set "DIR=preprint"
set "BASE=IAKM_Preprints"

echo === IAKM: Preprints.org submission ===

if not exist "%DIR%\%TEX%" (
    echo [ERROR] Not found: %DIR%\%TEX%
    exit /b 1
)

REM Compile from the .tex's own directory so Definitions\ and the figure
REM paths resolve.
pushd "%DIR%"

echo [1/2] First pass...
pdflatex -interaction=nonstopmode "%TEX%" >nul 2>&1

echo [2/2] Second pass (resolving references)...
pdflatex -interaction=nonstopmode "%TEX%" >nul 2>&1

if not exist "%BASE%.pdf" (
    echo [ERROR] No PDF produced. Rerunning to show the error:
    pdflatex -interaction=nonstopmode "%TEX%"
    popd
    exit /b 1
)

echo.
echo [OK] Output: %DIR%\%BASE%.pdf

del /q "%BASE%.aux" 2>nul
del /q "%BASE%.log" 2>nul
del /q "%BASE%.out" 2>nul
del /q "%BASE%.synctex.gz" 2>nul
del /q "%BASE%.spl" 2>nul
del /q "%BASE%.bbl" 2>nul
del /q "%BASE%.blg" 2>nul
del /q "%BASE%.toc" 2>nul
del /q "%BASE%.loe" 2>nul
echo [OK] Build artifacts cleaned.

popd
endlocal
