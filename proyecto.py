import pandas as pd
import streamlit as st
from pandasql import sqldf
import numpy as np
import plotly.express as px

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

st.radio('Tipo de interacciones',tipos_interracciones)

# Número de personas que hicieron click en cualquier lado del post 
# Número de interacciones totales por mes
# 

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


# Número de interacciones totales por mes por lifetime engaged users
    
totInt_month = sqldf(
    '''
    Select distinct Post_Month, sum(Total_Interactions) as [Interacciones por mes de usuarios únicos]
    from clean_df
    group by Post_Month
    order by sum(Total_Interactions) desc
    '''
) 

p = totInt_month.to_numpy()

month = st.selectbox('Seleccione el mes', ['Enero', 'Febrero', 'Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre'])

if month == 'Enero':
    st.write('Seleccionaste Enero')
    h = px.histogram(totInt_month, x=['Enero', 'Febrero', 'Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre'])


    st.plotly_chart(h)


  


st.write(p)


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


