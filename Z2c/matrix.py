from Z2c.cluster_c import Cluster_C
from Z2c.point import clusterDistance


class Matrix:
    def __init__(self, clusters):
        self.clusters = clusters
        self.matrix = self.makeMatrix()


    def makeMatrix(self):
        self.matrix = [[0 for _ in range(len(self.clusters))] for _ in range(len(self.clusters))]
        for st in range(len(self.clusters)):
            for nd in range(len(self.clusters)):
                self.matrix[st][nd] = clusterDistance(self.clusters[st], self.clusters[nd])
        return self.matrix

    def findMinDist(self):
        min = 12000
        pair = (0, 0)
        for i in range(len(self.matrix)):
            for j in range(i + 1, len(self.matrix)):
                if self.matrix[i][j] < min:
                    min = self.matrix[i][j]
                    pair = (i, j)
        return pair

    def removeCluster(self, index: int):
        self.matrix.pop(index)
        for i in range(len(self.matrix)):
            self.matrix[i].pop(index)

    def addCluster(self, cluster):
        self.matrix.append([])
        for i in range(len(self.clusters)):
            self.matrix[-1].append(clusterDistance(cluster, self.clusters[i]))
            self.matrix[i].append(clusterDistance(cluster, self.clusters[i]))
        self.matrix[-1].append(0)
        self.clusters.append(cluster)

    def aggregate(self):
        pair = self.findMinDist()

        i,j = pair[0], pair[1]

        new_c = Cluster_C.merge(self.clusters[i], self.clusters[j], 500)
        if isinstance(new_c, bool):
            return new_c

        if i < j:
            i, j = j, i

        self.removeCluster(i)
        self.removeCluster(j)
        self.clusters.pop(i)
        self.clusters.pop(j)

        self.addCluster(new_c)
        return True

class Matrix_M:
    def __init__(self, clusters):
        self.clusters = clusters
        self.matrix = self.makeMatrix()

    def makeMatrix(self):
        self.matrix = [[0 for _ in range(len(self.clusters))] for _ in range(len(self.clusters))]
        for i, st in enumerate(self.clusters):
            for j, nd in enumerate(self.clusters):
                self.matrix[i][j] = clusterDistance(st, nd)
        return self.matrix

    def findMinDist(self):
        min = 12000
        pair = (0, 0)
        for i in range(len(self.matrix)):
            for j in range(i + 1, len(self.matrix)):
                if self.matrix[i][j] < min:
                    min = self.matrix[i][j]
                    pair = (i, j)
        return pair

    def removeCluster(self, index: int):
        self.matrix.pop(index)
        for i in range(len(self.matrix)):
            self.matrix[i].pop(index)

    def addCluster(self, cluster):
        self.matrix.append([])
        for i in range(len(self.clusters)):
            self.matrix[-1].append(clusterDistance(cluster, self.clusters[i]))
            self.matrix[i].append(clusterDistance(cluster, self.clusters[i]))
        self.matrix[-1].append(0)
        self.clusters.append(cluster)

    def aggregate(self):
        pair = self.findMinDist()

        i,j = pair[0], pair[1]

        new_c = Cluster_C.merge(self.clusters[i], self.clusters[j], 500)
        if isinstance(new_c, bool):
            return new_c

        if i < j:
            i, j = j, i

        self.removeCluster(i)
        self.removeCluster(j)
        self.clusters.pop(i)
        self.clusters.pop(j)

        self.addCluster(new_c)
        return True
