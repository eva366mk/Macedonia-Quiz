@echo off
title Macedonia Quiz Master
color 0A

cd /d "%~dp0"

if not exist ".venv" (
    echo.
    echo ERROR: Setup not completed!
    echo.
    echo Please double-click SETUP.bat first
    echo.
    pause
    exit /b 1
)

cls
echo.
echo ================================================
echo   Macedonia Quiz Master 
echo ================================================
echo.
echo Starting application...
echo.

.\.venv\Scripts\python.exe launcher.py

pause
