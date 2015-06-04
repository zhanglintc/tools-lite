@echo off

color 3e

for /d %%i in (*) do (
    title Updating...  %%~fi

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

title Competed...  Powered by Lane at ZDS

echo.
echo Press any key to close...
pause > nul