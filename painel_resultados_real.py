import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

st.title("Painel de Resultados - SmartTrader View 🚀")

try:
    df = pd.read_csv("relatorio_volatile.csv")
    st.success("Relatório carregado com sucesso!")
    st.dataframe(df.tail(10))  # Exibe as últimas 10 entradas
except Exception as e:
    st.error(f"Erro ao carregar relatório: {e}")
