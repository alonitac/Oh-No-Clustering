from matplotlib import pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
import numpy as np
import json

# recommended reading https://joernhees.de/blog/2015/08/26/scipy-hierarchical-clustering-and-dendrogram-tutorial/

if __name__ == '__main__':

    dolars_pelged = []  # each elment is a tuple:  (<id>, <DolarsPelged>)

    # read & clean the json
    with open('ex1.json') as f:
        data = json.load(f)
        dolars_pelged += [(x['id'], x['DolarsPelged']) for x in data['records']['record'] if x['Currency'] == "$"]

    # create a matrix of (1, n) of points
    n = len(dolars_pelged)
    points = np.array([d[1] for d in dolars_pelged], ndmin=2)

    # perform hierarchical clustering (divisive)
    # I use centroid methods. see here list of methods: https://docs.scipy.org/doc/scipy/reference/generated/scipy.cluster.hierarchy.linkage.html#scipy.cluster.hierarchy.linkage
    levels = linkage(points.T, 'centroid')

    # print(levels[0]) - information about level 0 of the tree. each level is a merge between 2 clusters.
    # the following will be printed:
    # [cluster1 index , cluster2 index, distance between clusters, number of points in the merged cluster]

    plt.plot(range(n-1), levels[:, 2])
    plt.title('distances throughout the algorithm')
    plt.xlabel('Level')
    plt.ylabel('Distance of Centroids')
    plt.show()

