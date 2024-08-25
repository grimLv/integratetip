@echo off
ping 172.16.2.6 -n 3 >nul
if %errorlevel% neq 0 (
    echo "network connect error"
    exit
)
net use \\172.16.2.6\ipc$ data@2022 /user:web >nul
start \\172.16.2.6\file\2022¼ÆËã»úÌ¨ÕË.xlsx >nul
exit