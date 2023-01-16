import random

list_nombre = random.sample(range(1,6),4)

sorted_list_nombre = sorted(list_nombre)

print(sorted_list_nombre)

premier_nombre_max = sorted_list_nombre[-1]
deuxieme_nombre_max = sorted_list_nombre[-2]
troisieme_nombre_max = sorted_list_nombre[-3]

print(premier_nombre_max, deuxieme_nombre_max, troisieme_nombre_max)


objet=NPC()
objet.afficher_caracteristiques()