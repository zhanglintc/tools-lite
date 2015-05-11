@echo off
set var=%cd%
set target="C:\Users\zdsoft\AppData\Roaming\Microsoft\Windows\Themes"
md BingImg&cd BingImg
rm *.*
%var%\wget http://area.sinaapp.com/bingImg?daysAgo=
rename *.jpg today.jpg
xcopy /y today.jpg %target%\
pause
rm %target%\TranscodedWallpaper.jpg
pause
rename %target%\today.jpg TranscodedWallpaper.jpg
pause
RunDll32.exe USER32.DLL,UpdatePerUserSystemParameters
pause