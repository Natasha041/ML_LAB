ML_LAB_05_Clustering_Techniques

#import libraries 

import pandas as pd 
import matplotlib.pyplot as plt

#Read File
df=pd.read_csv('Mall_Customers.csv')

#Data Pre-processing

df.head()
df.info()
df.shape
df.isnull().sum

#Assign x value 

x=df.iloc[:,3:]
x

# Create Plot 

plt.title('Unclustered Data')
plt.xlabel('Annual Income')
plt.ylabel('Spending Score')
plt.scatter(x['Annual Income (k$)'],x['Spending Score (1-100)'])

#Import Cluster 

from sklearn.cluster import KMeans , AgglomerativeClustering

#Calculate the Sum of Squared Error (SSE)

sse = []
for k in range (1,16):
km=KMeans(n_clusters=k)
km.fit_predict(x)
sse.append(km.inertia_)

#Plot Elbow Method 

plt.title('Elbow Method')
plt.xlabel('Value of k')
plt.ylabel('SSE')
plt.grid()
plt.xticks(range(1,16))
plt.plot(range(1,16),sse,marker='.',color='r')

km=km.predict(n_clusters=5)

labels=km.fit_predict(x)
labels

#Import Silhouette Score 

from sklearn.metrics import silhouette_score

silh[]
for k in range (2,16)
km=KMeans(n_clusters=k)
labels=km.fit_predict(x)
score=Silhouette_Score(x,labels)
silh.append(score)

#Plot Silhouette Score 

plt.title('Silhouette Score')
plt.xlabel('Value of k')
plt.ylabel('SSE')
plt.bar(range(1,16),silh,color='g')

#Visualize Clusterd Data

km=KMeans(n_clusters=k)
km.fit_predict(x)
cent=cluster_centers_ 

plt.title('Clustered Data')
plt.xlabel('Annual Income')
plt.ylabel('Spending Score')
plt.scatter(x['Annual Income (k$)'],x['Spending Score (1-100)'],c=labels)
plt.scatter(cent[:,0],cent[:,1],s=100,color='k')

#Data Prediction 
km.predict([[28,90]])

#Visualize Agglomerative Clustering 

agl = AgglomerativeClustering(n_clusters=k)
alabels=agl.fit_predict(x)
alabels

#Plot Agglomerative Clustering

plt.title('Agglomerative Clustering')
plt.xlabel('Annual Income')
plt.ylabel('Spending Score')
plt.scatter(x['Annual Income (k$)'],x['Spending Score (1-100)'],c=alabels)

/******************************************************************************************/

* scatter plot represent?
A: The scatter plot displays the unclustered data. Each point represents a customer, 
with their Annual Income on the x-axis and Spending Score on the y-axis.
This plot helps visualize the overall distribution of customers before applying clustering algorithms.
 
* K-Means is a popular clustering algorithm that partitions data points 
into a predefined number of clusters (k). It iteratively minimizes 
the within-cluster variance (SSE) by assigning data points 
to the closest cluster center (centroid).

* The Silhouette Score (Silhouette Coefficient) evaluates the quality of clustering 
by considering both intra-cluster (cohesion) and inter-cluster (separation) distances. 
It ranges from -1 (poor) to +1 (optimal).


 /******************************************************************************************/

