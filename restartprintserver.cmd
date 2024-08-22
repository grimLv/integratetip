@echo off
sc stop spooler >nul
timeout /t 2 /nobreak
sc start spooler >nul
if %errorlevel% equ 0 (
echo success
) else (
echo failed
)
exit