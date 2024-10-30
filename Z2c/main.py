import heapq
import math
import random

from fontTools.misc.cython import returns
from matplotlib.streamplot import OutOfBounds

from Z2c.point import minDistance
from Z2c.visuals import visualize, visualizeList
from cluster import Cluster
from point import Point



### doesn't work like that
def compress(value, compression, min, max) -> int:
    index = round((value - min) / compression)
    return clamp(index, 0, math.ceil((max - min)/ compression)-1)


def addToGrid(value, grid: list, min_offset, max_offset):
    # if isinstance(value, Point):
    #     grid[compress(value.x, compression)][compress(value.y, compression)].add(value)
    if isinstance(value, Cluster):
        grid[compress(value.centroid.x, compression, min_offset, max_offset)][compress(value.centroid.y, compression, min_offset, max_offset)].add(value)
    elif isinstance(value, (list)):
        for cluster in value:
            grid[compress(cluster.centroid.x, compression, min_offset, max_offset)][compress(cluster.centroid.y, compression, min_offset, max_offset)].append(cluster)

def clamp(value, minimum, maximum):
    if (value < minimum):
        value = minimum
    if (value > maximum):
        value = maximum
    return value

def updateGrid(sub_grid, minheap: list):
    result = False
    merged_clusters = set()
    while True:
        try:
            p, pair = heapq.heappop(minheap)
        except IndexError:
            break

        if (pair[0] in merged_clusters or pair[1] in merged_clusters): return result
        merged_clusters.add(pair[0])
        merged_clusters.add(pair[1])

        try:
            new_c = Cluster.merge(pair[0], pair[1], LIMIT)

            sub_grid.remove(pair[0])
            sub_grid.remove(pair[1])
            sub_grid.append(new_c)

            result = True

        except OutOfBounds:
            break

    return result

def updateTheFullGrid(GRID):
    print("Updating the full grid")
    allClusters = []

    for rows in GRID:
        for squares in rows:
            allClusters.extend(squares)

    ### how the fuk do I stop this
    while True:
        print(".", end="")
        minheap = minDistance(allClusters)
        merged_clusters = set()
        try:
            priority, pair = heapq.heappop(minheap)
            new_c = Cluster.merge(pair[0], pair[1], LIMIT)
            allClusters.remove(pair[0])
            allClusters.remove(pair[1])
            allClusters.append(new_c)

        except IndexError:
            break
        except OutOfBounds:
            break

        merged_clusters.add(pair[0])
        merged_clusters.add(pair[1])

        while True:
            try:
                priority, pair = heapq.heappop(minheap)
            except IndexError:
                break

            if (pair[0] in merged_clusters or pair[1] in merged_clusters): break
            merged_clusters.add(pair[0])
            merged_clusters.add(pair[1])

            try:
                new_c = Cluster.merge(pair[0], pair[1], LIMIT)

                allClusters.remove(pair[0])
                allClusters.remove(pair[1])
                allClusters.append(new_c)
            except OutOfBounds:
                break
    return allClusters


if __name__ == '__main__':

    LIMIT = 500
    min = -5000
    max = 5000
    max_points = 20000
    offset_min = -100
    offset_max = 100
    compression = 100
    size = int((max - min)/compression)


    GRID = [[list() for _ in range(size)] for _ in range(size)]
    allClusters = [ Cluster(Point(random.randint(min, max), random.randint(min, max))) for _ in range(20)]

    while (len(allClusters) <= max_points):
        p = random.choice(allClusters)
        n_p = Point(clamp((random.randint(offset_min, offset_max) + p.centroid.x), min, max), clamp((random.randint(offset_min, offset_max) + p.centroid.y), min, max))
        allClusters.append(Cluster(n_p))

    addToGrid(allClusters, GRID, min, max)


    for rows in GRID:
        for squares in rows:
            while len(squares) > 3:
                if not updateGrid(squares, minDistance(squares)):
                    break
                print(".", end="")
        print("")

    visualizeList(updateTheFullGrid(GRID))
    # visualize(GRID)
