#!/bin/bash

echo "Iniciando painel..."
streamlit run painel_resultados_real.py --server.port=$PORT --server.address=0.0.0.0 --server.headless=true --server.enableCORS=false --server.enableXsrfProtection=false
