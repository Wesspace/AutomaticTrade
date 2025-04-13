import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="SmartTrader View", layout="wide")
st.title("📊 Painel de Resultados - SmartTrader View")

# Carregando relatório
csv_path = "relatorio_volatile.csv"

if os.path.exists(csv_path):
    df = pd.read_csv(csv_path)

    if not df.empty:
        st.success(f"Relatório carregado com sucesso. {len(df)} operações registradas.")

        # Filtros
        ativos = df['Ativo'].unique().tolist()
        direcoes = df['Direcao'].unique().tolist()
        data_min = pd.to_datetime(df['Data']).min()
        data_max = pd.to_datetime(df['Data']).max()

        with st.sidebar:
            st.header("🔍 Filtros")
            ativo_filter = st.multiselect("Ativos", ativos, default=ativos)
            direcao_filter = st.multiselect("Direção", direcoes, default=direcoes)
            data_range = st.date_input("Período", [data_min, data_max])

        # Aplicando filtros
        df['Data'] = pd.to_datetime(df['Data'])
        df_filtrado = df[
            (df['Ativo'].isin(ativo_filter)) &
            (df['Direcao'].isin(direcao_filter)) &
            (df['Data'] >= pd.to_datetime(data_range[0])) &
            (df['Data'] <= pd.to_datetime(data_range[1]))
        ]

        st.subheader("📈 Resultados das Operações Filtradas")
        st.dataframe(df_filtrado, use_container_width=True)

        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Total Operações", len(df_filtrado))
        with col2:
            st.metric("Lucro Total (USDT)", f"{df_filtrado['Lucro(USDT)'].sum():.2f}")
        with col3:
            st.metric("Média de Lucro (%)", f"{df_filtrado['Lucro(%)'].mean():.2f}")

    else:
        st.warning("O relatório está vazio.")
else:
    st.error("Arquivo relatorio_volatile.csv não encontrado.")
