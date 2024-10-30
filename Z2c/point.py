import heapq
import math
import queue

from scipy.spatial.distance import euclidean

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def pointDistance(p1, p2):
    return math.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)
    # return euclidean([p1.x, p1.y], [p2.x, p2.y])

def clusterDistance(p1, p2):
    return math.sqrt((p1.centroid.x - p2.centroid.x)**2 + (p1.centroid.y - p2.centroid.y)**2)
    # return euclidean([p1.centroid.x, p1.centroid.y], [p2.centroid.x, p2.centroid.y])

