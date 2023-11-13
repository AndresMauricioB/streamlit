import streamlit as st
import pandas as pd

import folium
 
st.write("""
# My first app
Hello *world!*
""")
data = {
    'Nombre': ['Alice', 'Bob', 'Charlie', 'David'],
    'Edad': [25, 30, 35, 28],
    'Ciudad': ['Nueva York', 'Los Ángeles', 'Chicago', 'Houston']
}

df = pd.DataFrame(data)
st.line_chart(df)

m = folium.Map(location=[51.5074, -0.1278], zoom_start=12)
st.write(m)
