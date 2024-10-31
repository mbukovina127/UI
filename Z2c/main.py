import random

from Z2c.matrix import Matrix
from Z2c.pltly import plotScatter
from cluster_c import Cluster_C
from point import Point


def clamp(value, minimum, maximum):
    if (value < minimum) or (value > maximum):
        return True
    return value

if __name__ == '__main__':

    LIMIT = 500
    min, max = -5000, 5000
    max_points = 5000
    offset_min, offset_max = -100, 100

    allClusters = [Cluster_C(Point(clamp(random.randint(min, max), min, max), clamp(random.randint(min, max), min, max))) for _ in range(20)]

    while (len(allClusters) <= max_points):
        p = random.choice(allClusters)
        x = min -1
        while clamp(x, min, max):
            x = (random.randint(offset_min, offset_max) + p.center.x)
        y = min -1
        while clamp(y, min, max):
            y = (random.randint(offset_min, offset_max) + p.center.y)
        n_p = Point(x, y)
        allClusters.append(Cluster_C(n_p))

    print("Building Matrix")
    MTRX = Matrix(allClusters)
    print("Aggregate clusterring", end="")
    while MTRX.aggregate(): print(".", end="")
    plotScatter(MTRX.clusters)