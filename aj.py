import streamlit as st
import pandas as pd

import folium
 


m = folium.Map(location=[51.5074, -0.1278], zoom_start=12)
st.write(m)
