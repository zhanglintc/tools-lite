@echo off
set var=%cd%
md BingImg&cd BingImg
for /l %%i in (0,1,30) do %var%\wget http://area.sinaapp.com/bingImg?daysAgo=%%i