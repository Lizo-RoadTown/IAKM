@echo off
REM compile_tex.bat - Compile a .tex file to PDF with proper passes
REM Usage: compile_tex.bat path\to\filename.tex
REM Runs pdflatex twice (for references/TOC) and cleans build artifacts after.
REM The .tex may live in a subfolder (e.g. papers\); this script compiles from
REM the .tex's own directory so the PDF lands beside the source and relative
REM figure paths (e.g. ..\figures\) resolve correctly.

setlocal

if "%~1"=="" (
    echo Usage: compile_tex.bat path\to\filename.tex
    exit /b 1
)

if not exist "%~1" (
    echo ERROR: File not found: %~1
    exit /b 1
)

set "TEXDIR=%~dp1"
set "TEXNAME=%~nx1"
set "BASENAME=%~n1"
set "MIKTEX_BIN=%LOCALAPPDATA%\Programs\MiKTeX\miktex\bin\x64"
set "PATH=%MIKTEX_BIN%;%PATH%"

REM Compile from the .tex's own directory
pushd "%TEXDIR%"

echo === Compiling %TEXNAME% (in %TEXDIR%) ===

echo [1/2] First pass...
pdflatex -interaction=nonstopmode "%TEXNAME%" >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo [ERROR] First pass failed. Check %BASENAME%.log for details.
    pdflatex -interaction=nonstopmode "%TEXNAME%"
    popd
    exit /b 1
)

echo [2/2] Second pass (resolving references)...
pdflatex -interaction=nonstopmode "%TEXNAME%" >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo [ERROR] Second pass failed. Check %BASENAME%.log for details.
    popd
    exit /b 1
)

echo.
echo [OK] Output: %TEXDIR%%BASENAME%.pdf

REM Clean build artifacts
del /q "%BASENAME%.aux" 2>nul
del /q "%BASENAME%.log" 2>nul
del /q "%BASENAME%.out" 2>nul
del /q "%BASENAME%.synctex.gz" 2>nul
del /q "%BASENAME%.spl" 2>nul
del /q "%BASENAME%.bbl" 2>nul
del /q "%BASENAME%.blg" 2>nul
del /q "%BASENAME%.toc" 2>nul
echo [OK] Build artifacts cleaned.

popd
endlocal
