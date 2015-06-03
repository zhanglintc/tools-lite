@echo off
echo Drag image here or copy to this folder:
echo (image file shoud smaller than 200kb)
echo (not set means clean)
echo.

set target=NULL
set /p target=
if %target%==NULL goto del

:add
del C:\Windows\System32\oobe\info\backgrounds\*.jpg
xcopy /y %target% C:\Windows\System32\oobe\info\backgrounds\
rename C:\Windows\System32\oobe\info\backgrounds\*.jpg BackgroundDefault.jpg
_add.reg
goto end

:del
_del.reg
goto end

:end
echo.
echo Completed, press any key to continue...
pause > nul
