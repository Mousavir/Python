import random


def calcul():
    list_nombre = random.sample(range(1, 6), 4)

    sorted_list_nombre = sorted(list_nombre)


    premier_nombre_max = sorted_list_nombre[-1]
    deuxieme_nombre_max = sorted_list_nombre[-2]
    troisieme_nombre_max = sorted_list_nombre[-3]

    calcul_effectue = (premier_nombre_max, deuxieme_nombre_max, troisieme_nombre_max)
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
        print(self.force,self.agilite,self.constitution, self.intelligence,self.sagesse,self.charisme,self.classe_armure,self.nom,self.race,self.espece,self.point_de_vie,self.profession)

objet=NPC()
objet.afficher_caracteristiques()