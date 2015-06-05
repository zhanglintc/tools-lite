@echo off

color 3e

setlocal enabledelayedexpansion

@echo off
if not defined flg set flg= && start /min "" %0& exit

set /a IP=1
::IP address
set /a cnt=1
::count the unable pinged numbers

echo “ú•tF%date%>>IPlog.txt
echo ŽžF%time%>>IPlog.txt
echo=>>IPlog.txt

:loop
echo Pinging: 192.168.39.%IP%
ping -n 1 192.168.39.%IP%|findstr "‚Å‚«‚Ü‚¹‚ñ"&&(
echo No%cnt%¨192.168.39.%IP%>>IPlog.txt
set /a cnt=!cnt!+1
)
set /a IP=%IP%+1
if %IP% LEQ 255 goto loop
set /a cnt=%cnt%-1
echo=>>IPlog.txt
echo %cnt%‘äping‚Å‚«‚È‚¢>>IPlog.txt
echo Žž:%time%>>IPlog.txt
echo=-------------------------------------->>IPlog.txt
echo=-------------------------------------->>IPlog.txt
echo=>>IPlog.txt
echo=>>IPlog.txt
IPlog.txt
exit