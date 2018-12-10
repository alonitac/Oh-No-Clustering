## Homework #2: Similar items, Clustering, Community Detection

### Problem 3

**(a) **

![syn_data_uniform](/home/franzi/briedenCloud/Studium/3Semester/DataScience/homework/Oh-No-Clustering/syn_data_uniform.png)

**(b)**

![syn_data_gaussian](/home/franzi/briedenCloud/Studium/3Semester/DataScience/homework/Oh-No-Clustering/syn_data_gaussian.png)
<div style="page-break-after: always;"></div>
**(c)**

![syn_data_3gaussian](/home/franzi/briedenCloud/Studium/3Semester/DataScience/homework/Oh-No-Clustering/syn_data_3gaussian.png)

**(d)**

![syn_data_circle](/home/franzi/briedenCloud/Studium/3Semester/DataScience/homework/Oh-No-Clustering/syn_data_circle.png)
<div style="page-break-after: always;"></div>
**(e)**

![syn_data_AF](/home/franzi/briedenCloud/Studium/3Semester/DataScience/homework/Oh-No-Clustering/syn_data_AF.png)



### Problem 4

For hierarchical clustering and the plot of the dendrogram we use the package `scipy.cluster.hierarchy`. Function `linkage` provides the hierarchical clustering algorithm for different methods. We use `method='centroid'` in part (a) and `method='complete'` in part (b).  Function `dendrogram` is used to plot the dendrogram. 

**(a) merge clusters with the closest centroids**
<center>
<img src="/home/franzi/briedenCloud/Studium/3Semester/DataScience/homework/Oh-No-Clustering/centroid_distances.png" width="480">
<img src="/home/franzi/briedenCloud/Studium/3Semester/DataScience/homework/Oh-No-Clustering/dendrogram1.png" width="480">
</center>

The Dendrogram shows that we would get 4 clusters if we decide to stop clustering at a distange of 0.1m and 2 clusters if we decide to stop at 0.5m. 



**(b) merge clusters so that the new diameter is the smallest among all options**
<center>
<img src="/home/franzi/briedenCloud/Studium/3Semester/DataScience/homework/Oh-No-Clustering/diameter_distances.png" width="480">
<img src="/home/franzi/briedenCloud/Studium/3Semester/DataScience/homework/Oh-No-Clustering/dendrogram2.png" width="480">
</center>
The Dendrogram shows that with this method we would get 5 clusters if we decide to stop clustering at a distange of 0.1m and 2 clusters if we decide to stop at 0.5m. 