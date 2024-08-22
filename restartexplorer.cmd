@echo off
taskkill /im explorer.exe /f >nul
start /HIGH explorer.exe >nul
if %errorlevel% equ 0 (
echo success
) else (
echo failed
)
exit