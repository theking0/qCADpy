pyinstaller --onefile %1
@echo off
cd dist 
set var=%1
set var=%var:~0,-3%
copy %var%.exe  C:%HOMEPATH%\Desktop\%var%.exe
cd ..
echo FILE %var%.exe COPIATO SUL DESKTOP
@echo on