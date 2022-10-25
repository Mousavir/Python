import random

niveau_vie = 20
force_adversaire = random.randint(1,5)

print("Voux tombez face à face avec un adversaire de difficulté:" + str(force_adversaire))

quoi_faire = input("""Que voulez-vous faire? 
1- Combattre cet adversaire
2- Contourner cet adversaire et aller ouvrir un autre porte
3- Afficher les règles du jeu
4- Quitter la partie
*Entrer le numero de l'option choisis*
Réponse:""")

print(quoi_faire)

if  quoi_faire == "1":
    print("ok")

elif quoi_faire == "2":
    print("oui")
elif quoi_faire == "3":
    print("non")

elif quoi_faire == "4":
    print()
