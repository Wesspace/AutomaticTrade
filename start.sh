#!/bin/bash
nohup python3 bot.py > bot.log 2>&1 &
sleep 5
streamlit run painel_resultados_real.py --server.port=10000
