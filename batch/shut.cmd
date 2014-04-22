@echo off
title Lane at NEU
COLOR 3E

set t=1
for /f "tokens=3" %%i in ('reg query "HKCU\Control Panel\International" /v "sLanguage"') do (
    set reg_localevar=%%i
)

if %reg_localevar% == CHS goto Chinese
goto English

:Chinese
echo -------------------------------------------------------------------------------
echo 此为作者无聊闲暇之余做的自动关机程序,可以方便大家做一些事。
echo 比如晚上放歌30分钟伴你入眠然后自动关机之类的。^^_^^呵呵。
echo -------------------------------------------------------------------------------
echo 由于作者初次接触，技艺不够高超，难免有些bug，敬请谅解！
echo 注意：必须输入数字（1~315360000）。输入字母等效于输入了0~~
echo -------------------------------------------------------------------------------
echo 输入数字 0 可以取消当前关机计划并退出程序。(没有计划则直接退出)
echo -------------------------------------------------------------------------------
set /p time=请输入关机倒计时时间（单位：min)：
set /a s=time*60
if "%s%"=="0" (shutdown -a&cls&echo.&echo 取消成功，谢谢使用！&&echo.&goto end1)
shutdown -a
ping -n 2 127.1>nul
shutdown -s -t "%s%"
echo -------------------------------------------------------------------------------
echo 您的计算机将于%time%分钟后关闭...
echo -------------------------------------------------------------------------------
cls
echo -------------------------------------------------------------------------------
echo 若要此时取消自动关机请输入0，然后回车，关闭程序请直接按回车键！
echo (程序关闭后倒计时继续将继续运行...)
echo -------------------------------------------------------------------------------
echo.
set /p t=
echo.
cls
if "%t%"=="0" (shutdown -a && echo. && echo 取消成功,谢谢使用！)
goto end1

:English
echo -------------------------------------------------------------------------------
echo This app was created in author's leisure time, could make something easier.
echo For example after 30 minutes music then shut down your PC, ^^_^^.
echo -------------------------------------------------------------------------------
echo It is the first time author writes a batch file, there may be several bugs.
echo Note: should input numbers (1~315360000). Charecters input means 0 ~~
echo -------------------------------------------------------------------------------
echo Input number 0 can cancel the current shut down plan.
echo -------------------------------------------------------------------------------
set /p time=Input time (Unit: min):
set /a s=time*60
if "%s%"=="0" (shutdown -a&cls&echo.&echo Cancelled successfully, thank you!&&echo.&goto end1)
shutdown -a
ping -n 2 127.1 > nul
shutdown -s -t "%s%"
echo -------------------------------------------------------------------------------
echo Your PC will be shouted down in %time% mins...
echo -------------------------------------------------------------------------------
cls
echo -------------------------------------------------------------------------------
echo If you want to cancel, please input 0, otherwise input Enter instead!
echo (Shut down countdown will continue after close...)
echo -------------------------------------------------------------------------------
echo.
set /p t=
echo.
cls
if "%t%"=="0" (shutdown -a && echo. && echo Cancelled successfully, thank you!)


:end1
echo -------------------------------------------------------------------------------
echo.
echo                                                     Powered by Lane at NEU
echo.
echo -------------------------------------------------------------------------------
if "%t%"=="1" goto end2
if not "%t%"=="0" echo Thank you!!
:end2
echo Press any key to quit...
echo.
pause>nul