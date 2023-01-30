# TP POO3
# Rozhina Mousavi
# Janvier 2023

import random


# fonction calcul qui renvoye la valeur des trois plus hautes valeurs choisis parmi 4 nombres, chacun resultant d'un nombre aléatoire qu'il classe en ordre croissant (sort) pour pouvoir trouver les 3 nb plus grands
def calcul():
    # la variable list nombre est globale
    global list_nombre

    # la variable list_nombre est egale a 4 nombres chacun dans un (range) nb aléatoire entre 1 et 6
    list_nombre = random.sample(range(1, 6), 4)

    # fonction sort() pour mettre en ordre croissant les valeurs du variable list_nombre
    list_nombre.sort()

    # revoye (return) les 3 plus haut nb (selon l'ordre croissant) du variable list_nombre
    return (list_nombre[3] + list_nombre[2] + list_nombre[1])


# classe NPC (non player character qui contient l'infromation pour les variable et pour les afficher ces caracteristiques
class NPC:
    #fonction qui contient informations sur divers variables (string, nb aleatoire ou d'apres valeur fonction calcul (objet creer)
    def __init__(self):
        self.force = calcul()
        self.agilite = calcul()
        self.constitution = calcul()
        self.intelligence = calcul()
        self.sagesse = calcul()
        self.charisme = calcul()
        self.classe_armure = random.randint(1, 12)
        self.nom = " "
        self.race = " "
        self.espece = " "
        self.point_de_vie = random.randint(1, 20)
        self.profession = " "

    #fonction afficher_characteristiques d'apres les variables definit dans __init__
    def afficher_caracteristiques(self):
        print("Caractéristiques du personnage: Force:", self.force, "Agilité:", self.agilite, " Constitution:",
              self.constitution, " Intelligence:", self.intelligence, "Sagesse:", self.sagesse, "Charisme:",
              self.charisme, " Classe d'armure:", self.classe_armure, " Nom:", self.nom, " Race:", self.race,
              " Espèce:", self.espece, " Point de vie:", self.point_de_vie, " Profession:", self.profession)




#classe Kobold (monstre) qui herite les charctéristiques et fonction du classe NPC et qui lui même contient d'autre capacites (attaquer et subir des dommages)
class Kobold(NPC):

    # fonction attaquer où il recoit le cible en parametre (paramtre_1) et renvoie la valeur
    def attaquer(self, parametre_1):
        return

    # fonction subir_dommages qui perd un certain nb de points de vie d'après la valeur associe au paramtre_1 (d'apres la reussite de l'attaque du hero joueur)

    def subir_dommages(self, parametre_2):
        self.point_de_vie -= parametre_2



# classe NPC (joueur) qui herite les charctéristiques et fonction du classe NPC et qui lui même contient d'autre capacites (attaquer un cible (ex:monstre) et subir des dommages)
class Hero(NPC):

    # fonction attaquer qui peut attaquer un cible qui est definit comme parametre.
    def attaquer(self, cible):
        #variable attaque est egale a un nombre aleatoire entre 1 et 20
        attaque = random.randint(1, 20)

        #declaration  de variable nombre_dommage (egale a 0)
        nombre_dommage= 0

        #condition if qui s'execute seulement si la variable attaque est egale a 20
        if attaque == 20:
            #variable nombre_dommage est egale a un nb aleatoire entre 1 et 8
            nombre_dommage = random.randint(1, 8)
        #condition elif qui s'execute seulement la variable attaque egale 1
        elif attaque == 1:
            # variable nombre_dommage est egale a 0
            nombre_dommage = 0

        #condition elif qui s'execute seulement si la variable attaque a une valeur plus grand ou egale au classe d'armure du cible (kobold)
        elif attaque >= cible.classe_armure:
            # variable nombre_dommage est egale a un nb aleatoire entre 1 et 6
            nombre_dommage = random.randint(1, 6)

        #condition else qui s'execute si toutes ceux ci-haut sont fausses
        else:
            # variable nombre_dommage est egale a 0
            nombre_dommage = 0

        #appelle a la la fonction subir_dommages du cible et lui donne comme parametre_2 la valeur d'un variable definit ci-haut d'après les circomstances de l'attaque du hero
        cible.subir_dommages(nombre_dommage)

    # fonction subir_dommages qui perd un certain nb de points de vie d'après la valeur associe au paramtre_3 et renvoie la valeur
    def subir_dommages(self, parametre_3):
        return


