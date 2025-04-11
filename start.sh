#!/bin/bash

# Força o Streamlit a rodar na porta esperada
streamlit run painel_resultados_real.py --server.port=$PORT --server.enableCORS=false --server.headless=true
