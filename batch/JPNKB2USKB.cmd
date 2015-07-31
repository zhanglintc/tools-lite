@echo off
title Powered by Lane at ZDS
color 3E

reg add "HKLM\SYSTEM\CurrentControlSet\Control\Keyboard Layouts\00000411" /v "Layout File" /t REG_SZ /d "KBDUS.DLL" /f > nul

echo Set 0411(Japanese) to KBDUS.DLL(US keyboard) successfull.
echo Please restart your computer to make this change take effect.
echo.
echo Press any to close...
pause > nul


