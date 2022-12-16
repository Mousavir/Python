from math import pi

#classe cercle qui recoit valeur rayon en parametre et qui avec cette information + pi calcule l'air et la circonference du cercle
class Cercle:
    #fonction pour creru objet cercle avec rayon variale qui est associé a une valeur qui sera définit par la suite
    def __init__(self, parametre_1):
        self.rayon = parametre_1
    #fonction pour calculer l'air du cercle en utilisa vairbale rayon, le nombre pi et formule
    def calcul_air(self):
        return pi * self.rayon ** 2
    #fonction pour calculer la circomference du cercle en utilisant varibale rayon, le nombre pi et formule
    def calcul_circonference(self):
        return 2 * pi * self.rayon
