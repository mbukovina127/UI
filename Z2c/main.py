import random

from matplotlib.streamplot import OutOfBounds

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
    Matrix = [[0 for _ in range(len(allClusters))] for _ in range(len(allClusters))]
    # min = 10000* math.sqrt(2)
    # pair = (0,0)
    for i, st in enumerate(allClusters):
        for j, nd in enumerate(allClusters):
            Matrix[i][j] = clusterDistance(st,nd)
            # if Matrix[i][j] < min:
            #     min = Matrix[i][j]
            #     pair = (i,j)
    return Matrix


def findMinDist(Matrix):
    min = 12000
    pair = (0,0)
    for i in range(len(Matrix)):
        for j in range (i+1, len(Matrix)):
            if Matrix[i][j] < min:
                min = Matrix[i][j]
                pair = (i,j)
    return pair


def removeCluster(index: int, matrix):
    matrix.pop(index)
    for i in range(len(matrix)):
        matrix[i].pop(index)

def addCluster(cluster, allClusters, matrix):
    matrix.append([])
    for i in range(len(allClusters)):
        matrix[-1].append(clusterDistance(cluster, allClusters[i]))
        matrix[i].append(clusterDistance(cluster, allClusters[i]))
    matrix[-1].append(0)


def aggregate(allClusters, MTRX):
    pair = findMinDist(Matrix=MTRX)

    try:
        new_c = Cluster.merge(allClusters[pair[0]], allClusters[pair[1]], 500)
    except OutOfBounds:
        return False
    if pair[0] > pair[1]:
        removeCluster(pair[0], MTRX)
        removeCluster(pair[1], MTRX)
        allClusters.pop(pair[0])
        allClusters.pop(pair[1])
    else:
        removeCluster(pair[1], MTRX)
        removeCluster(pair[0], MTRX)
        allClusters.pop(pair[1])
        allClusters.pop(pair[0])

    addCluster(new_c, allClusters, MTRX)
    allClusters.append(new_c)
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