import random
import myUtils

class Salesperson:
    def __init__(self, path: list = []):
        self.path = path
        self.distanceTraveled: int = 0
        if (len(self.path) > 0):
            self.calcDistance()

    def pathToStr(self):
        rStr = "PATH: "
        for node in self.path:
            rStr = rStr + "[" + str(node.x) + ":" + str(node.y) + "] "
        return str(rStr)
    def pathToStr(self, stefan: list):
        rStr = "PATH: "
        for node in stefan:
            rStr = rStr + "[" + str(node.x) + ":" + str(node.y) + "] "
        return str(rStr)

    def breedPath(self, parent1: 'Salesperson', parent2: 'Salesperson'):
        start = random.randint(0, len(parent1.path)-1)
        end = (start + (len(parent1.path) -1) // 2) % len(parent1.path)
        print(start, end)

        combinedPath = []
        if (start < end):
            combinedPath.extend(parent2.path[0:start])
            combinedPath.extend(parent1.path[start:end])
            combinedPath.extend(parent2.path[end:])
        else:
            combinedPath.extend(parent1.path[0:end])
            combinedPath.extend(parent2.path[end:start])
            combinedPath.extend(parent1.path[start:])
        
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
            