from Z2c.point import tupleDistance
from point import Point, pointDistance


class Cluster_C:
    def __init__(self, points):
        self.contents = set()
        self.center = Point(0, 0)
        self.number_of_points = 0

        if isinstance(points,set):
            self.contents = points
            self.calculateCenter()

        elif isinstance(points,tuple):
            self.contents.add(points)
            self.center = Point(points[0], points[1])

        else: raise TypeError

        self.number_of_points = len(self.contents)

    def calculateCenter(self):
        sum = Point(0,0)
        self.number_of_points = len(self.contents)
        for tuple_pt in self.contents:
            sum.x += tuple_pt[0]
            sum.y += tuple_pt[1]
        x_average = sum.x / self.number_of_points
        y_average = sum.y / self.number_of_points

        self.center.x = x_average
        self.center.y = y_average


    def checkCriterion(self, cl: 'Cluster_C', max: int):
        sum = 0
        for tuple_pt in self.contents:
            sum += tupleDistance(tuple_pt, (self.center.x , self.center.y))
        if sum / self.number_of_points > max:
            return False
        return True

    def merge(cl1: 'Cluster_C', cl2: 'Cluster_C', limit: int):
        new_set = cl1.contents | cl2.contents
        new_c = Cluster_C(new_set)
        new_c.calculateCenter()

        if (not new_c.checkCriterion(new_c, limit)):
            return False

        return new_c

class Cluster_M(Cluster_C):
    def __init__(self, points):
        super().__init__(points)
        self.calculateCenter()

    def calculateCenter(self):
        min = 400000
        min_point = Point(0,0)
        for st_tp in self.contents:
            sum = 0
            for nd_tp in self.contents:
                sum += tupleDistance(st_tp, nd_tp)

            if (sum < min):
                min = sum
                min_point = st_tp
        self.center = Point(min_point[0], min_point[1])

    def merge(cl1: 'Cluster_C', cl2: 'Cluster_C', limit: int):
        new_set = cl1.contents | cl2.contents
        new_c = Cluster_C(new_set)
        new_c.calculateCenter()

        if (not new_c.checkCriterion(new_c, limit)):
            return False

        return new_c