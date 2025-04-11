#!/bin/bash
# Inicia o bot em segundo plano
nohup python3 bot.py &

# Aguarda alguns segundos para garantir que o bot iniciou
sleep 5

# Inicia o painel Streamlit
streamlit run painel_resultados_real.py --server.port=10000
