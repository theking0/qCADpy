@echo off

if [%1]==[] goto usage

call qrc2py %1
call ui2py %2
goto :eof

:usage
echo:
@echo %0 ^<resources_file.qrc^> ^<ui_File.ui^>
goto :eof

:eof
exit /B 1