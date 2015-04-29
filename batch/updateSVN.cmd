@echo off
for /d %%i in (*) do (
    cd %%~fi
    echo updating %%~fi
    svn update > nul
    cd ..
)
echo.
echo completed...
pause > nul