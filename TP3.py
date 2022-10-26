import random

niveau_vie = 20
force_adversaire = random.randint(1, 5)
numero_adversaire = random.randint(1,20)
boucle_jeu = True

def statut_partie():
    print("Adversaire:" + str(numero_adversaire) + "\n Force de l'adversaire:" + str(force_adversaire) +"\nNiveau de vie de l'usager" + str(nveau_vie)+ "\nCombat" + str(numero_combat) + ":" + str(nombres_victoires) + "vs" + str(nombre_defaites))
statut_partie()

def jeu():

    print("Voux tombez face à face avec un adversaire de difficulté:" + str(force_adversaire))

    quoi_faire = input("""Que voulez-vous faire? 
    1- Combattre cet adversaire
    2- Contourner cet adversaire et aller ouvrir un autre porte
    3- Afficher les règles du jeu
    4- Quitter la partie
    *Entrer le numero de l'option choisis*
    Décision:""")

    print(quoi_faire)
    while boucle_jeu:

        if  quoi_faire == "1":
            lance_dé = random.randint(1,6)
            if lance_dé <= force_adversaire:
                print("ok")


        elif quoi_faire == "2":
            niveau_vie -= 1
            print("Vous recevez une pénalité de 1 point de vie. Voici votre niveau de vie mise à jour:" + str(niveau_vie))

        elif quoi_faire == "3":
            print("""Pour réussir un combat, il faut que la valeur du dé lancé soit supérieure à la force de l’adversaire. 
        Dans ce cas, le niveau de vie de l’usager est augmenté de la force de l’adversaire.
        Une défaite a lieu lorsque la valeur du dé lancé par l’usager est inférieure ou égale à la force de l’adversaire.  Dans ce cas, le niveau de vie de l’usager est diminué de la force de l’adversaire.
        La partie se termine lorsque les points de vie de l’usager tombent sous 0.
        L’usager peut combattre ou éviter chaque adversaire, dans le cas de l’évitement, il y a une pénalité de 1 point de vie. """)

        elif quoi_faire == "4":
            print("Merci et aurevoir!")
            boucle_jeu = False













