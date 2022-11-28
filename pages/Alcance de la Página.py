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

st.title("Alcance de la Página")

st.subheader("Likes Acumulados en el Año")

fig = px.line(likes_tiempo, title="Cantidad de Likes a través del Tiempo", color_discrete_sequence=['#B4846C'], labels={
        "Post_Month":"Número de Mes", 
        "value":"Cantidad de Likes"})
fig.update(layout_showlegend=False)
st.plotly_chart(fig)


month_names = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
post_reach = clean_df[['Lifetime_Post_Total_Reach', 'Post_Month', 'Paid']].iloc[::-1]

post_reach_total = post_reach[['Lifetime_Post_Total_Reach', 'Post_Month']].groupby(["Post_Month"]).mean()
post_reach_total['Mes'] = month_names

post_reach_paid =  post_reach[post_reach['Paid'] == 1.0][['Lifetime_Post_Total_Reach', 'Post_Month']].groupby(["Post_Month"]).mean()
post_reach_paid['Mes'] = month_names

post_reach_free = post_reach[post_reach['Paid'] == 0.0][['Lifetime_Post_Total_Reach', 'Post_Month']].groupby(["Post_Month"]).mean()
post_reach_free['Mes'] = month_names

st.subheader("Alcance de Visualizaciones")

option = st.selectbox('Filtrar Publicaciones:', ('Todas', 'Pagadas', 'Gratuitas'))

if option == 'Todas':
        fig = px.bar(x=post_reach_total['Mes'], y=post_reach_total['Lifetime_Post_Total_Reach'], color_discrete_sequence=['#7D5A50'],
                title="Visualizaciones a través del Tiempo", labels={
                "x":"Mes", 
                "y":"Visualizaciones Promedio por Publicación"})
        fig.update(layout_showlegend=False)
        st.plotly_chart(fig)
elif option == 'Pagadas':
        fig = px.bar(x=post_reach_paid['Mes'], y=post_reach_paid['Lifetime_Post_Total_Reach'], color_discrete_sequence=['#7D5A50'],
                title="Visualizaciones a través del Tiempo (Sólo Publicaciones Pagadas)", labels={
                "x":"Mes", 
                "y":"Visualizaciones Promedio por Publicación"})
        fig.update(layout_showlegend=False)
        st.plotly_chart(fig)
elif option == 'Gratuitas':
        fig = px.bar(x=post_reach_free['Mes'], y=post_reach_free['Lifetime_Post_Total_Reach'], color_discrete_sequence=['#7D5A50'],
                title="Visualizaciones a través del Tiempo (Sólo Publicaciones Gratuitas)", labels={
                "x":"Mes", 
                "y":"Visualizaciones Promedio por Publicación"})
        fig.update(layout_showlegend=False)
        st.plotly_chart(fig)