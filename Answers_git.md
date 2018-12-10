## Homework #2: Similar items, Clustering, Community Detection

### Problem 3

<center>
<img src="https://github.com/alonitac/Oh-No-Clustering/blob/master/syn_data_uniform.png">
<img src="https://github.com/alonitac/Oh-No-Clustering/blob/master/syn_data_gaussian.png">
<img src="https://github.com/alonitac/Oh-No-Clustering/blob/master/syn_data_3gaussian.png">
<img src="https://github.com/alonitac/Oh-No-Clustering/blob/master/syn_data_circle.png">
<img src="https://github.com/alonitac/Oh-No-Clustering/blob/master/syn_data_AF.png">
</center>
<div style="page-break-after: always;"></div>

### Problem 4

For hierarchical clustering and the plot of the dendrogram we use the package `scipy.cluster.hierarchy`. Function `linkage` provides the hierarchical clustering algorithm for different methods. We use `method='centroid'` in part (a) and `method='complete'` in part (b).  Function `dendrogram` is used to plot the dendrogram. 

**(a) merge clusters with the closest centroids**

<center>
<img src="https://github.com/alonitac/Oh-No-Clustering/blob/master/centroid_distances.png" width="480">
<img src="https://github.com/alonitac/Oh-No-Clustering/blob/master/dendrogram1.png" width="480">
</center>


The Dendrogram shows that we would get 4 clusters if we decide to stop clustering at a distange of 0.1m and 2 clusters if we decide to stop at 0.5m. 
<div style="page-break-after: always;"></div>

**(b) merge clusters so that the new diameter is the smallest among all options**

<center>
<img src="https://github.com/alonitac/Oh-No-Clustering/blob/master/diameter_distances.png" width="480">
<img src="https://github.com/alonitac/Oh-No-Clustering/blob/master/dendrogram2.png" width="480">
</center>

The Dendrogram shows that with this method we would get 5 clusters if we decide to stop clustering at a distange of 0.1m and 2 clusters if we decide to stop at 0.5m. 