@echo off
for /f "tokens=3" %%i in ('reg query "HKCU\Control Panel\International" /v "sLanguage"') do (
    set reg_localevar=%%i
)

echo %reg_localevar%

pause>nul