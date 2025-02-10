import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_plotly_events import plotly_events

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

    # Exibindo os gráficos e capturando eventos de clique
    st.write("### Clique em uma barra para filtrar os dados:")

    # Gráfico de Zona
    st.write("#### Zona")
    selected_zona = plotly_events(fig_zona, click_event=True)
    if selected_zona:
        zona_selecionada = tabela_zona.iloc[selected_zona[0]['pointIndex']]['Zona']
        df_filtrado = df[df['Zona'] == zona_selecionada]
    else:
        df_filtrado = df

    # Gráfico de Região
    st.write("#### Região")
    selected_regiao = plotly_events(fig_regiao, click_event=True)
    if selected_regiao:
        regiao_selecionada = tabela_regiao.iloc[selected_regiao[0]['pointIndex']]['Regiao']
        df_filtrado = df_filtrado[df_filtrado['Regiao'] == regiao_selecionada]

    # Gráfico de POP
    st.write("#### POP")
    selected_pop = plotly_events(fig_pop, click_event=True)
    if selected_pop:
        pop_selecionado = tabela_pop.iloc[selected_pop[0]['pointIndex']]['POP']
        df_filtrado = df_filtrado[df_filtrado['POP'] == pop_selecionado]

    # Gráfico de OLT
    st.write("#### OLT")
    selected_olt = plotly_events(fig_olt, click_event=True)
    if selected_olt:
        olt_selecionada = tabela_olt.iloc[selected_olt[0]['pointIndex']]['OLT']
        df_filtrado = df_filtrado[df_filtrado['OLT'] == olt_selecionada]

    # Gráfico de Placa
    st.write("#### Placa")
    selected_placa = plotly_events(fig_placa, click_event=True)
    if selected_placa:
        placa_selecionada = tabela_placa.iloc[selected_placa[0]['pointIndex']]['PLACA']
        df_filtrado = df_filtrado[df_filtrado['PLACA'] == placa_selecionada]

    # Gráfico de PON
    st.write("#### PON")
    selected_pon = plotly_events(fig_pon, click_event=True)
    if selected_pon:
        pon_selecionada = tabela_pon.iloc[selected_pon[0]['pointIndex']]['PON']
        df_filtrado = df_filtrado[df_filtrado['PON'] == pon_selecionada]

    # Exibindo os dados filtrados
    st.write("### Dados Filtrados:")
    st.write(df_filtrado)

else:
    st.write("Por favor, carregue um arquivo XLSX para começar.")
