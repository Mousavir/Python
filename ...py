import random


def calcul():
    list_nombre = random.sample(range(1, 6), 4)

    sorted_list_nombre = sorted(list_nombre)


    premier_nombre_max = sorted_list_nombre[-1]
    deuxieme_nombre_max = sorted_list_nombre[-2]
    troisieme_nombre_max = sorted_list_nombre[-3]




force = calcul()
agilite =calcul()
constitution =calcul()
intelligence =calcul()
sagesse = calcul()
charisme = calcul()
classe_armure = random.randint(1,12)
nom = " "
race = " "
espece = " "
point_de_vie = random.randint(1,20)
profession = " "

def afficher_caracteristiques():
    print(force,agilite,constitution,intelligence,sagesse,charisme,classe_armure,nom,race,espece,point_de_vie,profession)

afficher_caracteristiques()