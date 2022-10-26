import random


force_adversaire = random.randint(1, 5)
autre_partie = "o"

def nouveau_niveau_vie():
    global niveau_vie
    niveau_vie = 20
    niveau_vie -= 1
    print(niveau_vie)




def instructions():
    print("""Pour réussir un combat, il faut que la valeur du dé lancé soit supérieure à la force de l’adversaire. 
            Dans ce cas, le niveau de vie de l’usager est augmenté de la force de l’adversaire.
            Une défaite a lieu lorsque la valeur du dé lancé par l’usager est inférieure ou égale à la force de l’adversaire.  Dans ce cas, le niveau de vie de l’usager est diminué de la force de l’adversaire.
            La partie se termine lorsque les points de vie de l’usager tombent sous 0.
            L’usager peut combattre ou éviter chaque adversaire, dans le cas de l’évitement, il y a une pénalité de 1 point de vie. """)
def jeu():

    print("Vous tombez face à face avec un adversaire de difficulté:" + str(force_adversaire))

    quoi_faire = ("""Que voulez-vous faire? 
    1- Combattre cet adversaire
    2- Contourner cet adversaire et aller ouvrir un autre porte
    3- Afficher les règles du jeu
    4- Quitter la partie
    *Entrer le numero de l'option choisis*""")

    print(quoi_faire)

    boucle_jeu = True
    while boucle_jeu:
        decision = (input("Entrez votre decision:"))
        if  decision == "1":
            score_dé = random.randint(1,6)
            print("Lancé du dé:" + str(score_dé))
            if score_dé <= force_adversaire:
                combat_statut = "victoire"

            elif score_dé >= force_adversaire:
                combat_statut = "defaite"
            print("Dernier combat =" + str(combat_statut))


        elif decision == "2":
            nouveau_niveau_vie()
            print("Niveau de vie mise a jour:" +str(niveau_vie))

        elif decision == "3":
            instructions()

        elif decision == "4":
            print("Merci et aurevoir!")
            boucle_jeu = False


while autre_partie == "o":
    jeu()
    autre_partie = input("Voulez voulez faire une autre partie (o/n)")

