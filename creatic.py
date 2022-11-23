#Rozhina Mousavi
#TP3
#25 octobre 2022
import random

#variable numero_combat est egale a 0
numero_combat = 0

#variable nombres_de_victoires est egale a 0
nombres_de_victoires = 0

#variable nombres_de_defaites est egale a 0
nombres_de_defaites = 0

#variable autre_partie est egale a la lettre o
autre_partie = "o"

#variable minimum est egale a 1
minimum = 1

#variable maximum est egale a 12
maximum = 12

nombres_de_victoires_consecutifs = nombres_de_victoires

#fonction niveau_vie qui determine le statut du combat avec un monstre et change le niveau de vie de l'utilisateur en fonction
def nouveau_niveau_vie():
    #la variable niveau_vie est global
    global niveau_vie

    # fonction niveau vie qui si (if) le score total des 2 dé (score aleatoire entre 1 et 6 pour chacun) est plus petit ou egal a la variable du force d'adversaire, le statut du combat= defaite et le niveau de vi baisse basé sur la force d'adversaire
    if score_dé_final <= force_adversaire:
        global combat_statut
        combat_statut = "defaite"

        niveau_vie -= int(force_adversaire)

    # fonction niveau_vie qui si (elif) le score total des 2 dé (score aleatoire entre 1 et 6 pour chacun) est plus grand que le variable force adversaire, le statut du combat = victoire et niveau de vie augmente basé sur le force d'adversaire
    elif score_dé_final > force_adversaire:
        combat_statut = "victoire"

        niveau_vie += int(force_adversaire)


#fonction gange_perdu qui determine le nombres de victoires selon si le statut du combat est egale a une victoire ou un defaite
def gange_perdu():
    #la variable nombres_de_victoires et global

    global nombres_de_defaites
   #if si le variable combat_statut (determine ci haut) est egale a victoire, le nombre de victoires de l'utilisateur augmente de 1
    if combat_statut == "victoire":
        global nombres_de_victoires
        nombres_de_victoires += 1
        global nombres_de_victoires_consecutifs
        nombres_de_victoires_consecutifs = nombres_de_victoires

    #elif si le variable combat_statut (determin ci haut) est egale a defaite, le nombres de victoires de l'utisatoire devient 0
    elif combat_statut == "defaite":
        nombres_de_victoires_consecutifs = 0
        nombres_de_defaites +=1




def augmentation():
    if nombres_de_victoires > 3:
        global minimum
        global maximum
        minimum +=5
        maximum +=5
    elif nombres_de_victoires < 3:
        minimum = 1
        maximum = 12


def combat():
    global numero_combat
    numero_combat += 1


def contourner_monstre():
    global niveau_vie
    niveau_vie -= 1





def instructions():
    print("""Pour réussir un combat, il faut que la valeur du dé lancé soit supérieure à la force de l’adversaire. 
Dans ce cas, le niveau de vie de l’usager est augmenté de la force de l’adversaire.
Une défaite a lieu lorsque la valeur du dé lancé par l’usager est inférieure ou égale à la force de l’adversaire.  
Dans ce cas, le niveau de vie de l’usager est diminué de la force de l’adversaire.

La partie se termine lorsque les points de vie de l’usager tombent sous 0.

L’usager peut combattre ou éviter chaque adversaire, dans le cas de l’évitement, il y a une pénalité de 1 point de vie. """)


def statut_partie():
    print("Adversaire: " + str(numero_adversaire))
    print("Force de l'adversaire: " + str(force_adversaire))
    print("Niveau de vie de l'usager: " + str(niveau_vie))
    print("Combat " + str(numero_combat) + ": " + str(nombres_de_victoires) + " victoires vs " + str(nombres_de_defaites) + " defaites")


def jeu():
    boucle_jeu = True
    while boucle_jeu:
        global force_adversaire
        force_adversaire = random.randint(minimum,maximum)
        global score_dé_1
        global score_dé_2
        global score_dé_final
        score_dé_1 = random.randint(1, 6)
        score_dé_2 = random.randint(1, 6)
        score_dé_final = score_dé_1 + score_dé_2
        global numero_adversaire
        numero_adversaire = random.randint(1, 100)
        print("Vous tombez face à face avec un adversaire de difficulté:" + str(force_adversaire))

        quoi_faire = ("""Que voulez-vous faire? 
            1- Combattre cet adversaire
            2- Contourner cet adversaire et aller ouvrir un autre porte
            3- Afficher les règles du jeu
            4- Quitter la partie
            *Entrer le numero de l'option choisis*""")

        print(quoi_faire)

        decision = (input("Entrez votre decision:"))
        if decision == "1":
            augmentation()
            combat()
            statut_partie()
            print("Lancé du dé:" + str(score_dé_final))
            nouveau_niveau_vie()
            gange_perdu()
            print("Dernier combat = " + str(combat_statut) + "\nNiveau de vie = " + str(niveau_vie) + "\nNombre de victoires consécutives =" + str(nombres_de_victoires_consecutifs))


        elif decision == "2":
            contourner_monstre()
            print("Niveau de vie mise a jour:" + str(niveau_vie))

        elif decision == "3":
            instructions()

        elif decision == "4":
            print("Merci et aurevoir!")
            boucle_jeu = False

        if niveau_vie <= 0:
            print("La partie est terminée, vous avez vaincu " + str(nombres_de_victoires) + " monstre(s)")
            boucle_jeu = False

#boucle autre_partie qui se repete tant que cette derniere variable est egale la lettre o
while autre_partie == "o":

    # la variable biveau_vie est global
    global niveau_vie
    #variable niveau_vie est fixe arbitrairement a 20
    niveau_vie = 20
    #appelle a la fonction jeu et donc a tout son contenu et ses propres references a des fonctions (combat contre mostre avec 2 des et options pour decision et niveau de difficulte qui augment et niveau de vie qui change
    jeu()
    #variable autre_partie est egale au reponse qu'entre l'utilisateur pour s'il veut jouer un autre jeu (o) ou s'il ne veut pas (n)
    autre_partie = input("Voulez voulez faire une autre partie (o/n)")

    # si le reponse que l'utilisateur entre est egale a n affiche message d'aurevoir
    if autre_partie == "n":
        print("Aurevoir!")