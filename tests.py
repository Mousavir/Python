
jouer = "o"
def nouveau_niveau_vie():
    global niveau_vie
    niveau_vie = 20
    niveau_vie -= 1
    print(niveau_vie)
nouveau_niveau_vie()


def jeu():
    print("Niveau de vie mise a jour:" +str(niveau_vie))



