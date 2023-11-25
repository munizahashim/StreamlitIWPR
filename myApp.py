import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Load the data from Excel

# -------------------------------Title of the Page -----------------------------------
st.title('Buildings in Cities')

# --------------------------------- Side Bar --------------------------------------
st.sidebar.header("Choose Page")
city = st.sidebar.selectbox('Which page you want to visit?',
                             ('Bishkek', 'Astana', 'Ashgabat', 'Dushanbe', 'Tashkent'))

# Define a color map and normalize the number of floors to map to colors
light_blue = (0, 93, 138)  # (R, G, B) for light blue
color = (light_blue[0] / 255, light_blue[1] / 255, light_blue[2] / 255)  # Normalize RGB values to be in the range [0, 1]

# Create a 3D bar graph using Plotly Express
if city == 'Bishkek':
    data = pd.read_excel("C:/Users/muniza.hashim/Desktop/IWPR/IWPR internship/IWPR internship/building/Final Project/Bishkek_data.xlsx")
elif city == 'Tashkent':
    data = pd.read_excel("C:/Users/muniza.hashim/Desktop/IWPR/IWPR internship/IWPR internship/building/Final Project/Tashkent_data.xlsx")
elif city == 'Dushanbe':
    data = pd.read_excel("C:/Users/muniza.hashim/Desktop/IWPR/IWPR internship/IWPR internship/building/Final Project/Dushanbe_data.xlsx")
elif city == 'Astana':
    data = pd.read_excel("C:/Users/muniza.hashim/Desktop/IWPR/IWPR internship/IWPR internship/building/Final Project/Astana_data.xlsx")
elif city == 'Ashgabat':
    data = pd.read_excel("C:/Users/muniza.hashim/Desktop/IWPR/IWPR internship/IWPR internship/building/Final Project/Ashgabat_data.xlsx")

fig = px.scatter_3d(data, x=np.arange(len(data)), y='No. of Buildings', z='No. of Floors', color='No. of Floors',
                   opacity=0.7, color_continuous_scale='blues')

# Set layout for the 3D bar graph
fig.update_layout(scene=dict(
    xaxis_title=city,
    yaxis_title='No. of Buildings',
    zaxis_title='No. of Floors'
))

# Show the 3D bar graph using Streamlit
st.plotly_chart(fig)
