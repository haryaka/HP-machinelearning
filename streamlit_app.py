import streamlit as st
import pandas as pd

st.title('Machine Learning App')

st.info('Ini adalah Machine Learning untuk memenuhi project UAS mata kuliah Data Mining')

df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/refs/heads/master/penguins_cleaned.csv')
df
