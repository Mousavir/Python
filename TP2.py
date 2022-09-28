#Rozhina Mousavi
#28 septembre 2022
#TP2

import random

x= random.randint(0,100)
nombre_essai = 0

print(x)
print("""J'ai choisi un nombre au hasard entre 0 et 100. 
À vous de deviner...""")

essai = (int(input("Entrez votre essai:")))
print(str(essai))

if essai < x:
    print("x >", (int(essai)))

elif essai > x:
    print("x <", (int(essai)))

elif essai == x:
    print("Bravo! Bonne réponse!")
    quit = (input("Voulez-vous faire une autre partie (o/n)?:"))
    print(quit)
    if quit == "y":
        print("Merci et aurevoir...")

    elif quit == "n":
        print("Merci et aurevoir...")

