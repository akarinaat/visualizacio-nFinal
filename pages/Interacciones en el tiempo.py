import pandas as pd
import streamlit as st
from pandasql import sqldf
import plotly.express as px

df = pd.read_csv('dataset_Facebook.csv', sep=';')
clean_df = df.fillna(0)
clean_df.columns = clean_df.columns.str.replace(' ', '_')

# Month
month = sqldf('''
 Select Post_month, AVG(Total_interactions) as [AVG_Total_interactions] from clean_df group by Post_month
 ''')

# Names of the months
month_names = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']

# Replace the numbers with the names
month[month.columns[0]] = month[month.columns[0]].replace([1,2,3,4,5,6,7,8,9,10,11,12], month_names)

# Hour
hour = sqldf('''
    Select Post_hour, AVG(Total_interactions) as [AVG_Total_interactions], AVG("Lifetime_engaged_users") from clean_df group by Post_hour
    ''')

# Day
day = sqldf('''
    Select Post_weekday, AVG(Total_interactions) as [AVG_Total_interactions] from clean_df group by Post_weekday
    ''')

# Weekday names
weekday_names = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo']

# Replace the numbers with the names
day[day.columns[0]] = day[day.columns[0]].replace([1,2,3,4,5,6,7], weekday_names)

# Select box hora, dia, mes
option = st.selectbox('Selecciona una opcion', ('Hora', 'Dia', 'Mes'))

# Plot
if option == 'Dia':
    fig = px.line(day, x=day.columns[0], y=day.columns[1])
    fig.update_layout(title='Interacciones por dia', xaxis_title='Dia', yaxis_title='Interacciones')
    st.plotly_chart(fig)

elif option == 'Mes':
    fig = px.line(month, x=month.columns[0], y=month.columns[1])
    fig.update_layout(title='Interacciones por mes', xaxis_title='Mes', yaxis_title='Interacciones')
    st.plotly_chart(fig)

elif option == 'Hora':
    fig = px.line(hour, x=hour.columns[0], y=hour.columns[1])
    fig.update_layout(title='Interacciones por hora', xaxis_title='Hora', yaxis_title='Interacciones')
    st.plotly_chart(fig)
