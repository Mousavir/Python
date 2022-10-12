import random
<<<<<<< HEAD
borne_minimal= (int(input("Choisissez le nombre minimal pour la borne de nombre aléatoire")))
borne_maximal = (int(input("Choisissez le nombre maximal pour la borne de nombre aléatoire")))
=======
>>>>>>> origin/master

choisis = (input("Voulez vous choisir votre propre borne pour le nombre ou préférer vous l'option par défaut (0-100)? Répondez choisis ou défaut:"))
def choisis_bornes(choisis):

<<<<<<< HEAD
print(borne_minimal)
print(borne_minimal)
print( x)
=======
    if choisis == "choisis":
        borne_minimal = (int(input("Choisissez le nombre minimal pour la borne de nombre aléatoire:")))
        borne_maximal = (int(input("Choisissez le nombre maximal pour la borne de nombre aléatoire:")))


        print(borne_minimal)
        print(borne_maximal)

        x = random.randint(borne_minimal, borne_maximal)

    elif choisis == "défaut":
        x = random.randint(0, 100)

choisis_bornes(choisis)
>>>>>>> origin/master
