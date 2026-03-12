import streamlit as st
import pandas as pd
import plotly.express as px

#Criação do Titulo
st.title("Dashboard - Funcionários")

#Carregamento dos Dados
df = pd.read_csv("novos_dados.csv")
st.subheader("Tabela De Dados")
st.dataframe(df)

#Criação de Filtro
departamento = st.selectbox("Selecione o Departamento:", df["departamento"].unique())
df_filtrado = df[df["departamento"] == departamento]
st.subheader("Dados Filtrados")
st.write(df_filtrado)

#Elaboração de Grafico
barra = px.bar(
        df_filtrado,
        x = "nome_completo",
        y = "salario_mensal_brl",
        color = "nome_completo",
        title = "Salário Dos Funcionários"
)

st.plotly_chart(barra)