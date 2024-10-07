import asyncio

import myUtils
from salesperson import Salesperson
import gen
import networkx as nx
import matplotlib.pyplot as plt

if __name__ == '__main__':
    print("generation algorithm")
    #parametre
    max_dist = 200
    points = 100
    pop = 100
    threshold = points*3


    graf = myUtils.alocGraf(max_dist, points)
    visited = [x for x in range(len(graf))]
    salespeople = []
    for _ in range(pop):
        sp = Salesperson(myUtils.permutated_path(graf, list(visited)))
        salespeople.append(sp)


    number_of_generations = 0
    found_on = 0
    inc = 0
    previous = salespeople[0].distanceTraveled
    
    # performance graph
    performance_graf_x = list()
    performance_graf_y = list()
    performance_graf_x.append(number_of_generations)
    performance_graf_y.append(salespeople[0].distanceTraveled)

    while inc < threshold:
        salespeople = gen.newGeneration(salespeople, pop)
        if salespeople[0].distanceTraveled < previous:
            previous = salespeople[0].distanceTraveled
            # asyncio.run(myUtils.visualize_path(salespeople[0].path))
            inc = 0
            found_on = number_of_generations
            print(str(found_on))
        inc+= 1
        number_of_generations += 1
        performance_graf_x.append(number_of_generations)
        performance_graf_y.append(salespeople[0].distanceTraveled)

    print("Gen: %s -> best: " % salespeople[0].distanceTraveled)
    asyncio.run(myUtils.visualize_path(salespeople[0].path))

    #performance graph 
    asyncio.run(myUtils.vis_plot_performance(performance_graf_x, performance_graf_y, "Min. cesta   Genetický algo. Velkosť grafu: %s" % points  ))