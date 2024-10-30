import random

from matplotlib.streamplot import OutOfBounds
from numpy.matrixlib.defmatrix import matrix

from Z2c.point import clusterDistance
from Z2c.visuals import visualizeList
from cluster import Cluster
from point import Point
import numpy as np


def clamp(value, minimum, maximum):
    if (value < minimum):
        value = minimum
    if (value > maximum):
        value = maximum
    return value


def makeMatrix(allClusters):
    size = len(allClusters)
    matrix = np.zeros((size, size))
    print(size)
    for i, st in enumerate(allClusters):
        for j, nd in enumerate(allClusters):
            matrix[i, j] = clusterDistance(st,nd)
    return matrix


def findMinDist(Matrix):
    mask = np.where(np.eye(len(Matrix)), np.inf, Matrix)
    min_index = np.unravel_index(np.argmin(mask), Matrix.shape)
    return min_index

def removeCluster(index: int, matrix):
    print(matrix.shape)
    matrix = np.delete(matrix, index, axis=0)
    matrix = np.delete(matrix, index, axis=1)
    print("del", end="")
    print(matrix.shape)
    return matrix

def addCluster(new_cluster, allClusters, Matrix):
    allClusters.append(new_cluster)
    size = len(allClusters)
    print(size)
    print(Matrix.shape)
    new_dist = np.array([clusterDistance(new_cluster, nd) for nd in allClusters[:-1]])

    Matrix = np.pad(Matrix, ((0, 1), (0, 1)), mode='constant', constant_values=0)
    Matrix[-1, :-1] = new_dist
    Matrix[:-1, -1] = new_dist
    return Matrix


def aggregate(allClusters, MTRX):
    i, j = findMinDist(Matrix=MTRX)

    try:
        new_c = Cluster.merge(allClusters[i], allClusters[j], 500)
    except OutOfBounds:
        return False
    if i > j:
        i, j = j, i
    MTRX = removeCluster(j, removeCluster(i, MTRX))
    del allClusters[j]
    del allClusters[i]

    MTRX = addCluster(new_c, allClusters, MTRX)
    return True

if __name__ == '__main__':

    LIMIT = 500
    min = -5000
    max = 5000
    max_points = 1000
    offset_min = -100
    offset_max = 100
    compression = 10
    size = int((max - min)/compression)

    allClusters = [Cluster(Point(clamp(random.randint(min, max), min, max), clamp(random.randint(min, max), min, max))) for _ in range(20)]

    while (len(allClusters) <= max_points):
        p = random.choice(allClusters)
        n_p = Point(clamp((random.randint(offset_min, offset_max) + p.centroid.x), min, max), clamp((random.randint(offset_min, offset_max) + p.centroid.y), min, max))
        allClusters.append(Cluster(n_p))


    MTRX = makeMatrix(allClusters)

    while aggregate(allClusters, MTRX): print(".", end="")
    visualizeList(allClusters, True)