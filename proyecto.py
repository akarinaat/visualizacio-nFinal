import pandas as pd
import streamlit as st
from pandasql import sqldf

df = pd.read_csv('dataset_Facebook.csv', sep=';')
clean_df = df.fillna(0)
clean_df.columns = clean_df.columns.str.replace(' ', '_')

# st.write(clean_df)

total_reach = sqldf('''
 Select sum(Lifetime_Post_Total_Reach) as [Numero de personas que vieron el post]
 from clean_df
 ''')

total_interacciones = sqldf('''
select count(Lifetime_engaged_users) as [Toatal de interacciones]
from clean_df 

 ''')

tipos_interracciones = sqldf('''
select distinct Type as [Tipos de interaccion]
from clean_df 

 ''')

# Número de personas que hicieron click en cualquier lado del post 

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


st.write(tipos_interracciones)
st.write(total_interacciones)
st.write(status)
st.write(photo)
st.write(link)
st.write(video)
st.write(inter_video)
st.write(inter_photo)
st.write(inter_status)
st.write(inter_link)
