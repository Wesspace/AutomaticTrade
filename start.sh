#!/bin/bash

# Executa o painel Streamlit na porta que o Render define
streamlit run painel_resultados_real.py --server.port=$PORT --server.enableCORS=false --server.enableXsrfProtection=false
