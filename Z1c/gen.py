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


        


def chooseParents(list):
    firstNumber = [random.randint(0, len(list) -1) for _ in range(len(list)//2)]
    secondNumber = [random.randint(0, len(list) -1) for _ in range(len(list)//2)]
    firstNumber.sort()
    secondNumber.sort()

    return [list[firstNumber[0]], list[secondNumber[0]]]

