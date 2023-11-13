import streamlit as st
import pandas as pd

st.write("""
# APP
Hola Mundo*
""")
# Datos de ejemplos
data = {
    'Nombre': ['Alice', 'Bob', 'Charlie', 'David'],
    'Edad': [25, 30, 35, 28],
    'Ciudad': ['Nueva York', 'Los Ángeles', 'Chicago', 'Houston']
}
df = pd.DataFrame(data)
# Este comando crea un gráfico de línea a partir de los datos contenidos en un DataFrame de Pandas (df)
st.line_chart(df)

# Este comando genera un gráfico de barras a partir de los 
# datos contenidos en un DataFrame de Pandas (df).
st.bar_chart(df)


# Este comando crea un gráfico de barras utilizando solo la columna 'Nombre' como 
# etiquetas en el eje x y la columna 'Edad' como valores en el eje y.
st.bar_chart(df.set_index('Nombre')['Edad'])

# Este comando genera un gráfico de dispersión que muestra puntos dispersos en función de los 
# valores de las columnas 'Ciudad' en el eje x y 'Edad' en el eje y.
st.scatter_chart(df, x='Ciudad', y='Edad')


number = st.slider("Pick a number", 0, 100)



