import math
import random
from node import Node

def alocGraf() -> list:

    # BUG: possible 
    #creating 20 points
    graf = [Node(random.randint(0, 200), random.randint(0, 200)) for _ in range(20)]

    return graf


def distance(one: Node , two: Node):
    return math.sqrt((one.x - two.x)**2 + (one.y - two.y)**2)

def permutatedPath(graf: list, visited: list):
    path = []
    while len(visited):
        x = random.randint(0, len(visited) -1)
        index = visited.pop(x)
        path.append(graf[index])

    return path
