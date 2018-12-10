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
<div style="page-break-after: always;"></div>



### Problem 4

For hierarchical clustering and the plot of the dendrogram we use the package `scipy.cluster.hierarchy`. Function `linkage` provides the hierarchical clustering algorithm for different methods. We use `method='centroid'` in part (a) and `method='complete'` in part (b).  Function `dendrogram` is used to plot the dendrogram. 

**(a) merge clusters with the closest centroids**
<center>
<img src="/home/franzi/briedenCloud/Studium/3Semester/DataScience/homework/Oh-No-Clustering/centroid_distances.png" width="480">
<img src="/home/franzi/briedenCloud/Studium/3Semester/DataScience/homework/Oh-No-Clustering/dendrogram1.png" width="480">
</center>
The Dendrogram shows that we would get 4 clusters if we decide to stop clustering at a distange of 0.1m and 2 clusters if we decide to stop at 0.5m. 
<div style="page-break-after: always;"></div>

**(b) merge clusters so that the new diameter is the smallest among all options**
<center>
<img src="/home/franzi/briedenCloud/Studium/3Semester/DataScience/homework/Oh-No-Clustering/diameter_distances.png" width="480">
<img src="/home/franzi/briedenCloud/Studium/3Semester/DataScience/homework/Oh-No-Clustering/dendrogram2.png" width="480">
</center>
The Dendrogram shows that with this method we would get 5 clusters if we decide to stop clustering at a distange of 0.1m and 2 clusters if we decide to stop at 0.5m. 
<div style="page-break-after: always;"></div>

**Comparison**

When we evaluate the Dendograms of the clustering methods, we conclude in both cases that our data is best represented by k=5 clusters.
In this task we have the special case of just one dimensional data that we can visualize easily and compare the outcome with our expectation (since humans are incredibly good in clustering easy patterns).

In the case of centroid clustering the clusters represent the structure of our data pretty well. 

<center>
<img src="/home/franzi/briedenCloud/Studium/3Semester/DataScience/homework/Oh-No-Clustering/clusters1.png" width="480">
</center>
Whereas in the diameter case, the algorithm assigns data points to clusters that don't seem to make sense from our (visual) intuition. 
<center>
<img src="/home/franzi/briedenCloud/Studium/3Semester/DataScience/homework/Oh-No-Clustering/clusters2.png" width="480">
</center>
This shows that the choice of method and how you measure the distance always depends on the question that is asked about the data. 