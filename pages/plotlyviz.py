from app.utils import page_layout
import streamlit as st
import plotly.express as px
from plotly.data import iris, gapminder, stocks


page_layout() 

# Declaring variables from dataframe columns
iris = iris()
sepal_length = iris['sepal_length']
petal_length = iris['petal_length']
species = iris['species']

gapminder = gapminder()
country = gapminder['country']
continent = gapminder['continent']
year = gapminder['year']
lifeExp = gapminder['lifeExp']
pop = gapminder['pop']
gdpPercap = gapminder['gdpPercap']
iso_alpha = gapminder['iso_alpha']
iso_num = gapminder['iso_num']

stocks = stocks()
date = stocks['date']
goog = stocks['GOOG']
aapl = stocks['AAPL']
amzn = stocks['AMZN']
fb = stocks['FB']
nflx = stocks['NFLX']
msft = stocks['MSFT']

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
fig = px.line(stocks,x=date, y=[goog, aapl, amzn, fb, nflx, msft])
st.plotly_chart(fig, use_container_width=True)

#Choropleth
st.header("Choropleth")
fig = px.choropleth(gapminder, locations=iso_alpha, color=lifeExp, hover_name=country)
st.plotly_chart(fig, use_container_width=True)
