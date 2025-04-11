#!/bin/bash
streamlit run painel_resultados_real.py --server.port=$PORT &
python bot.py