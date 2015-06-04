@echo off

title Powered by Lane at ZDS
color 3e

for /d %%i in (*) do (
    cd %%~fi

    echo Updating: %%~fi
    echo ==================
    svn cleanup
    svn update
    echo ==================
    echo.
    echo.

    cd ..
)
echo.
echo Press any key to close...
pause > nul