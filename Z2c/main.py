import heapq
import math
import random

from fontTools.misc.cython import returns
from matplotlib.streamplot import OutOfBounds
from numpy.ma.core import indices

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
    try:
        p, pair = heapq.heappop(minheap)
        new_c = Cluster.merge(pair[0], pair[1], LIMIT)

        sub_grid.remove(pair[0])
        sub_grid.remove(pair[1])
        sub_grid.append(new_c)

        result = True
    except OutOfBounds:
        return
    except IndexError:
        return

    return result

def updateTheFullGrid(GRID):
    print("Updating the full grid")
    allClusters = []

    for rows in GRID:
        for squares in rows:
            allClusters.extend(squares)

    ### how the fuk do I stop this
    finalClusters = []
    while True:
        print(".", end="")
        minheap = minDistance(allClusters)
        try:
            priority, pair = heapq.heappop(minheap)
            new_c = Cluster.merge(pair[0], pair[1], LIMIT)
            allClusters.remove(pair[0])
            allClusters.remove(pair[1])
            allClusters.append(new_c)

        except OutOfBounds:
            finalClusters.append(pair[0])
            finalClusters.append(pair[1])
            allClusters.remove(pair[0])
            allClusters.remove(pair[1])
            continue
        except IndexError:
            return finalClusters

def binaryReduce(ogsize: int, GRID):
    print("binary reduction")
    new_size = ogsize // 2
    BiggerGrid = [[[] for _ in range(new_size)] for _ in range(new_size)]
    for i in range(0, len(GRID) - 1, 2):
        for j in range(0, len(GRID[i]) - 1, 2):
            k, l = (i // 2, j // 2)
            print(i,j,k,l)
            BiggerGrid[k][l].extend(GRID[i][j])
            BiggerGrid[k][l].extend(GRID[i][j + 1])
            BiggerGrid[k][l].extend(GRID[i][j + 1])
            BiggerGrid[k][l].extend(GRID[i + 1][j + 1])

    return BiggerGrid, new_size


if __name__ == '__main__':

    LIMIT = 500
    min = -5000
    max = 5000
    max_points = 20000
    offset_min = -100
    offset_max = 100
    compression = 10
    size = int((max - min)/compression)


    GRID = [[list() for _ in range(size)] for _ in range(size)]
    allClusters = [ Cluster(Point(random.randint(min, max), random.randint(min, max))) for _ in range(20)]

    while (len(allClusters) <= max_points):
        p = random.choice(allClusters)
        n_p = Point(clamp((random.randint(offset_min, offset_max) + p.centroid.x), min, max), clamp((random.randint(offset_min, offset_max) + p.centroid.y), min, max))
        allClusters.append(Cluster(n_p))

    addToGrid(allClusters, GRID, min, max)


    while True:
        print("reducing clusters")
        for rows in GRID:
            for squares in rows:
                while len(squares) > 5:
                    if not updateGrid(squares, minDistance(squares)):
                        break
                    print(".", end="")
            print("")

        ###binary reduction
        if (size <= 4):
            break
        sum
        GRID, size = binaryReduce(size, GRID)
        GRID, size = binaryReduce(size, GRID)

    visualize(GRID)