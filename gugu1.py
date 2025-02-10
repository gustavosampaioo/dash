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

    # Contagem de Caixas Ópticas por Zona, Região, POP, OLT, Placa e PON
    contagem = df.groupby(['Zona', 'Regiao', 'POP', 'OLT', 'PLACA', 'PON'])['Caixa Optica'].count().reset_index()

    # Renomeando a coluna de contagem
    contagem = contagem.rename(columns={'Caixa Optica': 'Quantidade de Caixas Ópticas'})

    # Exibindo a contagem
    st.write("Contagem de Caixas Ópticas por Zona, Região, POP, OLT, Placa e PON:")
    st.write(contagem)

    # Gráfico de barras para visualização
    st.bar_chart(contagem.set_index('Zona')['Quantidade de Caixas Ópticas'])

else:
    st.write("Por favor, carregue um arquivo XLSX para começar.")