import myUtils
from salesperson import Salesperson
import gen
import node


inc = 0

graf = [myUtils.alocGraf()]
# graf = [node.Node(0,0), node.Node(3,0), node.Node(3,4)]
visited = [x for x in range(len(graf))]


salespeople = []
for _ in range(20):
    sp = Salesperson(myUtils.permutatedPath(graf, list(visited)))
    salespeople.append(sp)

for x in range(100):
    print(f"Gen: {x} -> best: {salespeople[0].distanceTraveled} path: {salespeople[0].pathToStr()}")
    salespeople = gen.newGeneration(salespeople, 2)

print(f"Gen: {x} -> best: {salespeople[0].distanceTraveled} path: {salespeople[0].pathToStr()}")
    