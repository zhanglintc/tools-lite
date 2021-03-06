@echo off

title Powered by Lane @ZDS
color 3e

for /d %%i in (*) do (
    title Updating...  %%~fi

    cd %%~fi

    echo Updating: %%~fi
    echo ==================
    echo Cleaning...
    svn cleanup
    svn update
    echo ==================
    echo.
    echo.

    cd ..
)

title Completed...  Powered by Lane @ZDS

echo.
echo Press any key to close...
pause > nul

REM copy updateSVN itself to current path
if exist .\tools-lite (xcopy .\tools-lite\trunk\batch\updateSVN.cmd . /c /f /i /y > nul)