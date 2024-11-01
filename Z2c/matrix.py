from Z2c.cluster import Cluster_C, Cluster_M
from Z2c.point import clusterDistance


class Matrix_C:
    def __init__(self, clusters, lmt):
        self.clusters = clusters
        self.matrix = self.makeMatrix()
        self.LIMIT = lmt


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
        del self.matrix[index]
        for i in range(len(self.matrix)):
            del self.matrix[i][index]
        del self.clusters[index]

    def addCluster(self, cluster):
        self.matrix.append([])
        for i in range(len(self.clusters)):
            dst = clusterDistance(cluster, self.clusters[i])
            self.matrix[-1].append(dst)
            self.matrix[i].append(dst)
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
