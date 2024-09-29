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
        cut = random.randint(0, len(parent1.path)-1)
        
        #copy first parent into the path
        combinedPath = [None] * len(parent1.path)
        combinedPath[0:cut] = parent1.path[0:cut]

        #copy second parent into the path
        for i in range(cut, len(parent2.path)):
            if i in range(0,cut):
                continue
            node = parent2.path[i]
            #if node from p2 is in the path already because of p1
            # look at the position where it is occupied
            # use that index to find the cor. node from p2 repeat
            while node in combinedPath[0:cut]:
                node = parent2.path[parent1.path.index(node)]
            combinedPath[i] = node

        self.path = combinedPath
        self.mutatePath()
    
    def mutatePath(self):
        #swap
        if random.randint(0, 3) > 0:
            location = random.randint(0, len(self.path)-1)
            temp = self.path[location]
            self.path[location] = self.path[(location +1) % len(self.path)]
            self.path[(location +1) % len(self.path)] = temp
        if random.randint(0, 7) < 1:
            location1 = random.randint(0, len(self.path)-1)
            location2 = random.randint(0, len(self.path)-1)
            temp = self.path[location1]
            self.path[location1] = self.path[location2]
            self.path[location2] = temp

        self.calcDistance()


    def calcDistance(self):
        previous = self.path[0]
        lSize = len(self.path)
        self.distanceTraveled = 0
        for index in range(lSize+1):
            next = self.path[index % lSize]
            self.distanceTraveled += myUtils.distance(previous, next)
            previous = next
            