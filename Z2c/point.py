import heapq
import math
import queue


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def pointDistance(p1, p2):
    return math.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)

def clusterDistance(p1, p2):
    return math.sqrt((p1.centroid.x - p2.centroid.x)**2 + (p1.centroid.y - p2.centroid.y)**2)

def minDistance(clusters: list):
    distances = []
    for i, st in enumerate(clusters):
        for j, nd in enumerate(clusters, start=i + 1):
            priority = clusterDistance(st, nd)
            if priority == 0: continue
            heapq.heappush(distances, (priority, (st, nd)))

    return distances


