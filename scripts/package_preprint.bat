@echo off
REM package_preprint.bat - Build the Preprints.org submission archive.
REM
REM Preprints.org requires LaTeX submissions as an archive containing every
REM file needed to recreate the PDF. This packages the .tex, the MDPI class
REM files in Definitions\, the figures, and the built PDF.
REM
REM There is no .bib file: the bibliography is inline (thebibliography), so
REM the .tex is self-contained for references.
REM
REM Output: preprint\IAKM_Preprints_submission.zip
setlocal

cd /d "%~dp0.."

set "OUT=preprint\IAKM_Preprints_submission.zip"

if not exist "preprint\IAKM_Preprints.tex" (
    echo [ERROR] preprint\IAKM_Preprints.tex not found
    exit /b 1
)

if not exist "preprint\IAKM_Preprints.pdf" (
    echo [WARN] preprint\IAKM_Preprints.pdf not present.
    echo        Run scripts\build_preprint.bat first so the archive carries the PDF.
)

if exist "%OUT%" del /q "%OUT%"

powershell -NoProfile -Command ^
  "$items = Get-ChildItem -Path 'preprint' -Exclude '*.zip','README.md','*.aux','*.log','*.out','*.synctex.gz','*.spl','*.bbl','*.blg','*.toc','*.loe';" ^
  "Compress-Archive -Path $items -DestinationPath '%OUT%' -Force"

if not exist "%OUT%" (
    echo [ERROR] Archive was not created.
    exit /b 1
)

echo [OK] %OUT%
powershell -NoProfile -Command ^
  "Add-Type -AssemblyName System.IO.Compression.FileSystem;" ^
  "$z = [System.IO.Compression.ZipFile]::OpenRead((Resolve-Path '%OUT%'));" ^
  "$z.Entries | ForEach-Object { '{0,10}  {1}' -f $_.Length, $_.FullName };" ^
  "$z.Dispose()"

endlocal
