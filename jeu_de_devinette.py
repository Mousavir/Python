#Rozhina Mousavi
#28 septembre 2022
#TP2 - jeu de devinettes tests
import random

nombres_essai =0


def essais():
    global nombres_essai
    nombres_essai += 1
    print(nombres_essai)

quitter = "n"

def jeu():

    boucle_jeu = True
    borne_minimal = (int(input("Choisissez le nombre minimal pour la borne de nombre aléatoire:")))
    borne_maximal = (int(input("Choisissez le nombre maximal pour la borne de nombre aléatoire:")))
    x = random.randint(borne_minimal, borne_maximal)
    print(x)
    print("J'ai choisi un nombre au hasard entre " + str(borne_minimal) + " et " + str(borne_maximal) + ". À vous de deviner...")

    while boucle_jeu:
        essai = (int(input("Entrez votre essai:")))
        print(str(essai))
        if essai < x:
            print("x >", (int(essai)))
            essais()


        elif essai > x:
            print("x <", (int(essai)))
            essais()

        elif essai == x:
            print("Bravo! Bonne réponse!")
            essais()

            print("Vous avez réussi en " + str(nombres_essai) + " essai(s)!")
            boucle_jeu =False



while quitter == "n":
    print(quitter)
    jeu()
    quitter = input("Voulez vous quitter (o/n)")
    if quitter == "o":
        print("Merci et aurevoir!")