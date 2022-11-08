#Rozhina Mousavi
#28 septembre 2022
#TP2 - jeu de devinettes

import random

#fonction essais ou le variable nombres_essais est egale a plus 1 à chaque apelle de cette fonction
def essais():
    global nombres_essai #la variable nombres_essais est global
    nombres_essai += 1

#variable autre_partie est egale a o
autre_partie = "o"

#fonction jeu() pour choisir les bornes: l'utilisateur choisit s'il veut choisir lui même les bornes du nombre aléatoire (option choisis) ou choisit d"utilier les bornes defaut (option defaut)
#fonction jeu() pour jouer le jeu: contient le boucle while boucle_jeu: partie ou l'utilisateur entre un nombre en essaie, si son nombre = plus petit ou plus grand que celui en question, affichage à l'écran qui indiquant ceci, sinon si l'essai= nombre, affiche message bravo et le nb d'essai pris
#fonction jeu() est repete autant de fois selon si l'utilisateur veut jouer un autre jeu dans le boucle while autre_partie = "o".
def jeu():
    #variable choisis est egale a la reponse entre par l'utilisateur soit choisis ou defaut
    choisis = (input("Voulez vous choisir votre propre borne pour le nombre ou préférer vous l'option par défaut (0-100)? Répondez choisis ou defaut:"))

    #si le variable choisis est egale a choisis -entre par l'utilisateur- l'utilisateur peut choisir une nombre pour borne minimal et maximal
    if choisis == "choisis":
            borne_minimal = (int(input("Choisissez le nombre minimal pour la borne de nombre aléatoire:")))
            borne_maximal = (int(input("Choisissez le nombre maximal pour la borne de nombre aléatoire:")))

    #si le variable choisis est egale a defaut-entre par l'utilisateur- les bornes minimales et baximales (0 et 100 respectivement) predefinit egalent aux variables respectifs
    elif choisis == "defaut":
        borne_minimal= 0
        borne_maximal = 100

    #variable x est égale a un nombre alleatoire entre le borne minimal et maximal et cela depend de ci l'utilisateur decide de choisir les bornes ou ceux definit par defaut
    x = random.randint(borne_minimal, borne_maximal)
    # affiche a l'ecran le texte suivant indiquant la borne minimal et maximal soit celui définit par l'utilisateur ou celui par defaut dependant de l'option choisie ou defaut pris
    print("J'ai choisi un nombre au hasard entre " + str(borne_minimal) + " et " + str( borne_maximal) +". \n À vous de deviner...")
    #boucle de jeu est vraie
    boucle_jeu = True

    #boucle qui roule tant que la valeur du variable boucle jeu est vrai (True)
    while boucle_jeu:
        #l'utilisateur entre son essai
        essai = (int(input("Entrez votre essai:")))

        #si l'essai de l'utilisateur (nb) est plus petit que le nombre x en question affiche a l'ecran le texte disant que x est plus grand que l'essai de l'utilisateur
        if essai < x:
            print("Mauvaise reponse, le nombre est plus grand que (x >)", (int(essai)))
            # appel au fonction essais
            essais()

        #si l'essai de l'utilisateur (nb) est plus grand que le nombre x en question et que if est faux affiche a l'ecran le texte disant que x est plus petit que l'essai de l'utilisateur
        elif essai > x:
            print("Mauvais choix, le nombre est plus petit que (x <)", (int(essai)))
            #appel au fonction essais
            essais()

        #si l'essai de l'utilisateur (nb) est egale a la valeur de x choisis au hasard entre certains bornes dependament affiche a l'ecran message felicitation
        elif essai == x:
            print("Bravo! Bonne réponse!")
            # appel au fonction essais
            essais()

            #affiche a l'ecran message que l'utilisateur a reussis en tel nb d'essai grace au fonction essais()
            print("Vous avez réussi en " + str(nombres_essai) + " essai(s)!")
            # variable boucle jeu est faux, n'est plus vrai est le boucle while dans la fonction jeu() se termine
            boucle_jeu =False


#boucle autre_partie qui se repete tant que cette derniere variable est egale a o
while autre_partie == "o":
    # variable nombres_essais est egale a 0
    nombres_essai = 0
    # appel au fonction jeu() et donc a tout son contenu (partie choisir ou defaut des bornes et la partie du jeu (deviner valeur de x + nb essai pris)
    jeu()
    # variable est egale au reponse uq'en l'utilisateur pour jouer encore
    autre_partie = input("Voulez voulez faire une autre partie (o/n)")

    #si le reponse que l'utilisateur entre est egale a n affiche message de politesse et d'aurevoir
    if autre_partie == "n":
        print("Merci et aurevoir!")