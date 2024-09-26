import random
import myUtils
from node import Node


class Uses:
    def __init__(self, node: Node, count: int):
        self.node = node
        self.count = count

def countNodes(path: list, used: dict):
    for node in path:
        used[node] += 1



class Salesperson:
    def __init__(self, path: list = []):
        self.path = path
        self.distanceTraveled: int = 0
        if len(self.path) > 0:
            self.calcDistance()

    def pathToStr(self):
        rStr = "PATH: "
        for node in self.path:
            rStr = rStr + "[" + str(node.x) + ":" + str(node.y) + "] "
        return str(rStr)

    def breedPath(self, parent1: 'Salesperson', parent2: 'Salesperson'):
        start = random.randint(0, len(parent1.path)-1)
        end = (start + (len(parent1.path) -1) // 2) % len(parent1.path)

        if start > end:
            tmp = start
            start = end
            end = tmp

        combinedPath = parent1.path[:]
        usedNodes = set(parent1.path[start:end])
        for og in range(parent2.path.__len__()):
            if og not in range(start, end):
                for replace in range(parent2.path.__len__()):
                    if parent2.path[replace] not in usedNodes:
                        combinedPath[og] = parent2.path[replace]
                        usedNodes.add(parent2.path[replace])
                        break

        self.path = combinedPath
        self.mutatePath()
    
    def mutatePath(self):
        #swap
        if (random.randint(0,1) == 1):
            location = random.randint(0, len(self.path)-1)
            temp = self.path[location]
            self.path[location] = self.path[(location +1) % len(self.path)]
            self.path[(location +1) % len(self.path)] = temp
        
        self.calcDistance()


    def calcDistance(self):
        previous = self.path[0]
        lSize = len(self.path)
        self.distanceTraveled = 0
        for index in range(lSize+1):
            next = self.path[index % lSize]
            self.distanceTraveled += myUtils.distance(previous, next)
            previous = next
            