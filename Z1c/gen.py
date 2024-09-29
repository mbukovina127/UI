import random
import salesperson

def newGeneration(old: list, number) -> list:
    old.sort(key=lambda x: x.distanceTraveled)
    newPeople = []
    for _ in range(number):
        parents = chooseParents(old)
        person = salesperson.Salesperson()
        person.breedPath(parent1=parents[0], parent2=parents[1])
        newPeople.append(person)
    
    newPeople.sort(key=lambda x: x.distanceTraveled)
    return newPeople


        


def chooseParents(generation):
    firstNumber = [random.randint(0, len(generation) - 1) for _ in range(len(generation) // 3)]
    secondNumber = [random.randint(0, len(generation) - 1) for _ in range(len(generation) // 3)]
    firstNumber.sort()
    secondNumber.sort()
    pair = list([firstNumber[0]])
    for i in range(len(secondNumber)):
        if secondNumber[i] != pair[0]:
            pair.append(secondNumber[i])
    return [generation[pair[0]], generation[pair[1]]]

