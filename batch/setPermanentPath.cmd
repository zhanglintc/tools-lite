@echo off
::Refer to http://www.java123.net/v/549062.html (useless)

title Powered by Lane @ZDS
color 3e

echo ***************************************************
echo Default Python2 address: C:\Python27
echo Default Python3 address: C:\Python33
echo ***************************************************
echo.
echo If you installed other version of Python
echo or you installed Python in the other place
echo please modify the code by your self.
echo.

::useless source
::for /f "usebackq delims=" %%i in (`wmic ENVIRONMENT where "name='Path'" get VariableValue`) do (
::    echo %%i|findstr "bin">nul && set envPath=%%i
::)
::Get Path and save to %envPath%
set envPath=%path%

::Make a backup
set curTime=%time%
set fileName=%curTime::=.%.bak
echo Backup of your "Path" at %date% %curTime%:>%fileName%
echo.>>%fileName%
echo %envPath%>>%fileName%

::Remove "C:\Python27\;" and "C:\Python27;"
set envPath=%envPath:C:\Python27\;=%
set envPath=%envPath:C:\Python27;=%

::Remove "C:\Python33\;" and "C:\Python33;"
set envPath=%envPath:C:\Python33\;=%
set envPath=%envPath:C:\Python33;=%

echo Which Python version do you want to set:
choice /c 23
:: choose 2, errorlevel 1
:: choose 3, errorlevel 2
:: judge big number first
if errorlevel 2 goto Python3
if errorlevel 1 goto Python2

:Python2
::Add "C:\Python27\;" in the very start of %envPath%
set envPath=C:\Python27;%envPath%
set pyVer=Python2
goto SetPath

:Python3
::Add "C:\Python27\;" in the very start of %envPath%
set envPath=C:\Python33;%envPath%
set pyVer=Python3
goto SetPath



:SetPath
::useless source
::wmic ENVIRONMENT where "name='Path' and username='<system>'" set VariableValue="%envPath%"
:: Set "Path"
setx path "%envPath%" -m

goto end

:end
cls
echo Convert Python version to %pyVer% successful.
echo.
echo Press any key to close...
pause>nul


