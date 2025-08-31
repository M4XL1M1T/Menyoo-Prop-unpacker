@echo off
REM Aktiviere das virtuelle Environment
call .venv\Scripts\activate
REM Installiere die benötigten Pakete
pip install -r requirements.txt
REM Starte das Python-Skript
python unpackerlister.py
pause
