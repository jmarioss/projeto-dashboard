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

@st.cache_data
def carregar_arquivo(arquivo):
        try:
            df = pd.read_csv(arquivo)
            return df
        except Exception as e:
            st.error(f"Erro ao carregar o arquivo: {e}")
            return None

#df = carregar_dados("data.csv")

arquivo = st.file_uploader("Carregue seu arquivo CSV", type=["csv"])

df = carregar_arquivo(arquivo)

if df is not None and not df.empty:
    st.subheader("Selecione as colunas para visualizar:")
    colunas_disponiveis = list(df.columns)
    col_eixo_x = st.selectbox("Selecione o eixo X (ex: datas):", options=colunas_disponiveis)
    colunas_numericas = df.select_dtypes(include=['number']).columns.tolist()
    colunas_y = st.multiselect(
        "Selecione as colunas para o eixo Y (valores):",
        options=colunas_numericas,
        default=colunas_numericas
    )
    tipo_grafico = st.multiselect(
        "Selecione o tipo de gráfico:",
        options=["Linha", "Barra", "Área", "Dispersão"],
        default=["Linha"]
    )
    st.dataframe(df[[col_eixo_x] + colunas_y])
    if colunas_y:
        st.subheader("Visualização do gráfico:")
        dados_grafico = df[[col_eixo_x] + colunas_y].dropna()
        dados_grafico = dados_grafico.sort_values(by=col_eixo_x)
        dados_grafico = dados_grafico.set_index(col_eixo_x)
        for opcao in tipo_grafico:
            if opcao == "Linha":
                st.line_chart(dados_grafico)
            elif opcao == "Barra":
                st.bar_chart(dados_grafico)
            elif opcao == "Área":
                st.area_chart(dados_grafico)
            elif opcao == "Dispersão":
                import altair as alt
                for col_y in colunas_y:
                    chart = alt.Chart(df).mark_circle().encode(
                        x=col_eixo_x,
                        y=col_y,
                        tooltip=[col_eixo_x, col_y]
                    ).interactive()
                    st.altair_chart(chart, use_container_width=True)
    else:
        st.info("Selecione ao menos uma coluna para o eixo Y.")
else:
    st.warning("O arquivo CSV está vazio ou não foi encontrado.")