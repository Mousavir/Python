#classe rectangle qui recoit a largeur et lalongeur comme des parametre et les utilise pour calculer l'air puis elle peut afficher les information du rectangle a l'ecran
class Rectangle:
    #fonction qui créer variabel largeur et longeur asoci a une valeur qui sera definit apres (objet cree)
    def __init__(self, parametre_1, parametre_2):
        self.largeur = parametre_1
        self.longueur = parametre_2
    #fonction qui permet de calculer l'air du rectangle et d'en retourner la reponse en utilisant valeurs de l'objet crer
    def calcul_air(self):
        return self.largeur * self.longueur
    #fonction pour afficher les informations sur largeur, longeur et air rectangle
    def afficher_infos(self):
        print(self.largeur, self.longueur, self.calcul_air())