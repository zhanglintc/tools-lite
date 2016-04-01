@echo off
title Powered by Lane @ZDS
color 3E
echo -------------------------------------------------------------------------------
echo Intro: This tool helps to chang your Logon image,
echo        drag any JPEG file here to use.
echo.
echo Note: Image file should be smaller than 200kb. Set NULL to use default image.
echo -------------------------------------------------------------------------------
echo.

set target=NULL
set /p target=Drag JPEG file here: 
if %target%==NULL goto del

:add
del C:\Windows\System32\oobe\info\backgrounds\*.jpg > nul
xcopy /y %target% C:\Windows\System32\oobe\info\backgrounds\ > nul
rename C:\Windows\System32\oobe\info\backgrounds\*.jpg BackgroundDefault.jpg
reg add HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Authentication\LogonUI\Background /v OEMBackground /t REG_DWORD /d 00000001 /f > nul
echo Set Logon image success...
goto end

:del
reg add HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Authentication\LogonUI\Background /v OEMBackground /t REG_DWORD /d 00000000 /f > nul
echo Delete Logon image success...
goto end

:end
echo.
echo Press any key to continue...
pause > nul
