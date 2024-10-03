import math
import random
from cProfile import label
from math import floor

from node import Node
import networkx as nx
import matplotlib.pyplot as plt

def alocGraf(maxdist: int, num_of_nodes: int) -> list:

    graf = list()
    # grid graf
    # one_d: int = int(math.sqrt(num_of_nodes))
    # factor: int = maxdist // one_d
    # for i in range(one_d):
    #     graf.extend([Node(random.randint(x*factor, x*factor+factor), random.randint(i*factor, i*factor+factor)) for x in range(one_d) ])

    #classic random
    graf = [Node(random.randint(0, maxdist), random.randint(0, maxdist)) for _ in range(num_of_nodes)]

    return graf


def distance(one: Node , two: Node):
    return math.sqrt((one.x - two.x)**2 + (one.y - two.y)**2)

def length_of_path(path: list):
    previous = path[0]
    lSize = len(path)
    path_distance = 0
    for index in range(lSize + 1):
        next = path[index % lSize]
        path_distance += distance(previous, next)
        previous = next
    return path_distance

def permutated_path(graf: list, visited: list):
    path = []
    while len(visited):
        x = random.randint(0, len(visited) -1)
        index = visited.pop(x)
        path.append(graf[index])

    return path

async def visualize_path(path: list):
    vis_graph = nx.Graph()
    vis_graph.add_nodes_from(path)
    pos = dict()
    for node in path:
        pos[node] = (node.x, node.y)
    edges = list(zip(path, path[1:]))
    edges.append([path[-1], path[0]])
    nx.draw(vis_graph, pos=pos, node_color='red', node_size=25)
    tags = {x: "Node " + str(path.index(x)) for x in path}
    # nx.draw_networkx_labels(vis_graph, pos=pos, labels=tags)
    nx.draw_networkx_edges(vis_graph, pos=pos, edgelist=edges, edge_color='blue')
    plt.show()

