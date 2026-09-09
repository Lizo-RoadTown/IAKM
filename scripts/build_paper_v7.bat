@echo off
REM build_paper_v7.bat - Build the IAKM v7 paper (IEEE conference format)
REM
REM IMPORTANT: paper_v7\IAKM_PAPER_V7_IEEE.tex is the hand-maintained source
REM of record for the PDF. It is tuned by hand against
REM paper_v7\IAKM_V7_FLOAT_PLACEMENT.md (float environments, caption sides,
REM in-text callouts). Do NOT regenerate it from the markdown draft; the
REM converter would discard that placement work.
REM
REM The markdown draft (IAKM_PAPER_V7_DRAFT.md) is the prose source. When
REM prose changes, port the change into the .tex by hand.
setlocal

set "MIKTEX_BIN=%LOCALAPPDATA%\Programs\MiKTeX\miktex\bin\x64"
set "PATH=%MIKTEX_BIN%;%PATH%"
cd /d "%~dp0.."

set "TEX=paper_v7\IAKM_PAPER_V7_IEEE.tex"
set "BUILT=paper_v7\IAKM_PAPER_V7_IEEE.pdf"
set "PUBLIC=paper_v7\IAKM_Public.pdf"

echo === IAKM v7: IEEE conference ===

if not exist "%TEX%" (
    echo [ERROR] Not found: %TEX%
    exit /b 1
)

call "%~dp0compile_tex.bat" "%TEX%"
if %ERRORLEVEL% NEQ 0 exit /b 1

REM Publish under the distribution name used for release/DOI.
copy /y "%BUILT%" "%PUBLIC%" >nul
if %ERRORLEVEL% NEQ 0 (
    echo [ERROR] Could not write %PUBLIC%
    exit /b 1
)

echo [OK] %PUBLIC%
endlocal
