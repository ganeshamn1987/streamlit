import streamlit as st
import pandas as pd
 
st.write("""
# My first Streamlit Application
Hello *World!!!!*
""")
 
df = pd.read_csv("test.txt")
st.line_chart(df)
