import matplotlib.pyplot as plt

def visualize(grid, TIME):
    x_axis = []
    y_axis = []
    centroids_x = []
    centroids_y = []
    color = []
    rotation = 5
    color_num = 0
    for rows in grid:
        for squares in rows:
            for cluster in squares:
                color_num += 1
                centroids_x.append(cluster.center.x)
                centroids_y.append(cluster.center.y)

                for point in cluster.contents:
                    x_axis.append(point.x)
                    y_axis.append(point.y)
                    color.append(color_num % rotation)

    color_map = {0: "red", 1: "green", 2: "blue", 3: "yellow", 4: "black"}
    c = [color_map[x] for x in color]
    plt.scatter(x_axis, y_axis, color=c, s=.5)
    plt.scatter(centroids_x, centroids_y, color="black", s=500, alpha=0.1)
    plt.title(str(TIME))
    plt.show()

def visualizeList(list_of_grid, centroids):
    x_axis = []
    y_axis = []
    centroids_x = []
    centroids_y = []
    color = []
    rotation = 5
    color_num = 0
    for cluster in list_of_grid:
        color_num += 1
        centroids_x.append(cluster.center.x)
        centroids_y.append(cluster.center.y)

        for point in cluster.contents:
            x_axis.append(point.x)
            y_axis.append(point.y)
            color.append(color_num % rotation)

    color_map = {0: "red", 1: "green", 2: "blue", 3: "magenta", 4: "black"}
    c = [color_map[x] for x in color]
    plt.scatter(x_axis, y_axis, color=c, s=1, alpha=0.1)
    if centroids:
        plt.scatter(centroids_x, centroids_y, color="black", s=500, alpha=0.1)
    plt.show()

