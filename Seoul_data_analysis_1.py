import pandas as pd
import numpy as np
import sklearn as sk
import matplotlib.pyplot as plt
import plotly.express as px

data = pd.read_csv('Original Data\Measurement_info.csv')
items = pd.read_csv('Original Data\Measurement_item_info.csv')
localisation = pd.read_csv('Original Data\Measurement_station_info.csv')

print(data.columns)

# I select the desired columns

data = data[['Item code','Average value','Instrument status']]
print(data)

# I make sure to be in numeric and in characters for the right columns

pd.to_numeric(data['Average value'])
data['Item code'].apply(str)

# I filter the dataframe lines where the probe works (= 0)

data = data.loc[data['Instrument status'] == 0]

# I define a function allowing me to obtain the rate according to item code 

def gaz_sum(item_code):
    taux = data.loc[data['Item code'] == item_code]
    taux = taux['Average value'].sum()
    return taux

# The for loop automatically obtains the rate per item code

list_taux = []
list_code = [1,3,5,6] 
for k in list_code:
    list_taux.append(gaz_sum(item_code = k))

print(list_taux)

# Same thing, but to make a percentage

tot = sum(list_taux)
list_perc = []
for taux in list_taux:
    list_perc.append(taux * 100 / tot)

# We produce a pie chart to visualize the data with plotly

import plotly.graph_objects as go

labels = ['S02','N02','CO','O3']
values = list_perc

fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
fig.show()
