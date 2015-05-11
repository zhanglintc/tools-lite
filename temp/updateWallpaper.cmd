@echo off
cmd /c BingImg.bat
::set regadd=reg add "HKEY_CURRENT_USER\Control Panel\Desktop"
::%regadd%" /v TileWallpaper /d "0" /f
::%regadd%" /v Wallpaper /d "%cd%\BingImg\today.jpg" /f
::%regadd%" /v WallpaperStyle /d "2" /f
RunDll32.exe USER32.DLL,UpdatePerUserSystemParameters
pause