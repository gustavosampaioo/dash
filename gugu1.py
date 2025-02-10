import streamlit as st
import pandas as pd

# Título da Dashboard
st.title("Dashboard de Contagem de Caixas Ópticas")

# Upload do arquivo XLSX
uploaded_file = st.file_uploader("Carregue o arquivo XLSX", type=["xlsx"])

if uploaded_file is not None:
    # Lendo o arquivo XLSX
    df = pd.read_excel(uploaded_file, engine='openpyxl')

    # Exibindo os dados brutos (opcional)
    st.write("Dados Brutos:")
    st.write(df)

    # Função para criar tabelas agrupadas
    def criar_tabela_agrupada(df, coluna_agrupamento, coluna_contagem):
        tabela = df.groupby(coluna_agrupamento)[coluna_contagem].count().reset_index()
        tabela = tabela.rename(columns={coluna_contagem: 'Quantidade de Caixas Ópticas'})
        return tabela

    # Criando tabelas para cada categoria
    st.write("### Contagem por Zona")
    tabela_zona = criar_tabela_agrupada(df, 'Zona', 'Caixa Optica')
    st.write(tabela_zona)

    st.write("### Contagem por Região")
    tabela_regiao = criar_tabela_agrupada(df, 'Regiao', 'Caixa Optica')
    st.write(tabela_regiao)

    st.write("### Contagem por POP")
    tabela_pop = criar_tabela_agrupada(df, 'POP', 'Caixa Optica')
    st.write(tabela_pop)

    st.write("### Contagem por OLT")
    tabela_olt = criar_tabela_agrupada(df, 'OLT', 'Caixa Optica')
    st.write(tabela_olt)

    st.write("### Contagem por Placa")
    tabela_placa = criar_tabela_agrupada(df, 'PLACA', 'Caixa Optica')
    st.write(tabela_placa)

    st.write("### Contagem por PON")
    tabela_pon = criar_tabela_agrupada(df, 'PON', 'Caixa Optica')
    st.write(tabela_pon)

    # Gráfico de barras para visualização (opcional)
    st.write("### Gráfico de Barras por Zona")
    st.bar_chart(tabela_zona.set_index('Zona')['Quantidade de Caixas Ópticas'])

else:
    st.write("Por favor, carregue um arquivo XLSX para começar.")
