from app.utils import page_layout
import streamlit as st
import plotly.express as px
from plotly.data import iris

page_layout() 


iris = iris()
sepal_length = iris['sepal_length']
petal_length = iris['petal_length']
species = iris['species']


#Scatter
st.header("Scatter")
fig = px.scatter(iris, x=iris['petal_length'], y=iris['sepal_length'], color=iris['species'])
st.plotly_chart(fig, use_container_width=True)


#Bar
st.header("Bar")
fig = px.bar(iris, x=sepal_length, y=species, color=iris['species'])
st.plotly_chart(fig, use_container_width=True)

#Line
st.header("Line")
fig = px.line(iris, x=species, y=petal_length, color=iris['species'])
st.plotly_chart(fig, use_container_width=True)


