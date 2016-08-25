@echo off

@REG DELETE HKCU\Software\Microsoft\VisualStudio\9.0\FileMRUList /va /f
@REG DELETE HKCU\Software\Microsoft\VisualStudio\9.0\ProjectMRUList /va /f