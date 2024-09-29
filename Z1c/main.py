import myUtils
from salesperson import Salesperson
import gen
import networkx as nx
import matplotlib.pyplot as plt


inc = 0

graf = myUtils.alocGraf()
# graf = [node.Node(0,0), node.Node(3,0), node.Node(3,4)]
visited = [x for x in range(len(graf))]

population = 50

salespeople = []
for _ in range(population):
    sp = Salesperson(myUtils.permutated_path(graf, list(visited)))
    salespeople.append(sp)

for x in range(200):
    print(f"Gen: {x} -> best: {salespeople[0].distanceTraveled}")
    salespeople = gen.newGeneration(salespeople, population)
    myUtils.visualize_path(salespeople[0].path)


print(f"Gen: {x} -> best: {salespeople[0].distanceTraveled}")
