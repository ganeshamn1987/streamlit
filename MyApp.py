import streamlit as st
import pandas as pd
 
st.write("""
# My first Streamlit App
Hello *World!*
""")
 
df = pd.read_csv("C:\\project_workspace\\lad_workspace\\streamlit\\test.txt")
st.line_chart(df)
