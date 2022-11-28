import pandas as pd
import streamlit as st
import plotly.express as px
import matplotlib.pyplot as plt

df = pd.read_csv('dataset_Facebook.csv', sep=';')
clean_df = df.fillna(0)
clean_df.columns = clean_df.columns.str.replace(' ', '_')

likes_tiempo = clean_df.iloc[::-1].reset_index()
likes_tiempo = likes_tiempo[['Page_total_likes','Post_Month']]
likes_tiempo = likes_tiempo.groupby(["Post_Month"]).mean()

fig = px.line(likes_tiempo, title="Cantidad de Likes a través del Tiempo", labels={
        "Post_Month":"Número de Mes", 
        "value":"Cantidad de Likes", 
        "variable":"Variable"})
st.plotly_chart(fig)