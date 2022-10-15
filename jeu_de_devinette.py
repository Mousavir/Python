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
choisis = (input(" Voulez vous choisir votre propre borne pour le nombre ou préférer vous l'option par défaut (0-100)? Répondez choisis ou defaut:"))

def choisis_bornes(choisis):

    if choisis == "choisis":
        borne_minimal = (int(input("Choisissez le nombre minimal pour la borne de nombre aléatoire:")))
        borne_maximal = (int(input("Choisissez le nombre maximal pour la borne de nombre aléatoire:")))

        print(borne_minimal)
        print(borne_maximal)

        x = random.randint(borne_minimal, borne_maximal)
        print(x)
        print("J'ai choisi un nombre au hasard entre " + str(borne_minimal) + " et " + str(borne_maximal) + ".\nÀ vous de deviner...")

    elif choisis == "defaut":
        x = random.randint(0, 100)
        print(x)
        print("J'ai choisi un nombre au hasard entre 0 et 100\nÀ vous de deviner...")

    boucle_jeu = True
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
    choisis_bornes(choisis)
    quitter = input("Voulez vous quitter (o/n)")
    if quitter == "o":
        print("Merci et aurevoir!")