@echo off
for /f "tokens=3" %%i in ('reg query "HKCU\Control Panel\International" /v "sLanguage"') do (
    set reg_localevar=%%i
)
for /f "tokens=3" %%i in ('reg query "HKCU\Control Panel\Desktop" /v "PreferredUILanguages"') do (
    set reg_uilanguage=%%i
)

echo %reg_localevar%
echo %reg_uilanguage%

pause>nul