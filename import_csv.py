import csv
import pandas as pd
import petl as etl
import plotly.express as px
file = pd.read_csv(r"C:\\Users\\devinhill\\Downloads\\archive\\US counties - education vs per capita personal income - results-20221227-213216.csv")
graph = px.scatter(file, 
x='per_capita_personal_income_2020',
y='bachelor_degree_percentage_2015_2019', 
trendline='ols',
title='US Degree vs Income Per Capita 2015-2020')
graph.show()
