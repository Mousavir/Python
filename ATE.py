#Rozhina Mousavi
#28 septembre 2022
#TP2 - jeu de devinettes tests
import random

nombres_essai =0


def essais():
    global nombres_essai
    nombres_essai += 1
    print(nombres_essai)

boucle_essais =True
boucle_jeu = True

def jeu():

    borne_minimal = (int(input("Choisissez le nombre minimal pour la borne de nombre aléatoire:")))
    borne_maximal = (int(input("Choisissez le nombre maximal pour la borne de nombre aléatoire:")))
    x = random.randint(borne_minimal, borne_maximal)
    print( x)
    print("J'ai choisi un nombre au hasard entre " + str(borne_minimal) + " et " + str(borne_maximal) + ". À vous de deviner...")
    return x

while boucle_jeu:
    jeu()
    boucle_jeu=False

while boucle_essais:
    global x
    nb= jeu()
    essai = (int(input("Entrez votre essai:")))
    print(str(essai))

    if essai < nb:
        print("x >", (int(essai)))
        essais()


    elif essai > nb:
        print("x <", (int(essai)))
        essais()

    elif essai == nb:
        print("Bravo! Bonne réponse!")
        essais()

        print("Vous avez réussi en " + str(nombres_essai) + " essai(s)!")
        quitter = (input("Voulez-vous faire une autre partie (o/n)?:"))
        print(quitter)
        if quitter == "o":
            boucle_essais = True
            boucle_jeu = True


        elif quitter == "n":
            print("Merci et aurevoir...")
            boucle_essais =False
            boucle_jeu = False