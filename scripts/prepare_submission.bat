@echo off
REM prepare_submission.bat - Assemble everything Preprints.org needs, in one folder.
REM
REM Rebuilds the PDF, the graphical abstract, and the source archive first, so
REM the folder can never carry a stale manuscript. Output: submission\
REM
REM The folder's contents are derived from tracked sources and are gitignored;
REM rerun this script to recreate them.
setlocal

cd /d "%~dp0.."

set "OUT=submission"

echo === Preparing Preprints.org submission ===

echo [1/4] Rebuilding manuscript...
call "%~dp0build_preprint.bat" >nul
if %ERRORLEVEL% NEQ 0 (
    echo [ERROR] Manuscript build failed. If the PDF is open in a viewer, close it.
    exit /b 1
)

echo [2/4] Regenerating graphical abstract...
python "%~dp0generate_graphical_abstract.py" >nul
if %ERRORLEVEL% NEQ 0 (
    echo [ERROR] Graphical abstract generation failed.
    exit /b 1
)

echo [3/4] Rebuilding source archive...
call "%~dp0package_preprint.bat" >nul
if %ERRORLEVEL% NEQ 0 (
    echo [ERROR] Archive build failed.
    exit /b 1
)

echo [4/4] Assembling...
if exist "%OUT%" rmdir /s /q "%OUT%"
mkdir "%OUT%"

copy /y "preprint\IAKM_Preprints.pdf"            "%OUT%\1_manuscript.pdf" >nul
copy /y "preprint\IAKM_Preprints_submission.zip" "%OUT%\2_latex_source.zip" >nul
copy /y "preprint\graphical_abstract.png"        "%OUT%\3_graphical_abstract.png" >nul

REM The README is written by the POSIX script; regenerate it here too via bash
REM if available, otherwise point at the checklist.
where bash >nul 2>&1
if %ERRORLEVEL% EQU 0 (
    bash -c "sed -n '/^PREPRINTS.ORG SUBMISSION/,$p' scripts/prepare_submission.sh | sed '$d' > %OUT%/README.txt" 2>nul
)
if not exist "%OUT%\README.txt" (
    echo See preprint\README.md for the submission checklist. > "%OUT%\README.txt"
)

echo.
echo === %OUT%\ ===
dir /b "%OUT%"

endlocal
