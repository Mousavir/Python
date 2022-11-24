# Rozhina Mousavi
# TP3
# 25 octobre 2022
import random

# variable autre_partie est egale a la lettre o
autre_partie = "o"


# fonction nouveau_niveau_vie qui determine le statut du combat avec un monstre et change le niveau de vie de l'utilisateur en fonction
def nouveau_niveau_vie():
    # la variable niveau_vie est global
    global niveau_vie

    # fonction niveau vie qui si (if) le score total des 2 dé (score aleatoire entre 1 et 6 pour chacun determnine plus bas) est plus petit ou egal a la variable du force d'adversaire, le statut du combat= defaite et le niveau de vi baisse basé sur la force d'adversaire
    if score_de_final <= force_adversaire:
        global combat_statut
        combat_statut = "defaite"

        niveau_vie -= int(force_adversaire)

    # fonction niveau_vie qui si (elif) le score total des 2 dé (score aleatoire entre 1 et 6 pour chacun) est plus grand que le variable force adversaire, le statut du combat = victoire et niveau de vie augmente basé sur le force d'adversaire
    elif score_de_final > force_adversaire:
        combat_statut = "victoire"

        niveau_vie += int(force_adversaire)


# fonction gange_perdu qui determine le nombres de victoires selon si le statut du combat est egale a une victoire ou un defaite et change le niveau de vie et de vioires et conséquence
def gange_perdu():
    # if si le variable combat_statut (determine ci haut) est egale a victoire, le nombre de victoires de l'utilisateur augmente de 1 et le nombre de combats gagnes augmente de 1
    if combat_statut == "victoire":

        # la varibale nombre_de_victoires est global
        global nombres_de_victoires
        nombres_de_victoires += 1

        # la variabe nombre_gagne est global
        global nombre_combat_gagne
        nombre_combat_gagne += 1

    # elif si le variable combat_statut (determine ci haut) est egale a defaite, le nombres de victoires   devient 0 et le nombre de defaites augmente de 1
    elif combat_statut == "defaite":
        global nombres_de_defaites

        nombres_de_victoires = 0

        nombres_de_defaites += 1


# fonction augmentation qui augmente ou de remmetre à l'arbitraire le minimum et le maximum utilise pour bornes de la force de l'adversaire
def augmentation():
    # si le nombre_de_victoires de utilisateur est plus grand que 3, les variable minimum et au maximum deja definit (plus bas) y s'y ajoutent une valeur de +10 a leur valeur deja existante pour que les nombre bornes pour le force d'adversaire aleatoire soit plus grande (adversaire plus fort)
    if nombres_de_victoires > 3:

        # la variable minimum est global
        global minimum
        # la variable minimum est global
        global maximum

        minimum += 10
        maximum += 10

    # si le nombre_de_victoires est plus petit que 3, les variables minimummest le maximum restent 1 et 12 respectivement ainsi les nombre bornes pour le force d'adversaire aleatoires est plus petit (adversaire plus faible)
    elif nombres_de_victoires < 3:
        minimum = 1
        maximum = 12


# fonction combat qui augmente le numero_combat de 1 à chaque fois elle est appeele (fait augmenter nb de combat effectue)
def combat():
    # la variable numero_combat est global
    global numero_combat
    numero_combat += 1


# fonction contourner_monstre qui est appele si l'option 2 est choisi (plus bas) où l'utilisateur contourne un monstre mais un point de vie lui est coute. Donc niveau de vie baisse de 1
def contourner_monstre():
    # la variable numero_combat est global
    global niveau_vie
    niveau_vie -= 1


# fonction instruction qui imprime le texte suivant qui consistent des instruction du jeu -combat des montres- lorsquelle est appele
def instructions():
    print("""Pour réussir un combat, il faut que la valeur du dé lancé soit supérieure à la force de l’adversaire. 
Dans ce cas, le niveau de vie de l’usager est augmenté de la force de l’adversaire.
Une défaite a lieu lorsque la valeur du dé lancé par l’usager est inférieure ou égale à la force de l’adversaire.  
Dans ce cas, le niveau de vie de l’usager est diminué de la force de l’adversaire.

La partie se termine lorsque les points de vie de l’usager tombent sous 0.

L’usager peut combattre ou éviter chaque adversaire, dans le cas de l’évitement, il y a une pénalité de 1 point de vie. """)


# fonction statut_partie qui imprime plusieurs donnes lies au differents status et information sur la/les parties lorsque'elle est appele
def statut_partie():
    # affice a l'ecran le numero de l'adversaire (variable decrit plus bas)
    print("Adversaire: " + str(numero_adversaire))
    # affiche a l'ecran le numero du force d'adversaire (variable decrit plus bas (au hasard entre different bornes))
    print("Force de l'adversaire: " + str(force_adversaire))
    # affiche a l'ecran le niveau de vie de l'utilisateur (variable decrit plus bas et qui change )
    print("Niveau de vie de l'usager: " + str(niveau_vie))
    # affiche a l'ecran le numero du combat (combien cobats effectues) le nombre de parties gagnes (victoires) et le nombre de parties en defaite (defaites)
    print("Combat " + str(numero_combat) + ": " + str(nombre_combat_gagne) + " victoires vs " + str(
        nombres_de_defaites) + " defaites")


# fonction jeu qui contient les information est le schema du jeu et qui contient la partie qui decrit les variables qui se chnages a chaque partie (chaque fois le boucle est effectue)
# fonction jeu dans lequel il y a la partie du les options donnes lorsque l'adversaire (son force) est presente et que l'utilisateur choisit l'option qu'il veut prendre
# fonction jeu qui contient la partie où lorsque l'utilisateur a choisit une option, les differentes resultats finaux de chaque option sont presentes (le partie sur les combats, les contournements, l'information et le quitter)
def jeu():
    # variable boucle_jeu est vrai
    boucle_jeu = True

    # boucle qui se repete tant que le varible boucle jeu est vrai
    while boucle_jeu:
        # la varibale force_adversaire est global
        global force_adversaire
        # la avriable force adversaire est egale a un nombre au hasard entre les bornes minimum et maximum (qui se font mis a jour et qui peuvent demeruer le meme dependamemnt)
        force_adversaire = random.randint(minimum, maximum)
        # la variable score_de_1 est global
        global score_de_1
        # la variable score_de_2 est global
        global score_de_2
        # la varibale score_de_final est global
        global score_de_final

        # la variable score_de_1 est egale a un nombre au hasard entre la borne entre 1 et 6
        score_de_1 = random.randint(1, 6)
        # la varibale score_de_2 est egale a un nombre au hasard entre 1 et 6
        score_de_2 = random.randint(1, 6)
        # la varibale score_de_final est egale a la valeur du score_de_1 additione du valeur du score_de_2
        score_de_final = score_de_1 + score_de_2
        # la vairbale numero_adversaire est globale
        global numero_adversaire
        # la variable numero_adversaire est egale a un nombre au hasard entre 1 et 100
        numero_adversaire = random.randint(1, 100)

        # affiche a l'ecran le texte suivant et qui indique la valeur du force de l'adversiare
        print("Vous tombez face à face avec un adversaire de difficulté:" + str(force_adversaire))

        # variable quoi_faire est egale au texte suivant qui decrit les differents options possibles dans le jeu
        quoi_faire = ("""Que voulez-vous faire? 
            1- Combattre cet adversaire
            2- Contourner cet adversaire et aller ouvrir un autre porte
            3- Afficher les règles du jeu
            4- Quitter la partie
            *Entrer le numero de l'option choisis*""")

        # affiche a l'ecran la variable quoi faire - donc tout son contenu
        print(quoi_faire)

        # variable decision est egale a valeur entre par l'utilisateur comme decision (un numeor soit 1,2,3 ou 4) (input de l'utilisateur est stocke dans la vairbale decision)
        decision = (input("Entrez votre decision: "))

        # si la valeur du varibale decision est de 1, il y a appele a plusieurs fonctions et des valeurs indicants le score du de, et le statut du combat sont affiches a l'ecran
        if decision == "1":
            # appele a la fonction augmentation
            augmentation()
            # appele a la fonction combat
            combat()
            # appele a la fonction statut_partie
            statut_partie()
            # affiche a l'ecran le texte avec la valeur du varible score_de_final
            print("Lancé du dé:" + str(score_de_final))
            # appele a la fonction nouveau_niveau_vie
            nouveau_niveau_vie()
            # appele a la fonction gagne_perdu
            gange_perdu()
            # affiche a l'ecran un texte dans le quel il contient si le combat est un victoire ou une defaite et quelle est le niveau de vie de l'utilisateur et le nombre de victoires ocnsecutifs de l'utilisateur
            print("Dernier combat = " + str(combat_statut) + "\nNiveau de vie = " + str(
                niveau_vie) + "\nNombre de victoires consécutives =" + str(nombres_de_victoires))

        # si la valeur di varible decision est de 2, il y a appele a la fonction contourner_monstre et il y a une affichage a l'ecran d'un texte qui contient le niveau de vie de l'utilisateur mise a jour (base)
        elif decision == "2":
            contourner_monstre()
            print("Niveau de vie mise a jour:" + str(niveau_vie))

        # si la valeur du varibale decision est egale a 3, il y appele au fonction instruction et donc a tout son contenu
        elif decision == "3":
            instructions()

        # si la valeur du varibale decision est egale a 4, il y a un message de politesse et d'aurevoir qui ets affiche a l'ecran qui est affiche a l'ecran est la variable boucle_jeu est faux, donc le boucle se termine et on sort de se boucle
        elif decision == "4":
            print("Merci et aurevoir!")
            boucle_jeu = False
        # si la valeur du niveau de vie est plus petit ou egale a zero un message de texte qui contient le nombre de victoires a l'ecran (donc le nombre de monstres vaicus) et la avriabel boucle_jeu est faux et donc cette boucle se termine et on sort de ce boucle
        if niveau_vie <= 0:
            print("La partie est terminée, vous avez vaincu " + str(nombres_de_victoires) + " monstre(s)")
            boucle_jeu = False


# boucle autre_partie qui se repete tant que cette derniere variable est egale la lettre o
while autre_partie == "o":
    # variable numero_combat est egale a 0
    global numero_combat
    numero_combat = 0

    # variable minimum est egale a 1
    global minimum
    minimum = 1

    # variable maximum est egale a 12
    global maximum
    maximum = 12

    # variable nombres_de_victoires est egale a 0
    global nombres_de_victoires
    nombres_de_victoires = 0

    # variable nombres_de_defaites est egale a 0
    global nombres_de_defaites
    nombres_de_defaites = 0
    # la variable biveau_vie est global

    global niveau_vie
    # variable niveau_vie est fixe arbitrairement a 20
    niveau_vie = 20
    global nombre
    nombre = 0
    global nombre_combat_gange
    nombre_combat_gagne = 0
    # appelle a la fonction jeu et donc a tout son contenu et ses propres references a des fonctions (combat contre mostre avec 2 des et options pour decision et niveau de difficulte qui augment et niveau de vie qui change
    jeu()
    # variable autre_partie est egale au reponse qu'entre l'utilisateur pour s'il veut jouer un autre jeu (o) ou s'il ne veut pas (n)
    autre_partie = input("Voulez voulez faire une autre partie (o/n)")

    # si le reponse que l'utilisateur entre est egale a n affiche message d'aurevoir
    if autre_partie == "n":
        print("Aurevoir!")


