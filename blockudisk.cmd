@echo off
reg add HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows\\RemovableStorageDevices /v Deny_All /t REG_DWORD /d 1 /f>nul
reg add HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows\\RemovableStorageDevices\\{53f5630d-b6bf-11d0-94f2-00a0c91efb8b} /v Deny_Execute /t REG_DWORD /d 1 /f>nul
reg add HKLM\SOFTWARE\Policies\Microsoft\Windows\RemovableStorageDevices\{53f5630d-b6bf-11d0-94f2-00a0c91efb8b} /v Deny_Read /t REG_DWORD /d 1 /f>nul
reg add HKLM\SOFTWARE\Policies\Microsoft\Windows\RemovableStorageDevices\{53f5630d-b6bf-11d0-94f2-00a0c91efb8b} /v Deny_Write /t REG_DWORD /d 1 /f>nul
gpupdate /force >nul
if %errorlevel% equ 0 (
echo success
) else (
echo failed
)
exit