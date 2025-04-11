#!/bin/bash

echo "Iniciando bot.py..."
python3 bot.py &

echo "Iniciando painel_resultados_real.py..."
streamlit run painel_resultados_real.py --server.port 10000 --server.address 0.0.0.0
