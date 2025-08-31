@echo off
for %%a in (*.rar) do (
    mkdir "%%~na"
    "C:\Program Files\WinRAR\WinRAR.exe" x -y "%%a" "%%~na\"
)

pause