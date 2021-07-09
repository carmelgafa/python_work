import pandas as pd
import os
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from scipy.spatial import ConvexHull
import numpy as np


script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
rel_path = 'data/Concrete.xls'
abs_file_path = os.path.join(script_dir, rel_path)

df = pd.read_excel(abs_file_path)

colnames = {'Cement (component 1)(kg in a m^3 mixture)' : 'Cement',
    'Blast Furnace Slag (component 2)(kg in a m^3 mixture)' : 'FurnaceSlag',
    'Fly Ash (component 3)(kg in a m^3 mixture)': 'FlyAsh',
    'Water  (component 4)(kg in a m^3 mixture)' : 'Water',
    'Superplasticizer (component 5)(kg in a m^3 mixture)' : 'Superplasticizer',
    'Coarse Aggregate  (component 6)(kg in a m^3 mixture)' : 'CoarseAggregate',
    'Fine Aggregate (component 7)(kg in a m^3 mixture)': 'FineAggregate', 
    'Age (day)' : 'Age',
    'Concrete compressive strength(MPa, megapascals) ' : 'Strength'}

df = df.rename(columns=colnames)


# print(pd.DataFrame.corr(df))

#                     Cement  FurnaceSlag    FlyAsh     Water  Superplasticizer  CoarseAggregate  FineAggregate       Age  Strength
# Cement            1.000000    -0.275193 -0.397475 -0.081544          0.092771        -0.109356      -0.222720  0.081947  0.497833
# FurnaceSlag      -0.275193     1.000000 -0.323569  0.107286          0.043376        -0.283998      -0.281593 -0.044246  0.134824
# FlyAsh           -0.397475    -0.323569  1.000000 -0.257044          0.377340        -0.009977       0.079076 -0.154370 -0.105753
# Water            -0.081544     0.107286 -0.257044  1.000000         -0.657464        -0.182312      -0.450635  0.277604 -0.289613
# Superplasticizer  0.092771     0.043376  0.377340 -0.657464          1.000000        -0.266303       0.222501 -0.192717  0.366102
# CoarseAggregate  -0.109356    -0.283998 -0.009977 -0.182312         -0.266303         1.000000      -0.178506 -0.003016 -0.164928
# FineAggregate    -0.222720    -0.281593  0.079076 -0.450635          0.222501        -0.178506       1.000000 -0.156094 -0.167249
# Age               0.081947    -0.044246 -0.154370  0.277604         -0.192717        -0.003016      -0.156094  1.000000  0.328877
# Strength          0.497833     0.134824 -0.105753 -0.289613          0.366102        -0.164928      -0.167249  0.328877  1.000000


df = df[df.Superplasticizer > 1]

df.hist()

drop_cols = ['FurnaceSlag', 'FlyAsh', 'CoarseAggregate', 'FineAggregate']

df = df.drop(drop_cols, axis=1)

# df=df[1:200]

# plot attack vs defense 
plt.scatter(df.Water, df.Superplasticizer, alpha = 0.6, s=10)
plt.show()



number_clusters = 3

# k means - divide in 3 clusters
kmeans = KMeans(n_clusters=number_clusters, random_state=0)
# add column called cluster to contain cluster of item it will have a value of 0,1 or 2
df['cluster'] = kmeans.fit_predict(df[['Water', 'Superplasticizer']])


# get centroids
centroids = kmeans.cluster_centers_

# array of 3 items containing the x value of the centroid
cen_x = [i[0] for i in centroids] 
# array of 3 items containing the y value of the centroid
cen_y = [i[1] for i in centroids]

keys = range(number_clusters)

## add to df - 2 columns for x and y value of centroid
df['cen_x'] = df.cluster.map(dict(zip(keys, cen_x)))
df['cen_y'] = df.cluster.map(dict(zip(keys, cen_y)))

print(df.head())

# define and map colors for centroids
# colors = ['#DF2020', '#81DF20', '#2095DF', '#a8a832', '#a8329b']
import matplotlib.cm as cm

colors = cm.rainbow(np.linspace(0, 1, number_clusters))



df['c'] = df.cluster.map(dict(zip(keys, colors)))

plt.scatter(df.Water, df.Superplasticizer, c=df.c, alpha = 0.6)
plt.show()


# add another dimension - speed as size
plt.scatter(df.Water, df.Superplasticizer, c=df.c, s=df.Age, alpha = 0.6)
plt.show()


df_1 = df[df.cluster == 1]

plt.scatter(df_1.Superplasticizer, df_1.Strength, alpha = 0.6, s=10)
plt.show()
