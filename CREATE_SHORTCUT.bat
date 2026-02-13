@REM Create shortcut for Macedonia Quiz Master
@echo off

REM Create VBScript to generate shortcut
setlocal enabledelayedexpansion

set "shortcut_path=%USERPROFILE%\Desktop\Macedonia Quiz Master.lnk"
set "app_path=%cd%\START_APP.bat"
set "icon_path=%cd%\Home.py"

REM Create the shortcut using Windows API
powershell -Command ^
$WshShell = New-Object -ComObject WScript.Shell; ^
$Shortcut = $WshShell.CreateShortcut('%shortcut_path%'); ^
$Shortcut.TargetPath = '%app_path%'; ^
$Shortcut.WorkingDirectory = '%cd%'; ^
$Shortcut.Description = 'Macedonia Quiz Master - Test your knowledge!'; ^
$Shortcut.IconLocation = 'C:\Windows\System32\imageres.dll,100'; ^
$Shortcut.Save()

echo Shortcut created on Desktop: "Macedonia Quiz Master.lnk"
pause
