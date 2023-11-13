import streamlit as st
import pandas as pd

import matplotlib.pyplot as plt
 
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

data = {'Categoría A': 30, 'Categoría B': 20, 'Categoría C': 45}
fig, ax = plt.subplots()
ax.bar(data.keys(), data.values())
st.pyplot(fig)
