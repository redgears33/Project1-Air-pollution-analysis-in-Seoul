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

from sklearn.preprocessing import StandardScaler
X = data.values[:,1:]
X = np.nan_to_num(X)
Clus_dataSet = StandardScaler().fit_transform(X)
Clus_dataSet

clusterNum = 5
k_means = KMeans(init = "k-means++", n_clusters = clusterNum, n_init = 12)
k_means.fit(X)
labels = k_means.labels_
print(labels)

data["Clus_km"] = labels
data.groupby('Clus_km').mean()
print(data.head(10))

import plotly.express as px
data = px.data.iris()
fig = px.scatter_3d(data, x='sepal_length', y='sepal_width', z='petal_width',
              color='species')
fig.show()

# JUSQUE ICI OK
# Je génère une map de Seoul en HTML

import folium
c= folium.Map(location=[37.566535, 126.9779692])
c.save('MAP_SEOUL.html')

# Reste à trouver comment avoir les colones lat et long en fonction du station code