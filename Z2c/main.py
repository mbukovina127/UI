import random

from Z2c.matrix import Matrix_C, Matrix_M
from Z2c.pltly import plotScatter
from cluster import Cluster_C, Cluster_M
from point import Point


def clamp(value, minimum, maximum):
    if (value < minimum) or (value > maximum):
        return True
    return False

if __name__ == '__main__':

    LIMIT = 500
    min, max = -5000, 5000
    max_points = 5000
    offset_min, offset_max = -100, 100

    allClusters = []
    while (len(allClusters) <= 20):
        x = min -10
        while clamp(x, min, max):
            x = random.randint(min, max)
        y = min -10
        while clamp(y, min, max):
            y = random.randint(min, max)
        allClusters.append(Cluster_C(Point(x, y)))
        # allClusters.append(Cluster_M(Point(x, y)))

    while (len(allClusters) <= max_points):
        p = random.choice(allClusters)
        x = min -10
        while clamp(x, min, max):
            x = (random.randint(offset_min, offset_max) + p.center.x)
        y = min -10
        while clamp(y, min, max):
            y = (random.randint(offset_min, offset_max) + p.center.y)
        n_p = Point(x, y)
        ###centroid
        allClusters.append(Cluster_C(n_p))
        ###medoid
        # allClusters.append(Cluster_M(n_p))

    print("Building Matrix")
    ###centroid
    MTRX = Matrix_C(allClusters, LIMIT)
    ###medoid
    # MTRX = Matrix_M(allClusters, LIMIT)
    print("Aggregate clustering ", end="")
    print("by centroids", end="")
    # print("by medoids", end="")
    while MTRX.aggregate(): print(".", end="")
    plotScatter(MTRX.clusters)