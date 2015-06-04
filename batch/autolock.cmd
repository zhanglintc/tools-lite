@echo off

REM set the file path here
echo Drag target file here:
set /p file=

REM first update the file and then get lock
REM || means if failed to find "locked" then goto delay
:loop
svn update "%file%"
svn lock "%file%" | find "locked" || goto delay
goto end

:delay
ping 127.0.0.1 -n 4 > nul
goto loop

:end
REM if loop finished then start the file
REM this command could get optimize
start %file%