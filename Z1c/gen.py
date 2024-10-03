import random

from fontTools.designspaceLib.types import clamp

import salesperson
from salesperson import Salesperson


def newGeneration(old: list, number) -> list:
    old.sort(key=lambda x: x.distanceTraveled)
    newPeople = []
    for _ in range(number):
        parents = chooseParents(old)
        children = breedPath(parent1=parents[0], parent2=parents[1])
        for child in children:
            person = Salesperson(child)
            newPeople.append(person)

    newPeople.sort(key=lambda x: x.distanceTraveled)
    return newPeople


        


def chooseParents(generation):
    firstNumber = [random.randint(0, len(generation) - 1) for _ in range(len(generation) // 4)]
    secondNumber = [random.randint(0, len(generation) - 1) for _ in range(len(generation) // 4)]
    firstNumber.sort()
    secondNumber.sort()
    pair = list([firstNumber[0]])
    for i in range(len(secondNumber)):
        if secondNumber[i] != pair[0]:
            pair.append(secondNumber[i])
    return [generation[pair[0]], generation[pair[1]]]

def breedPath(parent1: 'Salesperson', parent2: 'Salesperson') -> list :
    start = random.randint(0, len(parent1.path) - 1)
    end = (start + (len(parent1.path) - 1) // 2) % len(parent1.path)

    if start > end:
        tmp = start
        start = end
        end = tmp

    off1 = [None] * len(parent1.path)
    off2 = [None] * len(parent2.path)
    off1[start:end] = parent1.path[start:end]
    off2[start:end] = parent2.path[start:end]

    off1 = crossover(off1, parent1.path, parent2.path, start, end)
    off2 = crossover(off2, parent1.path, parent2.path, start, end)

    return [mutatePath(off1), mutatePath(off2)]

def crossover(offspring: list, immutable: list, parent2: list, start, end) -> list:
    for i in range(len(parent2)):
        if i in range(start, end):
            continue
        node = parent2[i]
        while node in offspring[start:end]:
            node = parent2[immutable.index(node)]
        offspring[i] = node
    return offspring

def mutatePath(path: list):
    # neighbour swap
    if random.randint(0,9) < 6:
        move_city(path)
    if random.randint(0, 9) < 5:
        neighbour_swap(path)
        if random.randint(0, 10) > 0:
            mutatePath(path)
    #random swap
    if random.randint(0, 9) < 3:
        random_swap(path)
    #reverse
    if random.randint(0, 9) < 3:
        reverse_segment(path)
    return path

def neighbour_swap(path):
    location = random.randint(0, len(path) - 1)
    temp = path[location]
    path[location] = path[(location + 1) % len(path)]
    path[(location + 1) % len(path)] = temp
    return path

def random_swap(path):
    location1 = random.randint(0, len(path) - 1)
    location2 = location1 + (random.randint(0, len(path) //3))
    location2 = location2 % len(path)
    temp = path[location1]
    path[location1] = path[location2]
    path[location2] = temp
    return path

def reverse_segment(path):
    start = random.randint(0, len(path) - 1)
    end = (start + random.randint(0, len(path) - 1))
    if start > end:
        start, end = end, start
    for i in range(start, end // 2):
        keep = path[i]
        path[i] = path[end - i]
        path[end - i] = keep

def move_city(path: list):
    city = path.pop(random.randint(0, len(path) - 1))
    index = random.randint(0, len(path))
    path.insert(index, city)
