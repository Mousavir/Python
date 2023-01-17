# Exercice POO2
# Rozhina Mousavi
# Janvier 2023

import random

def calcul():
    global list_nombre
    list_nombre = random.sample(range(1, 6), 4)

    list_nombre.sort()
    return (list_nombre[3] + list_nombre[2] + list_nombre[1])


class NPC:
    def __init__(self):
        self.force = calcul()
        self.agilite =calcul()
        self.constitution =calcul()
        self.intelligence =calcul()
        self.sagesse = calcul()
        self.charisme = calcul()
        self.classe_armure = random.randint(1,12)
        self.nom = " "
        self.race = " "
        self.espece = " "
        self.point_de_vie = random.randint(1,20)
        self.profession = " "

    def afficher_caracteristiques(self):
        print("Caractéristiques du personnage: Force:", self.force, "Agilité:", self.agilite," Constitution:",self.constitution," Intelligence:", self.intelligence, "Sagesse:",self.sagesse, "Charisme:",self.charisme, " Classe d'armure:",self.classe_armure," Nom:",self.nom," Race:",self.race, " Espèce:",self.espece, " Point de vie:",self.point_de_vie," Profession:",self.profession)

class Kobold(NPC):
    def attaquer(self,parametre_1):
        return

    def subir_dommages(self,parametre_2):
        return


class Hero(NPC):
    def attaquer(self, parametre_3):
        return


    def subir_dommages(self,parametre_4):
        return

