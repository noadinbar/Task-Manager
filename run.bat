@echo off
cd /d "%~dp0"
python -m pip install colorama >nul 2>&1
python main.py
pause
