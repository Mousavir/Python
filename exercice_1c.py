#variable nombre_lignes_etoiles est egale a 11
nombre_lignes_etoiles = 11

#variable ligne est egale a 0
ligne = 0

#boucle while qui se repete tant que valeur associe varible ligne est plus petit que la valeur associe au variable nombre_lignes_etoiles
while ligne < nombre_lignes_etoiles:

    #variable etoile est egale au valeur associa au variable nombre_lignes_etoiles moins la valeur associe au variable ligne
    etoile = nombre_lignes_etoiles - ligne

    #boucle while qui se repete tant que la variable etoile est plus grand ou egale a 1
    while etoile >=1:

        #affiche a l'ecran de caractere (*) tant que la boucle est vrai -sur la meme ligne
        print("*", end="")
        #variable etoile egale a son valeur moins 1 a chaque fois que cette boucle se repete (nb de * diminue de 1 a chaque ligne)
        etoile-=1

    #variable ligne egale a lui meme plus 1 (augmente de 1 a chaque fois) - change valeur associe au variable ligne
    ligne +=1
    #change de ligne
    print()

