import random

choisir = input("Vous voulez choisir propre nombre ou un borne définit")

if choisir == "choisir":
    borne_minimal= (int(input("Choisissez le nombre minimal pour la borne de nombre aléatoire:")))
    borne_maximal = (int(input("Choisissez le nombre maximal pour la borne de nombre aléatoire:")))
    x = random.randint(borne_minimal, borne_maximal)

elif choisir == "definit":
    x = random.randint(0,100)

print( x)
