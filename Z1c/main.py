import myUtils
from salesperson import Salesperson
import gen
import networkx as nx
import matplotlib.pyplot as plt


inc = 0

graf = myUtils.alocGraf()
# graf = [node.Node(0,0), node.Node(3,0), node.Node(3,4)]
visited = [x for x in range(len(graf))]


salespeople = []
for _ in range(50):
    sp = Salesperson(myUtils.permutated_path(graf, list(visited)))
    salespeople.append(sp)

for x in range(300):
    print(f"Gen: {x} -> best: {salespeople[0].distanceTraveled}")
    salespeople = gen.newGeneration(salespeople, 100)
    myUtils.visualize_path(salespeople[0].path)


print(f"Gen: {x} -> best: {salespeople[0].distanceTraveled}")
myUtils.visualize_path(salespeople[0].path)