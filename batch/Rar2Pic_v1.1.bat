@ECHO OFF&TITLE 藏图制作脚本v1.1 CodeBy:Sylthas
MODE con COLS=55 LINES=25
color 0A
:loop
cls
echo.藏图制作脚本 For 福利吧http://fuliba.net CodeBy:Sylthas 
echo.
echo.Hi! %username%! Now is %date% %time%
echo.欢迎使用藏图制作脚本,本脚本可以将rar文件隐藏到图片里.
echo.
echo.①请拖入图像文件后回车：
set /p imagefile=
echo.②请拖入rar文件后回车：
set /p rarfile=
echo.
copy /b %imagefile% + %rarfile% %rarfile%_new.jpg
echo.
if errorlevel 1 goto errorinfo
echo.藏图%rarfile%_new.jpg已经生成
echo.使用时请将%rarfile%_new.jpg更名为xx.rar即可打开
echo.
goto choice
:errorinfo
echo.发生错误,藏图生成失败.
echo.
:choice
set /p key=是否继续？Q键退出:
if /i "%key%" =="q" goto quit
goto loop
:quit
exit