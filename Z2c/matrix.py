from Z2c.cluster import Cluster_C, Cluster_M
from Z2c.point import clusterDistance


class Matrix_C:
    def __init__(self, clusters, lmt):
        self.map = list()
        self.clusters = clusters
        self.LIMIT = lmt
        self.matrix = self.makeMatrix()


    def makeMatrix(self):
        self.matrix = [[0 for _ in range(len(self.clusters))] for _ in range(len(self.clusters))]
        for st in range(len(self.clusters)):
            self.map.append(20000)
            for nd in range(len(self.clusters)):
                dst = clusterDistance(self.clusters[nd], self.clusters[st])
                self.matrix[st][nd] = dst
                if (dst < self.map[-1]) and dst > 0:
                    self.map[-1] = dst


        return self.matrix

    def recalculateMap(self, index):
        min = 20000
        for dst in self.matrix[index]:
            if min > dst > 0:
                min = dst
                self.map[index] = min


    def findMinDist(self):
        min = 12000
        index = -1
        for min_row in range(len(self.matrix)):
            if self.map[min_row] < min:
                min = self.map[min_row]
                index = min_row
        for i,dist in enumerate(self.matrix[index]):
            if dist == min:
                return (index, i)
        return False

    def removeCluster(self, index: int):
        del self.matrix[index]
        del self.map[index]
        del self.clusters[index]

        for i in range(len(self.matrix)):
            if self.map[i] == self.matrix[i].pop(index):
                self.recalculateMap(i)

    def addCluster(self, cluster):
        self.matrix.append([])
        self.map.append(0)
        min_last = 20000
        for i in range(len(self.clusters)):
            dst = clusterDistance(cluster, self.clusters[i])
            self.matrix[-1].append(dst)
            self.matrix[i].append(dst)

            if self.map[i] > dst > 0:
                self.map[i] = dst
            if min_last > dst > 0:
                min_last = dst

        self.map[-1] = min_last
        self.matrix[-1].append(0)
        self.clusters.append(cluster)

    def aggregate(self):
        pair = self.findMinDist()

        i,j = pair[0], pair[1]

        new_c = Cluster_C.merge(self.clusters[i], self.clusters[j], self.LIMIT)
        if isinstance(new_c, bool):
            return new_c

        if i < j:
            i, j = j, i

        self.removeCluster(i)
        self.removeCluster(j)

        self.addCluster(new_c)
        return True

class Matrix_M(Matrix_C):
    def __init__(self, clusters, lmt):
        super().__init__(clusters,lmt)

    def aggregate(self):
        pair = self.findMinDist()

        i,j = pair[0], pair[1]

        new_c = Cluster_M.merge(self.clusters[i], self.clusters[j], self.LIMIT)
        if isinstance(new_c, bool):
            return new_c

        if i < j:
            i, j = j, i

        self.removeCluster(i)
        self.removeCluster(j)

        self.addCluster(new_c)
        return True
