@echo off
chdir %~dp0
call .\venv\Scripts\activate.bat && python tests.py
pause