@echo off
reg add HKLM\\SOFTWARE\\Microsoft\\WindowsUpdate\\UX\\Settings /v FlightSettingsMaxPauseDays /t REG_DWORD /d 7152 /f>nul
reg add HKLM\\SOFTWARE\\Microsoft\\WindowsUpdate\\UX\\Settings /v PauseFeatureUpdatesStartTime /t REG_SZ /d 2024-01-01T10:00:52Z /f>nul
reg add HKLM\\SOFTWARE\\Microsoft\\WindowsUpdate\\UX\\Settings /v PauseFeatureUpdatesEndTime /t REG_SZ /d 2999-01-01T10:00:52Z /f>nul
reg add HKLM\\SOFTWARE\\Microsoft\\WindowsUpdate\\UX\\Settings /v PauseQualityUpdatesStartTime /t REG_SZ /d 2024-01-01T10:00:52Z /f>nul
reg add HKLM\\SOFTWARE\\Microsoft\\WindowsUpdate\\UX\\Settings /v PauseQualityUpdatesEndTime /t REG_SZ /d 2999-01-01T10:00:52Z /f>nul
reg add HKLM\\SOFTWARE\\Microsoft\\WindowsUpdate\\UX\\Settings /v PauseUpdatesStartTime /t REG_SZ /d 2024-01-01T10:00:52Z /f>nul
reg add HKLM\\SOFTWARE\\Microsoft\\WindowsUpdate\\UX\\Settings /v PauseUpdatesExpiryTime /t REG_SZ /d 2999-01-01T10:00:52Z /f>nul
exit