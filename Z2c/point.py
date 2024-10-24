import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def distance(p1: Point, p2: Point):
    return math.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)