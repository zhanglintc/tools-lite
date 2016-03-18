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
    
    if "%%~xi"==".ex_" (
        expand %%i .\expanded\%%~ni.exe
    )
    
    if "%%~xi"==".pp_" (
        expand %%i .\expanded\%%~ni.ppd
    )
    
    if "%%~xi"==".gp_" (
        expand %%i .\expanded\%%~ni.gpd
    )
    
    if "%%~xi"==".kv_" (
        expand %%i .\expanded\%%~ni.kvd
    )
    
    if "%%~xi"==".xm_" (
        expand %%i .\expanded\%%~ni.xml
    )
    
    if "%%~xi"==".confi_" (
        expand %%i .\expanded\%%~ni.config
    )
    
    if "%%~xi"==".manifes_" (
        expand %%i .\expanded\%%~ni.manifest
    )
)

echo=
echo Press any key to close...
pause>nul