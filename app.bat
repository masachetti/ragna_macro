@echo off
chdir %~dp0
call .\venv\Scripts\activate.bat && python app.py
pause