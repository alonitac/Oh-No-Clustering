from matplotlib import pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage, fcluster
import numpy as np
import json


if __name__ == '__main__':

    dolars_pelged = []  # each element is a tuple:  (<id>, <DolarsPelged>)

    # read & clean the json
    with open('ex1.json') as f:
        data = json.load(f)
        dolars_pelged += [(x['id'], x['DolarsPelged']) for x in data['records']['record'] if x['Currency'] == "$"]

    # create a matrix of (1, n) of points
    n = len(dolars_pelged)
    points = np.array([d[1] for d in dolars_pelged], ndmin=2)

    # show the points
    plt.figure()
    plt.title('The points')
    plt.scatter(points, [0] * points.shape[1])
    plt.show()

    # perform hierarchical clustering (divisive)
    levels = linkage(points.T, 'centroid')     # centroids the closest, part (a)
    # levels = linkage(points.T, 'complete')     # smallest diameter, part (b)

    # plot distances as function of level
    plt.plot(range(n-1), levels[:, 2])
    plt.title('Distance between the Clusters merged in that Step')
    plt.xlabel('Level')
    plt.ylabel('Distance')
    plt.show()

    # plot how many clusters for certain distance
    m = levels[-1, 2]  # last merging distance

    plt.title('Number of clusters for m={}'.format(int(m)))
    plt.xlabel('Index')
    plt.ylabel('Distance')
    dendrogram(levels)
    plt.axhline(y=0.1 * m, color='black', ls='--', label='4 clusters for 0.1m')
    plt.axhline(y=0.5 * m, color='red', ls='--', label='2 clusters for 0.5m')
    plt.legend()
    plt.show()

    # retrieve the clusters
    k = 5
    clusters = fcluster(levels, k, criterion='maxclust')
    plt.figure()
    plt.title('The clusters for k={}'.format(5))
    plt.scatter(points, [0]*points.shape[1], c=clusters, cmap='Set1')
    plt.show()
