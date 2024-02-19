import pandas as pd
import os
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from scipy.spatial import ConvexHull
import numpy as np


script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
rel_path = 'data/Pokemon.csv'
abs_file_path = os.path.join(script_dir, rel_path)

df = pd.read_csv(abs_file_path)

# prepare data

# identify the three types. the df types will have a single column with values True / False
types = df['Type 1'].isin(['Grass', 'Fire', 'Water'])

# identfy columns to drop
drop_cols = ['Type 1', 'Type 2', 'Generation', 'Legendary', 'Number']


# drop columns from the fields having their 'types' as true. set this result as the dataframe to work with
df = df[types].drop(columns = drop_cols)

print(df.head())

# plot attack vs defense 
plt.scatter(df.Attack, df.Defense, alpha = 0.6, s=10)
plt.show()


# k means - divide in 3 clusters
kmeans = KMeans(n_clusters=5, random_state=0)
# add column called cluster to contain cluster of item it will have a value of 0,1 or 2
df['cluster'] = kmeans.fit_predict(df[['Attack', 'Defense']])

# get centroids
centroids = kmeans.cluster_centers_

# array of 3 items containing the x value of the centroid
cen_x = [i[0] for i in centroids] 
# array of 3 items containing the y value of the centroid
cen_y = [i[1] for i in centroids]

print(cen_x, cen_y)

## add to df - 2 columns for x and y value of centroid
df['cen_x'] = df.cluster.map({0:cen_x[0], 1:cen_x[1], 2:cen_x[2], 3:cen_x[3], 4:cen_x[4]})
df['cen_y'] = df.cluster.map({0:cen_y[0], 1:cen_y[1], 2:cen_y[2], 3:cen_y[3], 4:cen_y[4]})

print(df.head())

# define and map colors for centroids
colors = ['#DF2020', '#81DF20', '#2095DF', '#a8a832', '#a8329b']
df['c'] = df.cluster.map({0:colors[0], 1:colors[1], 2:colors[2], 3:colors[3], 4:colors[4]})

plt.scatter(df.Attack, df.Defense, c=df.c, alpha = 0.6)
plt.show()


# add another dimension - speed as size
plt.scatter(df.Attack, df.Defense, c=df.c, s=df.Speed, alpha = 0.6)
plt.show()


#####PLOT#####
fig, ax = plt.subplots(1, figsize=(8,8))
# plot data
plt.scatter(df.Attack, df.Defense, c=df.c, alpha = 0.6, s=10)

# create a list of legend elements
## markers / records
legend_elements = [Line2D([0], [0], marker='o', color='w', label=f'Cluster {i+1}', 
               markerfacecolor=mcolor, markersize=5) for i, mcolor in enumerate(colors)]

# plot legend
plt.legend(handles=legend_elements, loc='upper right')

# title and labels
plt.title('Pokemon Stats\n', loc='left', fontsize=22)
plt.xlabel('Attack')
plt.ylabel('Defense')

plt.show()




####putting in even more information####

fig, ax = plt.subplots(1, figsize=(8,8))

# plot data
plt.scatter(df.Attack, df.Defense, c=df.c, alpha = 0.6, s=10)

# plot centroids
plt.scatter(cen_x, cen_y, marker='^', c=colors, s=70)

# plot Attack mean
plt.plot([df.Attack.mean()]*2, [0,200], color='black', lw=0.5, linestyle='--')
plt.xlim(0,200)

# plot Defense mean
plt.plot([0,200], [df.Defense.mean()]*2, color='black', lw=0.5, linestyle='--')
plt.ylim(0,200)

# create a list of legend elemntes
## average line
legend_elements = [Line2D([0], [0], color='black', lw=0.5, linestyle='--', label='Average')]

## markers / records
cluster_leg = [Line2D([0], [0], marker='o', color='w', label=f'Cluster {i+1}', 
               markerfacecolor=mcolor, markersize=5) for i, mcolor in enumerate(colors)]
## centroids
cent_leg = [Line2D([0], [0], marker='^', color='w', label=f'Centroid - C{i+1}', 
            markerfacecolor=mcolor, markersize=10) for i, mcolor in enumerate(colors)]

# add all elements to the same list
legend_elements.extend(cluster_leg)
legend_elements.extend(cent_leg)

# plot legend
plt.legend(handles=legend_elements, loc='upper right', ncol=2)

# title and labels
plt.title('Pokemon Stats\n', loc='left', fontsize=22)
plt.xlabel('Attack')
plt.ylabel('Defense')

plt.show()



###plot lines###
fig, ax = plt.subplots(1, figsize=(8,8))

# plot data
plt.scatter(df.Attack, df.Defense, c=df.c, alpha = 0.6, s=10)

# plot centroids
plt.scatter(cen_x, cen_y, marker='^', c=colors, s=70)

# plot lines
for idx, val in df.iterrows():
    x = [val.Attack, val.cen_x,]
    y = [val.Defense, val.cen_y]
    plt.plot(x, y, c=val.c, alpha=0.2)


# plot Attack mean
plt.plot([df.Attack.mean()]*2, [0,200], color='black', lw=0.5, linestyle='--')
plt.xlim(0,200)

# plot Defense mean
plt.plot([0,200], [df.Defense.mean()]*2, color='black', lw=0.5, linestyle='--')
plt.ylim(0,200)


# legend
legend_elements = [Line2D([0], [0], marker='o', color='w', label='Cluster {}'.format(i+1), 
                   markerfacecolor=mcolor, markersize=5) for i, mcolor in enumerate(colors)]

legend_elements.extend([Line2D([0], [0], marker='^', color='w', label='Centroid - C{}'.format(i+1), 
            markerfacecolor=mcolor, markersize=10) for i, mcolor in enumerate(colors)])

legend_elements.extend([Line2D([0], [0], color='black', lw=0.5, linestyle='--', label='Average')])



# legend_elements.extend(cent_leg)
plt.legend(handles=legend_elements, loc='upper right', ncol=1)

# x and y limits
plt.xlim(0,200)
plt.ylim(0,200)

# title and labels
plt.title('Pokemon Stats\n', loc='left', fontsize=22)
plt.xlabel('Attack')
plt.ylabel('Defense')

plt.show()


### convex hull ###

fig, ax = plt.subplots(1, figsize=(8,8))

# plot data
plt.scatter(df.Attack, df.Defense, c=df.c, alpha = 0.6, s=10)

# plot centroids
plt.scatter(cen_x, cen_y, marker='^', c=colors, s=70)

# plot lines
for idx, val in df.iterrows():
    x = [val.Attack, val.cen_x,]
    y = [val.Defense, val.cen_y]
    plt.plot(x, y, c=val.c, alpha=0.2)


# draw enclosure
for i in df.cluster.unique():
    points = df[df.cluster == i][['Attack', 'Defense']].values
    # get convex hull
    hull = ConvexHull(points)
    # get x and y coordinates
    # repeat last point to close the polygon
    x_hull = np.append(points[hull.vertices,0],
                       points[hull.vertices,0][0])
    y_hull = np.append(points[hull.vertices,1],
                       points[hull.vertices,1][0])
    # plot shape
    plt.fill(x_hull, y_hull, alpha=0.3, c=colors[i])


# plot Attack mean
plt.plot([df.Attack.mean()]*2, [0,200], color='black', lw=0.5, linestyle='--')
plt.xlim(0,200)

# plot Defense mean
plt.plot([0,200], [df.Defense.mean()]*2, color='black', lw=0.5, linestyle='--')
plt.ylim(0,200)


# legend
legend_elements = [Line2D([0], [0], marker='o', color='w', label='Cluster {}'.format(i+1), 
                   markerfacecolor=mcolor, markersize=5) for i, mcolor in enumerate(colors)]

legend_elements.extend([Line2D([0], [0], marker='^', color='w', label='Centroid - C{}'.format(i+1), 
            markerfacecolor=mcolor, markersize=10) for i, mcolor in enumerate(colors)])

legend_elements.extend([Line2D([0], [0], color='black', lw=0.5, linestyle='--', label='Average')])



# legend_elements.extend(cent_leg)
plt.legend(handles=legend_elements, loc='upper right', ncol=1)

# x and y limits
plt.xlim(0,200)
plt.ylim(0,200)

# title and labels
plt.title('Pokemon Stats\n', loc='left', fontsize=22)
plt.xlabel('Attack')
plt.ylabel('Defense')

plt.show()
