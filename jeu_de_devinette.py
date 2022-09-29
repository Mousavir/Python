#Rozhina Mousavi
#28 septembre 2022
#TP2 - jeu de devinettes

import random

x=  random.randint(0,100)
nombre_essai = 1

boucle_jeu =True
def essais(nombre_essai):
    return(nombre_essai += 1)

combien_essai = essais(nombre_essai)


while boucle_jeu:
    print(x)
    print("""J'ai choisi un nombre au hasard entre 0 et 100. 
    À vous de deviner...""")

    essai = (int(input("Entrez votre essai:")))
    print(str(essai))

    if essai < x:
        print("x >", (int(essai)))
        essais(nombre_essai)


    elif essai > x:
        print("x <", (int(essai)))
        essais(nombre_essai)

    elif essai == x:
        print("Bravo! Bonne réponse!")
        essais(nombre_essai)

        print("Vous avez réussi en " + str(combien_essai) + " essai(s)!")
        quitter = (input("Voulez-vous faire une autre partie (o/n)?:"))
        print(quitter)
        if quitter == "o":
            print("Merci et aurevoir...")
            boucle_jeu = False

        elif quitter == "n":
            boucle_jeu = True