@echo off
REM Setup Macedonia Quiz Master
REM Run this once to install dependencies

echo.
echo ========================================
echo   Macedonia Quiz Master - Setup
echo ========================================
echo.

cd /d "%~dp0"

echo Checking Python installation...
python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python not found! Please install Python 3.8+
    echo Download from: https://www.python.org/downloads/
    pause
    exit /b 1
)

echo.
echo Creating virtual environment...
python -m venv .venv

echo.
echo Activating virtual environment...
call .\.venv\Scripts\activate.bat

echo.
echo Installing dependencies...
pip install -q -r requirements.txt

echo.
echo ========================================
echo   Setup Complete!
echo ========================================
echo.
echo You can now run the app by double-clicking START_APP.bat
echo.
pause
