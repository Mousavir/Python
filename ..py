import random
def calcul():
    list_nombre = random.sample(range(1, 6), 4)

    sorted_list_nombre = sorted(list_nombre)



    premier_nombre_max = sorted_list_nombre[-1]
    deuxieme_nombre_max = sorted_list_nombre[-2]
    troisieme_nombre_max = sorted_list_nombre[-3]

    calcul_effectue = (premier_nombre_max, deuxieme_nombre_max, troisieme_nombre_max)
force = calcul()
agilite = calcul()
constitution =calcul()
intelligence =calcul()

print(force, agilite,constitution,intelligence)