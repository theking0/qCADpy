@echo off
set var=%1
set var=%var:~0,-3%
pyuic5 %1 -o %var%.py
