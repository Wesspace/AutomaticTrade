#!/bin/bash

echo "Iniciando painel Streamlit na porta 10000..."
streamlit run painel_resultados_real.py --server.port 10000 --server.enableCORS false --server.enableXsrfProtection false
