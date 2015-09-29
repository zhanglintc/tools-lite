@echo off
::Refer to http://www.java123.net/v/549062.html

title Powered by Lane @ZDS
color 3e

::Get Path and save to %envPath%
for /f "usebackq delims=" %%i in (`wmic environment where "name='Path'" get VariableValue`) do (
    echo %%i|findstr "bin">nul && set envPath=%%i
)

::Remove "C:\Python27\;"
set envPath=%envPath:C:\Python27\;=%

::Remove "C:\Python33\;"
set envPath=%envPath:C:\Python33\;=%

::Add "C:\Python27\;" in the very start of %envPath%
set envPath=C:\Python27\;%envPath%

echo %envPath%

echo.
echo Press any key to close...
pause>nul


