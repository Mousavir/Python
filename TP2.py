#Rozhina Mousavi
#28 septembre 2022
#TP2 - jeu de devinettes

#fait appele à la bibliotheque random
import random

#fonction essais ou le variable nombres_essais est egale a plu 1 chaque fois que cette fonction est appele
def essais():
    global nombres_essai #la variable nombres_essais est global
    nombres_essai += 1

#variable autre_partie est egale a o
autre_partie = "o"

#fonction jeu() pour choisir les bornes et jouer le jeu
def jeu():
    #variable choisis est egale a la reponse entre par l'utilisateur soit choisis ou defaut
    choisis = (input("Voulez vous choisir votre propre borne pour le nombre ou préférer vous l'option par défaut (0-100)? Répondez choisis ou defaut:"))

    #si le variable choisis est egale a choisis -entre par l'utilisateur- l'utilisateur peut choisir une nombre pour borne minimal et maximal et ceci est stocké dans des variable
    if choisis == "choisis":
            borne_minimal = (int(input("Choisissez le nombre minimal pour la borne de nombre aléatoire:")))
            borne_maximal = (int(input("Choisissez le nombre maximal pour la borne de nombre aléatoire:")))

            #variable x est eagle a un nombre au hasard entre le borne définit par l'utilisateur
            x =random.randint(borne_minimal, borne_maximal)

            #affiche a l'ecran le texte suivant indiquant la borne minimal et maximal entre par l'utilisateur
            print("J'ai choisi un nombre au hasard entre " + str(borne_minimal) + " et " + str(borne_maximal) + ".\nÀ vous de deviner...")


    #si le variable choisis est egale a defaut-entre par l'utilisateur- l'orinateur genere un nombre au hasard entre 0 et 100 comme la valeur de x (variable)
    elif choisis == "defaut":
        x = random.randint(0, 100)
        #affiche a l'ecrann la phrase suivante en indiquant la borne par defaut
        print("J'ai choisi un nombre au hasard entre 0 et 100\nÀ vous de deviner...")

    #boucle de jeu est vraie
    boucle_jeu = True

    #boucle qui roule tant que la valeur de=u variable boucle jeu est vrai
    while boucle_jeu:
        #l'utilisateur entre son essai et ceci est stocke dans une variable essai
        essai = (int(input("Entrez votre essai:")))

        #si l'essai de l'utilisateur (nb) est plus petit que le nombre x en question affiche a l'ecran le texte disant que x est plus grand que l'essai de l'utilisateur
        if essai < x:
            print("Mauvaise reponse, le nombre est plus grand que (x >)", (int(essai)))
            essais() #appel au fonction essais

        #si l'essai de l'utilisateur (nb) est plus grand que le nombre x en question et que if est faux affiche a l'ecran le texte disant que x est plus petit que l'essai de l'utilisateur
        elif essai > x:
            print("Mauvais choix, le nombre est plus petit que (x <)", (int(essai)))
            essais() #appel au fonction essais

        #si l'essai de l'utilisateur (nb) est egale a la valeur de x choisis au hasard entre certains bornes dependament affiche a l'ecran message felicitation
        elif essai == x:
            print("Bravo! Bonne réponse!")
            essais() #appel au fonction essais

            #affiche a l'ecran message que l'utilisateur a reussis en tel nb d'essai grace au fonction essais()
            print("Vous avez réussi en " + str(nombres_essai) + " essai(s)!")
            boucle_jeu =False #variable boucle jeu est faux, n'est plus vrai est le boucle while dans la fonction jeu() se termine


#boucle autre_partie qui se repete tant que cette derniere variable est egale a o
while autre_partie == "o":
    nombres_essai = 0 #variable nombres_essais est egale a 0
    jeu() #appel au fonction jeu() et donc a tout son contenu
    autre_partie = input("Voulez voulez faire une autre partie (o/n)") #variable est egale au reponse uq'en l'utilisateur pour jouer encore

    #si le reponse que l'utilisateur entre, qui est stocke dans la variable est egale a n affiche message de politesse et d'aurevoir
    if autre_partie == "n":
        print("Merci et aurevoir!")