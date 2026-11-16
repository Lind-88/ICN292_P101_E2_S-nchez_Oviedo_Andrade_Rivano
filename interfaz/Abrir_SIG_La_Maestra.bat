
@echo off
cd /d "%~dp0"
py SIG_La_Maestra.py

if errorlevel 1 (
    echo.
    echo No se pudo iniciar el programa.
    pause
)
