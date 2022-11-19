import random

niveau_vie = 20
numero_combat = 0
autre_partie = "o"
nombres_de_victoires=0
nombres_de_defaites=0
minimum = 1
maximum = 5


def gange_perdu():
    global nombres_de_victoires
    global nombres_de_defaites
    if combat_statut == "victoire":
        nombres_de_victoires +=1
    elif combat_statut=="defaite":
        nombres_de_victoires=0

def combat():
    global numero_combat
    numero_combat += 1

def contourner_monstre():
    global niveau_vie
    niveau_vie -= 1


def nouveau_niveau_vie():
    global niveau_vie
    if score_dé <= force_adversaire:
        global combat_statut
        combat_statut = "defaite"

        niveau_vie -= int(force_adversaire)

    elif score_dé > force_adversaire:
        combat_statut = "victoire"

        niveau_vie += int(force_adversaire)



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
    print("Vous tombez face à face avec un adversaire de difficulté:")

    quoi_faire = ("""Que voulez-vous faire? 
        1- Combattre cet adversaire
        2- Contourner cet adversaire et aller ouvrir un autre porte
        3- Afficher les règles du jeu
        4- Quitter la partie
        *Entrer le numero de l'option choisis*""")

    print(quoi_faire)

    boucle_jeu = True
    while boucle_jeu:
        global force_adversaire
        force_adversaire = random.randint(1, 5)
        global score_dé
        score_dé = random.randint(1, 6)
        global numero_adversaire
        numero_adversaire = random.randint(0, 100)
        decision = (input("Entrez votre decision:"))
        augmentation()
        if decision == "1":
            statut_partie()
            print("Lancé du dé:" + str(score_dé))
            nouveau_niveau_vie()
            gange_perdu()
            print("Dernier combat = " + str(combat_statut) + "\nNiveau de vie = " + str(niveau_vie) + "\nNombre de victoires consécutives =" +str(nombres_de_victoires))
            print()

        elif decision == "2":
            contourner_monstre()
            print("Niveau de vie mise a jour:" +str(niveau_vie))

        elif decision == "3":
            instructions()

        elif decision == "4":
            print("Merci et aurevoir!")
            boucle_jeu = False
        if niveau_vie <= 0:
            print("La partie est terminée, vous avez vaincu " + str(nombres_de_victoires) +" monstre(s)")
            boucle_jeu = False
while autre_partie == "o":

    jeu()
    autre_partie = input("Voulez voulez faire une autre partie (o/n)")