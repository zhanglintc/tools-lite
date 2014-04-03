::Original useing to count file's lines in one tasuku
::(that's why it is named as tasuku)
::Now could use to count file's lines in one folder

@echo off
setlocal enabledelayedexpansion
title タスク カウント ツール by Lane
color 3E

set /a input_path=initial
set file_suffix=*.c *.cpp *.h

echo Drag your folder here and then push ENTER button:
set /p input_path=

if %input_path%==initial goto end

set driver=%input_path:~0,2%
%driver%
cd %input_path%
echo %input_path%>log.c

set /a line_count=1
set /a file_count=1
set /a percent=1
set /a completed=1

dir /b /s %input_path%\%file_suffix%>tmp.dat

for /f %%i in (tmp.dat) do set /a file_count=!file_count!+1
set /a file_count=%file_count%-1
cls
echo There are %file_count% files found
echo=
echo Press any key to count the lines...
pause>nul
cls

for /f "usebackq delims=" %%i in (tmp.dat) do (
for /f "usebackq delims=" %%z in (%%i) do (
set /a line_count=!line_count!+1
)
cls
echo 処理進度：!completed!/%file_count%
echo 総行数:!line_count!
echo %%i
set /a completed=!completed!+1
)

del tmp.dat

echo 有効行数は:!line_count!行ぐらい>>log.c
echo=>>log.c

pause>nul

::echo the valid lines number

::echo ここから:>>log.c
::findstr /i "#" %input_path%>>log.c
echo 以上です!>>log.c
::find the lines with # and output to the log.c

start log.c
::open the result file

%input_path%
::open the original file

:end