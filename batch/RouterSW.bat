@echo off
Title Linn 的路由选择器
Color 3E
echo -------------------------------------------------------------------------------
echo     此工具可以帮助你选择上网时的路由，可以是网通网，也可以是校园网，还可以
echo     两个一起上网，当然得自己插好网线……剩下的就是本工具的事儿了。
echo.
echo				@ 输入1，使用您的网通网上网~~
echo				@ 输入2，使用您的校园网上网~~
echo				@ 输入3，使用双网卡同时上网~~
echo				@ 输入4，查看当前的ipv4路由情况~~
echo -------------------------------------------------------------------------------
set /p ch=请输入你的选择:
set /a choice=ch
if "%choice%"=="1" (goto ch1)
if "%choice%"=="2" (goto ch2)
if "%choice%"=="3" (goto ch3)
if "%choice%"=="4" (goto ch4)
if "%choice%"=="0" (echo did nothing && goto end)
goto end

:ch1
route delete 0.0.0.0 mask 0.0.0.0
route add 0.0.0.0 mask 0.0.0.0 192.168.1.1 metric 1
route add 0.0.0.0 mask 0.0.0.0 192.168.1.253 metric 2
route delete 202.118.0.0 mask 255.255.0.0 58.154.234.254
route delete 219.216.0.0 mask 255.255.0.0 58.154.234.254
route delete 202.199.0.0 mask 255.255.0.0 58.154.234.254
route delete 58.154.0.0 mask 255.255.0.0 58.154.234.254
route delete 118.202.0.0 mask 255.255.0.0 58.154.234.254
cls
goto end

:ch2
route delete 0.0.0.0 mask 0.0.0.0
route add 0.0.0.0 mask 0.0.0.0 58.154.234.254 metric 1
route delete 202.118.0.0 mask 255.255.0.0 58.154.234.254
route delete 219.216.0.0 mask 255.255.0.0 58.154.234.254
route delete 202.199.0.0 mask 255.255.0.0 58.154.234.254
route delete 58.154.0.0 mask 255.255.0.0 58.154.234.254
route delete 118.202.0.0 mask 255.255.0.0 58.154.234.254
cls
goto end

:ch3
route delete 0.0.0.0 mask 0.0.0.0
route add 0.0.0.0 mask 0.0.0.0 192.168.1.1 metric 1
route add 0.0.0.0 mask 0.0.0.0 192.168.1.253 metric 2
route add 0.0.0.0 mask 0.0.0.0 58.154.234.254 metric 100
route add 202.118.0.0 mask 255.255.0.0 58.154.234.254
route add 219.216.0.0 mask 255.255.0.0 58.154.234.254
route add 202.199.0.0 mask 255.255.0.0 58.154.234.254
route add 58.154.0.0 mask 255.255.0.0 58.154.234.254
route add 118.202.0.0 mask 255.255.0.0 58.154.234.254
cls
goto end

:ch4
cls
route print -4
pause
exit

:end
echo -------------------------------------------------------------------------------
echo.
echo    操作成功！！！
echo.
echo                                                     Powered by Linn at NEU
echo.
echo -------------------------------------------------------------------------------
echo 请按任意键退出程序...
echo.
pause>nul
