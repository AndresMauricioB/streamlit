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

# Este comando crea un gráfico de torta o pastel
# Definir grupos de edad
bins = [0, 25, 30, 35, 100]  # Puedes ajustar estos límites según tus necesidades

# Etiquetas para los grupos de edad
labels = ['Menos de 25', '25-30', '30-35', 'Más de 35']

# Agregar una nueva columna 'Grupo de Edad' al DataFrame
df['Grupo de Edad'] = pd.cut(df['Edad'], bins=bins, labels=labels, right=False)

# Calcular la distribución de los grupos de edad
edad_distribucion = df['Grupo de Edad'].value_counts()

# Crear el gráfico de torta
st.write("Distribución de Edades:")
st.pie_chart(edad_distribucion)
 


