@echo off
set var=%1
set var=%var:~0,-4%
pyrcc5 %1 -o %var%_rc.py
