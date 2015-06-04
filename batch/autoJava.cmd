@echo off
REM Compile given JAVA file and then run it.
title Powered by Lane at ZDS
color 3e

REM if no given parameter, set %target%
REM else compile parameter file
if not "%~1"=="" goto with_para else goto no_para

:no_para
cls
echo Drag JAVA file here:
set /p target=
REM command below is calling self with para
%0 %target%
goto end

:with_para
cls
REM change directory
pushd %~dp1
echo Compiling...
REM compile file
javac "%~f1"
cls
echo Running...
echo.
REM run file
java "%~n1"
REM clean directory
del /q *.class
echo.
echo Press any key to close...
pause>nul

:end
exit