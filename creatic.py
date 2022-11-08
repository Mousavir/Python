import random

niveau_vie = 0
force_adversaire = random.randint(1, 5)
numero_adversaire = random.randint(0, 100)
numero_combat = 0
nombres_de_victoires = 0
nombres_de_defaites = 0
decision = "1"


def combat():
    global numero_combat
    numero_combat += 1





def nouveau_niveau_vie():
    global niveau_vie

    if score_dé <= force_adversaire:
        global combat_statut
        combat_statut = "defaite"
        niveau_vie -= int(force_adversaire)

    elif score_dé > force_adversaire:
        combat_statut = "victoire"
        niveau_vie += int(force_adversaire)

def nb_victoires_consécutifs():
    global nombres_de_victoires


def statut_partie():
    print("Adversaire: " + str(numero_adversaire))
    print("Force de l'adversaire: " + str(force_adversaire))
    print("Niveau de vie de l'usager: " + str(niveau_vie))
    print("Combat " + str(numero_combat) + ": " + str(nombres_de_victoires) + " victoires vs " + str(
        nombres_de_defaites) + " defaites")


if decision == "1":
    combat()
    statut_partie()
    score_dé = random.randint(1, 6)
    print("Lancé du dé:" + str(score_dé))
    nouveau_niveau_vie()
    if niveau_vie <= 0:
        print("La partie est terminée, vous avez vaincu monstre(s)")

    print("Dernier combat = " + str(combat_statut))
    print("Niveau de vie = " + str(niveau_vie))
