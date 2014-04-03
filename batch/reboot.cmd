::restart windows explorer easily

@echo off
color 3e
title Reboot Lite
taskkill /f /im explorer.exe
start explorer.exe
cls
echo Restart successfully !!!
echo Press any key to close...
pause>nul