import random

from cluster import Cluster
from point import Point




def compress(value, compression) -> int:
    return round(value / compression)

def addToGrid(value, grid):
    if (type(value) is Point):
        graf[compress(value.x, compression)][compress(value.y, compression)].add(value)
    if (type(value) is Cluster):
        graf[compress(value.centroid.x, compression)][compress(value.centroid.y, compression)].add(value)
    if (type(value) is set or type(value) is list):
        for point in value:
            graf[compress(point.x, compression)][compress(point.y, compression)].add(point)

def clamp(value, minimum, maximum):
    if (value < minimum):
        value = minimum
    if (value > maximum):
        value = maximum
    return value


if __name__ == '__main__':

    min = -5000
    max = 5000
    compression = 100
    number_of_secondary_points = 200
    offset_min = -100
    offset_max = 100
    size = int((max - min)/compression)

    randomPoints = [ Point(random.randint(min, max), random.randint(min, max)) for _ in range(20)]

    graf = [[set() for _ in range(size)] for _ in range(size)]

    allPoints = set()
    for point in randomPoints:
        for x in range(number_of_secondary_points):
            p = Point(clamp((random.randint(offset_min, offset_max) + point.x), min, max), clamp((random.randint(offset_min, offset_max) + point.y), min, max))
            allPoints.add(p)


    addToGrid(randomPoints, graf)
    addToGrid(allPoints, graf)

