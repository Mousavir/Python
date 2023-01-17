import random


def calcul():
    global list_nombre
    list_nombre = random.sample(range(1, 6), 4)

    list_nombre.sort()
    print(list_nombre)
    return(list_nombre[-1], list_nombre[-2], list_nombre[-3])


force = calcul()
agilite = calcul()

print(force,agilite)
