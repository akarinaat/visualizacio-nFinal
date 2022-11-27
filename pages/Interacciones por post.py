import pandas as pd
import streamlit as st
from pandasql import sqldf
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt

df = pd.read_csv('dataset_Facebook.csv', sep=';')
clean_df = df.fillna(0)
clean_df.columns = clean_df.columns.str.replace(' ', '_')



# Post type 
tipos_interracciones = sqldf('''
select distinct Type as [Tipos de interaccion]
from clean_df 

 ''')
st.radio('Tipo de interacciones',tipos_interracciones)


st.title('Número de personas que hicieron click en el post (Usuarios únicos)')


status = sqldf('''
select count(Lifetime_engaged_users) as [Interacciones por estatus]
from clean_df 
where Type = 'Status'
 ''')

photo = sqldf('''
select count(Lifetime_engaged_users) as [Interacciones por foto]
from clean_df 
where Type = 'Photo'
 ''')

link = sqldf('''
select count(Lifetime_engaged_users) as [Interacciones por foto]
from clean_df 
where Type = 'Link'
 ''')

video = sqldf('''
select count(Lifetime_engaged_users) as [Interaccion de usuarios únicos por video]
from clean_df 
where Type = 'Video'
 ''')

# Pie chart

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = tipos_interracciones
sizes = [15, 30, 45, 10]
explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

st.pyplot(fig1)



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




st.write(tipos_interracciones)

st.write(status)
st.write(photo)
st.write(link)
st.write(video)
st.title('Suma total de las interacciones')
st.write(inter_video)
st.write(inter_photo)
st.write(inter_status)
st.write(inter_link)


