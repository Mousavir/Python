import random
repeat = True
while repeat:
    def calcul():
        list_nombre = random.sample(range(1, 6), 4)

        sorted_list_nombre = sorted(list_nombre)



        premier_nombre_max = sorted_list_nombre[-1]
        deuxieme_nombre_max = sorted_list_nombre[-2]
        troisieme_nombre_max = sorted_list_nombre[-3]

        calcul_effectue = (premier_nombre_max, deuxieme_nombre_max, troisieme_nombre_max)
force = calcul_effectue
agilite = calcul_effectue
constitution = calcul_effectue
intelligence = calcul_effectue

print(force, agilite,constitution,intelligence)