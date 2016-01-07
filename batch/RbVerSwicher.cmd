@echo off

title Powered by Lane @ZDS
color 3e

echo ***************************************************
echo Default Ruby1.9 address: C:\Ruby193
echo Default Ruby2.1 address: C:\Ruby21
echo ***************************************************
echo.
echo If you installed other version of Ruby
echo or you installed Ruby in the other place,
echo please modify the address by yourself.
echo.
echo If any problem occured, plase use "*.bak" file
echo to recover your original "Path" setting.
echo.

::Get Path and save to %envPath%
set envPath=%path%

::Use %envPathBak% to store current environment path and save to backup file
set envPathBak=%path%

::Remove "C:\Ruby193\bin\;" and "C:\Ruby193\bin;"
set envPath=%envPath:C:\Ruby193\bin\;=%
set envPath=%envPath:C:\Ruby193\bin;=%

::Remove "C:\Ruby21\bin\;" and "C:\Ruby21\bin;"
set envPath=%envPath:C:\Ruby21\bin\;=%
set envPath=%envPath:C:\Ruby21\bin;=%

echo Current Ruby version:
echo ---------------
ruby -v
echo ---------------
echo.
echo Which Ruby version do you want to set:
choice /c 12c
:: choose 2, errorlevel 1
:: choose 3, errorlevel 2
:: judge big number first
if errorlevel 3 goto end
if errorlevel 2 goto Ruby21
if errorlevel 1 goto Ruby193

:Ruby193
::Add "C:\Ruby19\;" in the very start of %envPath%
set envPath=C:\Ruby193\bin;%envPath%
set pyVer=Ruby193
goto SetPath

:Ruby21
::Add "C:\Ruby21\;" in the very start of %envPath%
set envPath=C:\Ruby21\bin;%envPath%
set pyVer=Ruby21
goto SetPath



:SetPath
::useless source
::wmic ENVIRONMENT where "name='Path' and username='<system>'" set VariableValue="%envPath%"
:: Set "Path"
setx path "%envPath%" -m

::Make a backup(%envPathBak% won't be modified)
set curTime=%time%
set fileName=%curTime::=.%.bak
echo Backup of your "Path" at %date% %curTime%:>%fileName%
echo.>>%fileName%
echo %envPathBak%>>%fileName%
goto end

:end
cls
if "%pyVer%"=="" (echo Cancelled...) else (echo Convert Python version to %pyVer% successful.)
echo.
echo Press any key to close...
pause>nul


