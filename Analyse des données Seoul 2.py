import pandas as pd
import numpy as np
import sklearn as sk
import matplotlib.pyplot as plt
import plotly.express as px
from sklearn.cluster import KMeans 

data = pd.read_csv('Original Data\Measurement_info.csv')
items = pd.read_csv('Original Data\Measurement_item_info.csv')
localisation = pd.read_csv('Original Data\Measurement_station_info.csv')

print(data.columns)

# I select the desired columns

data = data[['Item code','Average value','Instrument status','Station code']]
print(data)

pd.to_numeric(data['Average value'])
data['Item code'].apply(str)

data = data.loc[data['Instrument status'] == 0]
data.head(10)

print(data)


# J'affiche les stations sur une map en ajoutant le nom de celles-ci

fig = px.scatter_mapbox(localisation, lat="Latitude", lon="Longitude", hover_name="Station name(district)", hover_data=["Station name(district)"],
                        color_discrete_sequence=["blue"], zoom=9, height=300)
fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()


# JUSQUE ICI OK

#from sklearn.preprocessing import StandardScaler
#X = data.values[:,1:]
#X = np.nan_to_num(X)
#Clus_dataSet = StandardScaler().fit_transform(X)

#clusterNum = 5
#k_means = KMeans(init = "k-means++", n_clusters = clusterNum, n_init = 12)
#k_means.fit(X)
#labels = k_means.labels_
#print(labels)

#data["Clus_km"] = labels
#data.groupby('Clus_km').mean()
#print(data.head(10))