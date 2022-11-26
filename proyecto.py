import pandas as pd
import streamlit as st
from pandasql import sqldf

df = pd.read_csv('dataset_Facebook.csv', sep=';')
clean_df = df.fillna(0)
clean_df.columns = clean_df.columns.str.replace(' ','_')

#st.write(clean_df)

total_reach = sqldf('''
 Select sum(Lifetime_Post_Total_Reach) as [Numero de personas que vieron el post]
 from clean_df
 ''')

st.write(total_reach) 









