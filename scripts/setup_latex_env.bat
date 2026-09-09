@echo off
REM setup_latex_env.bat - Add MiKTeX to PATH and verify LaTeX environment
REM Run this once per terminal session, or add the PATH line to your system environment.

echo === LaTeX Environment Setup ===

REM Add MiKTeX to PATH for this session
set "MIKTEX_BIN=%LOCALAPPDATA%\Programs\MiKTeX\miktex\bin\x64"
if not exist "%MIKTEX_BIN%\pdflatex.exe" (
    echo ERROR: MiKTeX not found at %MIKTEX_BIN%
    echo Please install MiKTeX from https://miktex.org/download
    exit /b 1
)

set "PATH=%MIKTEX_BIN%;%PATH%"
echo MiKTeX added to PATH: %MIKTEX_BIN%

REM Verify tools
echo.
echo Checking tools:
where pdflatex >nul 2>&1 && echo   [OK] pdflatex || echo   [MISSING] pdflatex
where bibtex >nul 2>&1 && echo   [OK] bibtex || echo   [MISSING] bibtex
where python >nul 2>&1 && echo   [OK] python || echo   [MISSING] python

REM Set MiKTeX to auto-install packages
echo.
echo Setting MiKTeX to auto-install missing packages...
initexmf --set-config-value=[MPM]AutoInstall=1 2>nul
if %ERRORLEVEL% EQU 0 (
    echo   [OK] Auto-install enabled
) else (
    echo   [WARN] Could not set auto-install. Set it manually in MiKTeX Console.
)

echo.
echo === Setup complete. You can now run the build scripts. ===
