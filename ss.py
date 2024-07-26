import pygwalker as pyg
import pandas as pd
import streamlit.components.v1 as components
import streamlit as st
 
# Adjust the width of the Streamlit page
st.set_page_config(
    page_title="Automatic Analytics",
    layout="wide"
)
 
# Add Title
st.title("Automatic Analytics")
 
# Import your data
df = pd.read_csv('sales_data_sample.csv',sep=",", encoding='Latin-1')
 
# Generate the HTML using Pygwalker
pyg_html = pyg.to_html(df)
 
# Embed the HTML into the Streamlit app
components.html(pyg_html, height=1000, scrolling=True)
