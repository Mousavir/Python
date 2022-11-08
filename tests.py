import random
niveau_vie = 20
force_adversaire = random.randint(1, 5)
numero_adversaire = random.randint(0,100)
numero_combat = 0
nombres_de_victoires = 0
nombres_de_defaites = 0
decision = "1"

def combat():
    global numero_combat
    numero_combat +=1

def nb_victoires_consécutifs():
    nombres_de_victoire

def new_niveau_vie():
    global niveau_vie
    niveau_vie += int(force_adversaire)

def nouveau_niveau_vie():
    global niveau_vie
    niveau_vie -= int(force_adversaire)

def statut_partie():
    print("Adversaire: "+ str(numero_adversaire))
    print("Force de l'adversaire: " + str(force_adversaire))
    print("Niveau de vie de l'usager: " +str(niveau_vie))
    print("Combat " + str(numero_combat) + ": "+ str(nombres_de_victoires) + " victoires vs " +str(nombres_de_defaites) + " defaites")

if decision == "1":
    combat()
    statut_partie()
    score_dé = random.randint(1, 6)
    print("Lancé du dé:" + str(score_dé))

    if score_dé >= force_adversaire:
        combat_statut = "victoire"
        new_niveau_vie()



    elif score_dé <= force_adversaire:
        combat_statut = "defaite"
        nouveau_niveau_vie()
        nouveau_niveau_vie()


    print("Dernier combat = " + str(combat_statut))
    print("Niveau de vie = " + str(niveau_vie))



    elif score_dé > force_adversaire:
        niveau_vie += int(force_adversaire)
