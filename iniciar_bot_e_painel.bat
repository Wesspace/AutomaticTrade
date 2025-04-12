@echo off
cd /d "%~dp0"
call venv\Scripts\activate
start cmd /k "python bot.py"
start cmd /k "streamlit run painel_resultados_real.py --server.port=10000"