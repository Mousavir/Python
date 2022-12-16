class Hero:
    def __init__(self, parametre_1, parametre_2, parametre_3, parametre_4):
        self.nombre_points_de_vie = parametre_1
        self.force_attaque = parametre_2
        self.force_defense = parametre_3
        self.nom_du_heros = parametre_4

    def faire_une_attaque(self):
        return self.force_defense + self.force_attaque

    def recevoir_des_dommages(self, parametre_5):
        self.dommages = parametre_5
        hp = self.dommages - self.force_defense

    def est_vivant(self):
        return True

    def afficher_infos(self):
        print(self.faire_une_attaque(), self.recevoir_des_dommages(), self.est_vivant())