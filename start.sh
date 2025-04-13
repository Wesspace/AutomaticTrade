#!/bin/bash

streamlit run painel_resultados_real.py --server.port=$PORT --server.address=0.0.0.0 --server.enableCORS=false --server.enableXsrfProtection=false
