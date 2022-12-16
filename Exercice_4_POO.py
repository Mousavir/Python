from random import randint

class Hero:
    def __init__(self, parametre_1):
        self.nombre_points_de_vie = random.randint(1,10)+ random.randint(1,10)
        self.force_attaque = random.randint(1,6)
        self.force_defense = random.randint(1,6)
        self.nom_du_heros = parametre_1

    def faire_une_attaque(self):
        return random.randint(1,6) + self.force_attaque

    def recevoir_des_dommages(self, parametre_5):
        dommages = parametre_5
        self.nombre_points_de_vie -= dommages - self.force_defense

    def est_vivant(self):
        if self.nombre_points_de_vie
