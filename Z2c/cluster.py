from matplotlib.streamplot import OutOfBounds

from point import Point, pointDistance


class Cluster:
    def __init__(self, points):
        self.contents = set()
        self.centroid = Point(0,0)
        self.number_of_points = 0

        if isinstance(points,set):
            self.contents = points
            self.calculateCentroid()

        elif isinstance(points,Point):
            self.contents.add(points)
            self.centroid = points

        else: raise TypeError

        self.number_of_points = len(self.contents)

    def __lt__(self, other):
        if self.number_of_points < other.number_of_points:
            return True
        else: return False

    def calculateCentroid(self):
        sum = Point(0,0)
        self.number_of_points = 0
        for point in self.contents:
            sum.x += point.x
            sum.y += point.y
            self.number_of_points += 1
        x_average = sum.x / self.number_of_points
        y_average = sum.y / self.number_of_points

        self.centroid.x = x_average
        self.centroid.y = y_average

    ### Static methods
    ###

    def checkCriterion(self, cl: 'Cluster', max: int):
        for point in self.contents:
            if (pointDistance(point, cl.centroid) > max):
                return False
        return True

    def merge(cl1: 'Cluster', cl2: 'Cluster', limit: int):
        new_set = cl1.contents | cl2.contents
        new_c = Cluster(new_set)
        new_c.calculateCentroid()

        if (not new_c.checkCriterion(new_c, limit)):
            raise OutOfBounds

        return new_c
