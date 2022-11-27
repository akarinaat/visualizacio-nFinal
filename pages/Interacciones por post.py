import pandas as pd
import streamlit as st
from pandasql import sqldf
import numpy as np
import plotly.express as px


df = pd.read_csv('dataset_Facebook.csv', sep=';')
clean_df = df.fillna(0)
clean_df.columns = clean_df.columns.str.replace(' ', '_')



# Post type 
# tipos_interracciones = sqldf('''
# select distinct Type as [Tipos de interaccion]
# from clean_df 

#  ''')



st.title('Número de personas que hicieron click en el post (Usuarios únicos)')

# Unique users interactions per post
interacciones_tipo = sqldf(''' 
Select Type as Tipo, count(Lifetime_engaged_users) as Interacciones
from clean_df
group by Type
''')

# Post type
tipos = sqldf('''
select distinct Type from clean_df
''')

# Pie chart
fig = px.pie(interacciones_tipo, values='Interacciones', names='Tipo')
st.plotly_chart(fig)


# Radio
st.radio('Tipo de interacciones',tipos)

#sacar el total de interacciones por tipo
inter_video = sqldf('''
select sum(Total_Interactions) as [Interacciones por video]
from clean_df 
where Type = 'Video'
 ''')

inter_photo = sqldf('''
select sum(Total_Interactions) as [Interacciones por foto]
from clean_df 
where Type = 'Photo'
 ''')

inter_status = sqldf('''
select sum(Total_Interactions) as [Interacciones por status]
from clean_df 
where Type = 'Status'
 ''')


inter_link = sqldf('''
select sum(Total_Interactions) as [Interacciones por link]
from clean_df 
where Type = 'Link'
 ''')


# # Número de interacciones totales por mes por lifetime engaged users
    
# totInt_month = sqldf(
#     '''
#     Select distinct Post_Month, sum(Total_Interactions) as [Interacciones por mes de usuarios únicos]
#     from clean_df
#     group by Post_Month
#     order by sum(Total_Interactions) desc
#     '''
# ) 




st.write(interacciones_tipo)

st.title('Suma total de las interacciones')
st.write(inter_video)
st.write(inter_photo)
st.write(inter_status)
st.write(inter_link)


