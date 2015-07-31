@echo off
title Powered by Lane at ZDS
color 3E

echo Current setting:
echo ==================================
reg query "HKLM\SYSTEM\CurrentControlSet\Control\Keyboard Layouts\00000411"
echo ==================================
echo.

:loop
set op=null
set /p op=Are you sure to change "Layout File" to "KBDUS.DLL"? [Y/N]
if %op%==Y goto set
if %op%==y goto set
if %op%==N goto cancel
if %op%==n goto cancel
goto loop

:set
reg add "HKLM\SYSTEM\CurrentControlSet\Control\Keyboard Layouts\00000411" /v "Layout File" /t REG_SZ /d "KBDUS.DLL" /f > nul
echo.
echo Set 0411(JPN) "Layout File" to "KBDUS.DLL"(US keyboard) successfull.
echo Please restart your computer to make this change take effect.
goto end

:cancel
echo.
echo You haven't changed anything.

:end
echo.
echo Press any to close...
pause > nul


