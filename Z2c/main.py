import random

from Z2c.matrix import Matrix
from Z2c.visuals import visualizeList
from cluster import Cluster
from point import Point


def clamp(value, minimum, maximum):
    if (value < minimum):
        value = minimum
    if (value > maximum):
        value = maximum
    return value

if __name__ == '__main__':

    LIMIT = 500
    min = -5000
    max = 5000
    max_points = 5000
    offset_min = -100
    offset_max = 100
    compression = 10
    size = int((max - min)/compression)

    allClusters = [Cluster(Point(clamp(random.randint(min, max), min, max), clamp(random.randint(min, max), min, max))) for _ in range(20)]

    while (len(allClusters) <= max_points):
        p = random.choice(allClusters)
        n_p = Point(clamp((random.randint(offset_min, offset_max) + p.centroid.x), min, max), clamp((random.randint(offset_min, offset_max) + p.centroid.y), min, max))
        allClusters.append(Cluster(n_p))

    print("Building Matrix")
    MTRX = Matrix(allClusters)
    print("Aggregate clusterring", end="")
    while MTRX.aggregate(): print(".", end="")
    visualizeList(allClusters, True)