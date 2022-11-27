import streamlit as st
from PIL import Image

st.title('Elate Cosmetics')
cosmetics_img = Image.open('elateCosmetics.jpeg')
st.image(cosmetics_img)