import heapq
import math
import queue

from scipy.spatial.distance import euclidean

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def pointDistance(p1, p2):
    return euclidean([p1.x, p1.y], [p2.x, p2.y])

def clusterDistance(p1, p2):
    return euclidean([p1.centroid.x, p1.centroid.y], [p2.centroid.x, p2.centroid.y])

def minDistance(clusters: list, LIMIT: int):
    distances = []
    for i, st in enumerate(clusters):
        for j, nd in enumerate(clusters, start=i + 1):
            priority = clusterDistance(st, nd)
            if priority >= LIMIT or priority == 0: continue
            heapq.heappush(distances, (priority, (st, nd)))
    return distances


