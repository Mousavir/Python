import random
borne_minimal = (int(input("Choisissez le nombre minimal pour la borne de nombre aléatoire:")))
borne_maximal = (int(input("Choisissez le nombre maximal pour la borne de nombre aléatoire:")))

print(borne_minimal)
print(borne_maximal)

x = random.randint(borne_minimal, borne_maximal)