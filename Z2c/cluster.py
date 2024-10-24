from point import Point, distance


class Cluster:
    def __init__(self, points: set):
        self.contents = points
        self.number_of_points = 0
        self.centroid = Point(0,0)


    def calculateCentroid(self):
        sum = Point(0,0)
        for point in self.contents:
            sum.x += point.x
            sum.y += point.y
            self.number_of_points += 1
        x_average = sum.x / self.number_of_points
        y_average = sum.y / self.number_of_points

    ### Static methods
    ###
    def checkCriterion(self, cl: 'Cluster', max):
        for point in self.contents:
            if (distance(point, cl.centroid) > max):
                return False
        return True

    def merge(cl1: 'Cluster', cl2: 'Cluster', limit: int):
        new_c = Cluster(set(*cl1.contents, *cl2.contents))
        if (not new_c.calculateCentroid()):
            return False
        if (not new_c.checkCriterion(new_c, limit)):
            return False

        return new_c
