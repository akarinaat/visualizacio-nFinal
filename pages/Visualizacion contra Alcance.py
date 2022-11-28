import pandas as pd
import streamlit as st
from pandasql import sqldf
import numpy as np
import plotly.express as px


df = pd.read_csv('dataset_Facebook.csv', sep=';')
clean_df = df.fillna(0)
clean_df.columns = clean_df.columns.str.replace(' ', '_')

#Comparación por foto
alcance_foto = sqldf(''' 
SELECT Lifetime_post_total_reach AS Alcance, Lifetime_post_total_impressions AS Visualizaciones
FROM clean_df
WHERE Type = "Photo"
''') 
#Comparación por link
alcance_link = sqldf(''' 
SELECT Lifetime_post_total_reach AS Alcance, Lifetime_post_total_impressions AS Visualizaciones
FROM clean_df
WHERE Type = "Link"
''') 
#Comparación por status
alcance_status = sqldf(''' 
SELECT Lifetime_post_total_reach AS Alcance, Lifetime_post_total_impressions AS Visualizaciones
FROM clean_df
WHERE Type = "Status"
''') 
#Comparación por video
alcance_video = sqldf(''' 
SELECT Lifetime_post_total_reach AS Alcance, Lifetime_post_total_impressions AS Visualizaciones
FROM clean_df
WHERE Type = "Video"
''') 

#Visualizaciones por foto
v_foto = sqldf(''' 
SELECT Lifetime_post_total_impressions AS Visualizaciones
FROM clean_df
WHERE Type = "Photo"
''') 
#Visualizaciones por link
v_link = sqldf(''' 
SELECT Lifetime_post_total_impressions AS Visualizaciones
FROM clean_df
WHERE Type = "Link"
''') 
#Visualizaciones por status
v_status = sqldf(''' 
SELECT Lifetime_post_total_impressions AS Visualizaciones
FROM clean_df
WHERE Type = "Status"
''') 
#Visualizaciones por video
v_video = sqldf(''' 
SELECT Lifetime_post_total_impressions AS Visualizaciones
FROM clean_df
WHERE Type = "Video"
''')

#Alcance por foto
a_foto = sqldf(''' 
SELECT Lifetime_post_total_reach AS Alcance
FROM clean_df
WHERE Type = "Photo"
''') 
#Alcance por link
a_link = sqldf(''' 
SELECT Lifetime_post_total_reach AS Alcance
FROM clean_df
WHERE Type = "Link"
''') 
#Alcance por status
a_status = sqldf(''' 
SELECT Lifetime_post_total_reach AS Alcance
FROM clean_df
WHERE Type = "Status"
''') 
#Alcance por video
a_video = sqldf(''' 
SELECT Lifetime_post_total_reach AS Alcance
FROM clean_df
WHERE Type = "Video"
''')



st.title('Comparación entre Alcance y Visualizaciones por tipo de post')

# Select box hora, dia, mes
option = st.selectbox('Selecciona una opcion', ('Foto', 'Status', 'Link', 'Video'))

# Color palette
color_palette = ['#7D5A50', '#B4846C', '#E5B299', '#FCDEC0']

# Plot
if option == 'Foto':
	fig = px.line(alcance_foto, color_discrete_sequence=px.colors.sequential.RdBu)
	fig.update_layout(title='Alcance y Visualizaciones en post tipo foto', xaxis_title='Número de post', yaxis_title='Total')
	st.plotly_chart(fig)
	fig = px.line(v_foto, color_discrete_sequence=px.colors.sequential.RdBu)
	fig.update_layout(title='Visualizaciones en post tipo foto', xaxis_title='Número de post', yaxis_title='Visualizaciones')
	st.plotly_chart(fig)
	fig = px.line(a_foto, color_discrete_sequence=px.colors.sequential.RdBu)
	fig.update_layout(title='Alcance en post tipo foto', xaxis_title='Número de post', yaxis_title='Alcance')
	st.plotly_chart(fig)

elif option == 'Link':
	fig = px.line(alcance_link, color_discrete_sequence=px.colors.sequential.RdBu )
	fig.update_layout(title='Alcance y Visualizaciones en post tipo link', xaxis_title='Número de post', yaxis_title='Total')
	st.plotly_chart(fig)
	fig = px.line(v_link, color_discrete_sequence=px.colors.sequential.RdBu )
	fig.update_layout(title='Visualizaciones en post tipo link', xaxis_title='Número de post', yaxis_title='Visualizaciones')
	st.plotly_chart(fig)
	fig = px.line(a_link, color_discrete_sequence=px.colors.sequential.RdBu )
	fig.update_layout(title='Alcance en post tipo link', xaxis_title='Número de post', yaxis_title='Alcance')
	st.plotly_chart(fig)

elif option == 'Status':
	fig = px.line(alcance_status, color_discrete_sequence=px.colors.sequential.RdBu)
	fig.update_layout(title='Alcance y Visualizaciones en post tipo status', xaxis_title='Número de post', yaxis_title='Total')
	st.plotly_chart(fig)
	fig = px.line(v_status, color_discrete_sequence=px.colors.sequential.RdBu )
	fig.update_layout(title='Visualizaciones en post tipo status', xaxis_title='Número de post', yaxis_title='Visualizaciones')
	st.plotly_chart(fig)
	fig = px.line(a_status, color_discrete_sequence=px.colors.sequential.RdBu )
	fig.update_layout(title='Alcance en post tipo status', xaxis_title='Número de post', yaxis_title='Alcance')
	st.plotly_chart(fig)

elif option == 'Video':
	fig = px.line(alcance_video, color_discrete_sequence=px.colors.sequential.RdBu )
	fig.update_layout(title='Alcance y Visualizaciones en post tipo video', xaxis_title='Número de post', yaxis_title='Total')
	st.plotly_chart(fig)
	fig = px.line(v_video, color_discrete_sequence=px.colors.sequential.RdBu )
	fig.update_layout(title='Visualizaciones en post tipo video', xaxis_title='Número de post', yaxis_title='Visualizaciones')
	st.plotly_chart(fig)
	fig = px.line(a_video, color_discrete_sequence=px.colors.sequential.RdBu )
	fig.update_layout(title='Alcance en post tipo video', xaxis_title='Número de post', yaxis_title='Alcance')
	st.plotly_chart(fig)

