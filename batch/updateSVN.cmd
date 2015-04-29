@echo off
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
echo Completed...
pause > nul