    # Dashboard interativo com Streamlit
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Dashboard Dinâmico CSV", layout="wide")
st.title("Dashboard Dinâmico a partir de CSV")

@st.cache_data
def carregar_dados(caminho_arquivo):
        try:
            df = pd.read_csv(caminho_arquivo)
            return df
        except Exception as e:
            st.error(f"Erro ao carregar o arquivo: {e}")
            return None

df = carregar_dados("data.csv")

if df is not None and not df.empty:
        st.subheader("Selecione as colunas para visualizar:")
        colunas_selecionadas = st.multiselect(
            "Colunas disponíveis:",
            options=list(df.columns),
            default=list(df.columns)
        )
        if colunas_selecionadas:
            st.dataframe(df[colunas_selecionadas])
            # Exemplo de gráfico se houver colunas numéricas
            colunas_numericas = df[colunas_selecionadas].select_dtypes(include=['number']).columns.tolist()
            if len(colunas_numericas) >= 1:
                st.subheader("Gráfico das colunas numéricas selecionadas:")
                st.line_chart(df[colunas_numericas])
        else:
            st.info("Selecione ao menos uma coluna para visualizar os dados.")
else:
        st.warning("O arquivo CSV está vazio ou não foi encontrado.")