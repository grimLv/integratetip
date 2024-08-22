@echo off
reg delete HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows\\RemovableStorageDevices /f >nul
gpupdate /force>nul
if %errorlevel% equ 0 (
echo success
) else (
echo failed
)
exit