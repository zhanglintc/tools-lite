@echo off
setlocal enabledelayedexpansion

set /a cnt=1
set /a max=1

echo 本程序能显示所有被隐藏的文件和文件夹.
echo=
echo 请把该文件放在移动硬盘根目录下再操作,
echo 如果已在根目录下，请任意键继续，否则请关闭...
pause>nul

cls
dir /b /a:d > log.dat

for /f %%i in (log.dat) do (
set /a cnt=!cnt!+1
)
set /a max=%cnt%
set /a cnt=1

for /f %%i in (log.dat) do (
cls
echo 当前处理进度： !cnt!/!max!
echo 当前处理文件夹：%%i
echo=
echo=
echo 处理中，请稍等...
attrib /d /s -a -r -s -h %%i
set /a cnt=!cnt!+1
)
del log.dat

cls
echo 处理完成，任意键退出...
pause>nul