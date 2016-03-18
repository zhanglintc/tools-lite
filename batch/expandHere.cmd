@echo off
setlocal enabledelayedexpansion

title Powered by Lane @ZDS
color 3e

mkdir expanded
for %%i in (*) do (
    if "%%~xi"==".ch_" (
        expand %%i .\expanded\%%~ni.chm
    )
    
    if "%%~xi"==".dl_" (
        expand %%i .\expanded\%%~ni.dll
    )
    
    if "%%~xi"==".in_" (
        expand %%i .\expanded\%%~ni.ini
    )
    
    if "%%~xi"==".km_" (
        expand %%i .\expanded\%%~ni.kmp
    )
    
    if "%%~xi"==".kp_" (
        expand %%i .\expanded\%%~ni.kpd
    )
)

echo=
echo Press any key to close...
pause>nul