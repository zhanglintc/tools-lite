@echo off

REM set the file path here
set file=lottery.pl

REM first update the file and then get lock
REM || means if failed to find "locked" then goto loop
:loop
ping 127.0.0.1 > nul
svn update %file%
svn lock %file% | find "locked" || goto loop

REM if loop finished then start the file
start %file%