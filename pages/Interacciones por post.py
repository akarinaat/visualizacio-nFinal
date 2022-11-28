import pandas as pd
import streamlit as st
from pandasql import sqldf
import numpy as np
import plotly.express as px


df = pd.read_csv('dataset_Facebook.csv', sep=';')
clean_df = df.fillna(0)
clean_df.columns = clean_df.columns.str.replace(' ', '_')



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
fig = px.pie(interacciones_tipo, values='Interacciones', names='Tipo', color_discrete_sequence=px.colors.sequential.RdBu)
st.plotly_chart(fig)


st.title('Suma total de las interacciones')

# Radio
op_radio= st.radio('Tipo de interacciones',tipos)



#sacar el total de interacciones por tipo
inter_video = sqldf('''
select distinct [Post_Month] as Mes, sum(Total_Interactions) as [Interacciones por video]
from clean_df 
where Type = 'Video'
group by [Post_Month]
 ''')

inter_photo = sqldf('''
select distinct [Post_Month] as Mes, sum(Total_Interactions) as [Interacciones por foto]
from clean_df 
where Type = 'Photo'
group by [Post_Month]
 ''')

inter_status = sqldf('''
select distinct [Post_Month] as Mes, sum(Total_Interactions) as [Interacciones por status]
from clean_df 
where Type = 'Status'
group by [Post_Month]
 ''')


inter_link = sqldf('''
select distinct [Post_Month] as Mes, sum(Total_Interactions) as [Interacciones por link]
from clean_df 
where Type = 'Link'
group by [Post_Month]
 ''')

colors = ['#E98580']
colors2 = ['#B4846C']
if op_radio == 'Photo':
     
        fig = px.scatter(inter_photo, y="Interacciones por foto", x="Mes", color_discrete_sequence=colors)
        fig.update_traces(marker_size=10)
        st.plotly_chart(fig)

        fig2 = px.histogram(inter_photo, x="Interacciones por foto", color_discrete_sequence=colors2)
        st.plotly_chart(fig2)

elif op_radio == 'Status':

        fig = px.scatter(inter_status, y="Interacciones por status", x="Mes", color_discrete_sequence=colors)
        fig.update_traces(marker_size=10)
        st.plotly_chart(fig)

        fig2 = px.histogram(inter_status, x="Interacciones por status", color_discrete_sequence=colors2)
        st.plotly_chart(fig2)

elif op_radio == 'Link':

        fig = px.scatter(inter_link, y="Interacciones por link", x="Mes", color_discrete_sequence=colors)
        fig.update_traces(marker_size=10)
        st.plotly_chart(fig)

        fig2 = px.histogram(inter_link, x="Interacciones por link", color_discrete_sequence=colors2)
        st.plotly_chart(fig2)

elif op_radio == 'Video':

        fig = px.scatter(inter_video, y="Interacciones por video", x="Mes", color_discrete_sequence=colors)
        fig.update_traces(marker_size=10)
        st.plotly_chart(fig)

        fig2 = px.histogram(inter_video, x="Interacciones por video", color_discrete_sequence=colors2)
        st.plotly_chart(fig2)

# # Número de interacciones totales por mes por lifetime engaged users
    
# totInt_month = sqldf(
#     '''
#     Select distinct Post_Month, sum(Total_Interactions) as [Interacciones por mes de usuarios únicos]
#     from clean_df
#     group by Post_Month
#     order by sum(Total_Interactions) desc
#     '''
# ) 




#st.write(interacciones_tipo)


# st.write(inter_video)
# st.write(inter_photo)
# st.write(inter_status)
# st.write(inter_link)


