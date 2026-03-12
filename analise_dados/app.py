import streamlit as st
import pandas as pd
import plotly.express as px

#Criação do Titulo
st.title("Dashboard - Desempenho de Alunos")

#Carregamento dos Dados
df = pd.read_csv("dados.csv")
st.subheader("Tabela De Dados")
st.dataframe(df)

#Criação de Filtro
curso = st.selectbox("Selecione o Curso:", df["Curso"].unique())
df_filtrado = df[df["Curso"] == curso]
st.subheader("Dados Filtrados")
st.write(df_filtrado)

#Elaboração de Grafico
barra = px.bar(
        df_filtrado,
        x = "Aluno",
        y = "Nota",
        color = "Aluno",
        title = "Notas Dos Alunos"
)

st.plotly_chart(barra)