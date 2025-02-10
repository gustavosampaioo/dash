import streamlit as st
import pandas as pd
import plotly.express as px

# Título da Dashboard
st.title("Dashboard de Contagem de Caixas Ópticas Interativa")

# Upload do arquivo XLSX
uploaded_file = st.file_uploader("Carregue o arquivo XLSX", type=["xlsx"])

if uploaded_file is not None:
    # Lendo o arquivo XLSX
    df = pd.read_excel(uploaded_file, engine='openpyxl')

    # Exibindo os dados brutos (opcional)
    st.write("Dados Brutos:")
    st.write(df)

    # Função para criar gráficos de barras interativos
    def criar_grafico(df, coluna_agrupamento, titulo):
        contagem = df.groupby(coluna_agrupamento)['Caixa Optica'].count().reset_index()
        contagem = contagem.rename(columns={'Caixa Optica': 'Quantidade de Caixas Ópticas'})
        fig = px.bar(contagem, x=coluna_agrupamento, y='Quantidade de Caixas Ópticas', title=titulo)
        return fig, contagem

    # Criando gráficos para cada categoria
    fig_zona, tabela_zona = criar_grafico(df, 'Zona', 'Contagem de Caixas Ópticas por Zona')
    fig_regiao, tabela_regiao = criar_grafico(df, 'Regiao', 'Contagem de Caixas Ópticas por Região')
    fig_pop, tabela_pop = criar_grafico(df, 'POP', 'Contagem de Caixas Ópticas por POP')
    fig_olt, tabela_olt = criar_grafico(df, 'OLT', 'Contagem de Caixas Ópticas por OLT')
    fig_placa, tabela_placa = criar_grafico(df, 'PLACA', 'Contagem de Caixas Ópticas por Placa')
    fig_pon, tabela_pon = criar_grafico(df, 'PON', 'Contagem de Caixas Ópticas por PON')

    # Exibindo os gráficos
    st.plotly_chart(fig_zona, use_container_width=True)
    st.plotly_chart(fig_regiao, use_container_width=True)
    st.plotly_chart(fig_pop, use_container_width=True)
    st.plotly_chart(fig_olt, use_container_width=True)
    st.plotly_chart(fig_placa, use_container_width=True)
    st.plotly_chart(fig_pon, use_container_width=True)

    # Função para filtrar os dados com base na seleção do gráfico
    def filtrar_dados(df, coluna, valor):
        return df[df[coluna] == valor]

    # Capturando a seleção do usuário em cada gráfico
    selecao_zona = st.selectbox("Selecione uma Zona para filtrar:", tabela_zona['Zona'].unique())
    df_filtrado = filtrar_dados(df, 'Zona', selecao_zona)

    selecao_regiao = st.selectbox("Selecione uma Região para filtrar:", df_filtrado['Regiao'].unique())
    df_filtrado = filtrar_dados(df_filtrado, 'Regiao', selecao_regiao)

    selecao_pop = st.selectbox("Selecione um POP para filtrar:", df_filtrado['POP'].unique())
    df_filtrado = filtrar_dados(df_filtrado, 'POP', selecao_pop)

    selecao_olt = st.selectbox("Selecione uma OLT para filtrar:", df_filtrado['OLT'].unique())
    df_filtrado = filtrar_dados(df_filtrado, 'OLT', selecao_olt)

    selecao_placa = st.selectbox("Selecione uma Placa para filtrar:", df_filtrado['PLACA'].unique())
    df_filtrado = filtrar_dados(df_filtrado, 'PLACA', selecao_placa)

    selecao_pon = st.selectbox("Selecione uma PON para filtrar:", df_filtrado['PON'].unique())
    df_filtrado = filtrar_dados(df_filtrado, 'PON', selecao_pon)

    # Exibindo os dados filtrados
    st.write("### Dados Filtrados:")
    st.write(df_filtrado)

else:
    st.write("Por favor, carregue um arquivo XLSX para começar.")
