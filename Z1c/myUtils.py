import math
import random
from cProfile import label

from node import Node
import networkx as nx
import matplotlib.pyplot as plt

def alocGraf() -> list:

    # BUG: possible 
    #creating 20 points
    graf = [Node(random.randint(0, 200), random.randint(0, 200)) for _ in range(100)]

    return graf


def distance(one: Node , two: Node):
    return math.sqrt((one.x - two.x)**2 + (one.y - two.y)**2)

def permutated_path(graf: list, visited: list):
    path = []
    while len(visited):
        x = random.randint(0, len(visited) -1)
        index = visited.pop(x)
        path.append(graf[index])

    return path

def visualize_path(path: list):
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