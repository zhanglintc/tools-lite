@echo off
title Powered by Lane @ZDS
color 3e

set /p username=enter VSS username: 
set /p password=enter VSS password: 
setx SSUSER "%username%" -m
setx SSPWD "%password%" -m

echo.
echo.
echo VSS username and password saved, press any key to close...
pause>nul



