import myUtils


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

    def calcDistance(self):
        previous = self.path[0]
        lSize = len(self.path)
        self.distanceTraveled = 0
        for index in range(lSize+1):
            next = self.path[index % lSize]
            self.distanceTraveled += myUtils.distance(previous, next)
            previous = next
            