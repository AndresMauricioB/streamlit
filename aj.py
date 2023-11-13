import streamlit as st
import pandas as pd

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

st.bar_chart(df)

st.area_chart(df)
# Gráfico de barras de edades
st.bar_chart(df.set_index('Nombre')['Edad'])

# Gráfico de dispersión de edades por ciudad
st.scatter_chart(df, x='Ciudad', y='Edad')

# Gráfico de torta de edades
st.pie_chart(df['Edad'])
 


