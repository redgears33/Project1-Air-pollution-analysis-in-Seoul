import pandas as pd
import numpy as np
import sklearn as sk
import matplotlib.pyplot as plt
import plotly.express as px

data = pd.read_csv('Original Data\Measurement_info.csv')
items = pd.read_csv('Original Data\Measurement_item_info.csv')
localisation = pd.read_csv('Original Data\Measurement_station_info.csv')

print(data.columns)

# Je sélectionne les colones souhaitées

data = data[['Item code','Average value','Instrument status']]
print(data)

# Je m'assure d'être en numérique et en caractères pour les bonnes colones

pd.to_numeric(data['Average value'])
data['Item code'].apply(str)

# Je filtre les lignes du dataframe ou la sonde fonctionne (=0)

data = data.loc[data['Instrument status'] == 0]

# Je défini une fonction me permettant d'obtenir le taux selon item code 

def gaz_sum(item_code):
    taux = data.loc[data['Item code'] == item_code]
    taux = taux['Average value'].sum()
    return taux

# La boucle for permet d'obtenir automatiquement le taux par item code

list_taux = []
list_code = [1,3,5,6] 
for k in list_code:
    list_taux.append(gaz_sum(item_code = k))

print(list_taux)

# Même chose, mais pour faire un pourcentage

tot = sum(list_taux)
list_perc = []
for taux in list_taux:
    list_perc.append(taux * 100 / tot)

# On produit un pie chart pour visualiser les données avec plotly

import plotly.graph_objects as go

labels = ['S02','N02','CO','O3']
values = list_perc

fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
fig.show()