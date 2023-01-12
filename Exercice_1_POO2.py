from random import randint
class NPC:
    def __init__(self):
        self.force
        self.agilite
        self.constitution
        self.inteligence
        self.sagesse
        self.charisme
        self.classe_armure = random.randint(1,12)
        self.nom = " "
        self.race = " "
        self.espece = " "
        self.point_de_vie = random.randint(1,20)
        self.profession = " "

    def afficher_caracteristiques(self):
        print(self)