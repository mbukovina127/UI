import asyncio

import myUtils
from salesperson import Salesperson
import gen
import networkx as nx
import matplotlib.pyplot as plt

if __name__ == '__main__':
    print("generation algorithm")
    max_dist = 200
    points = 120
    pop = 100
    graf = myUtils.alocGraf(max_dist, points)
    visited = [x for x in range(len(graf))]

    salespeople = []
    for _ in range(pop):
        sp = Salesperson(myUtils.permutated_path(graf, list(visited)))
        salespeople.append(sp)


    number_of_generations = 0
    found_on = 0
    threshold = points*3
    inc = 0
    previous = salespeople[0].distanceTraveled
    while inc < threshold:
        salespeople = gen.newGeneration(salespeople, pop)
        if salespeople[0].distanceTraveled < previous:
            previous = salespeople[0].distanceTraveled
            asyncio.run(myUtils.visualize_path(salespeople[0].path))
            inc = 0
            found_on = number_of_generations
            print(str(found_on))
        inc+= 1
        number_of_generations += 1
    print("Gen: %s -> best: " % salespeople[0].distanceTraveled)
    asyncio.run(myUtils.visualize_path(salespeople[0].path))