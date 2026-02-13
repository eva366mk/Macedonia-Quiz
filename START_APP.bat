@echo off
REM Macedonia Quiz Master Launcher
REM This batch file starts the Streamlit app automatically

echo.
echo ========================================
echo   Macedonia Quiz Master
echo ========================================
echo.
echo Starting the app...
echo.

cd /d "%~dp0"

REM Check if virtual environment exists
if not exist ".venv" (
    echo Error: Virtual environment not found!
    echo Please run setup first.
    pause
    exit /b 1
)

REM Launch Streamlit
.\.venv\Scripts\python.exe -m streamlit run Home.py --logger.level=error

pause
