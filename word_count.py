#Rozhina Mousavi
#13 septembre 2022
#TP1 word_count

#variable chaine est egale au chaine au caractères qu'entre l"utilisateur
chaine = (input("Écriver une chaine de caractères:"))
nombre_dans_chaine = len(chaine.split(" "))
#fonction count_word() qui recoit l'input de l'utilisateur calcule et retourne le nombre de mots dans le chaine de caracteres qu'a entre l'utilisateur
def count_word(chaine):
   return(nombre_dans_chaine)

#variable nombre_de_mots est égale à la fonction count_word
nombre_de_mots = count_word(chaine) #appel au fonction count_word()

#affichage à l'ecran du nombre de mots dans la chaine de caractère grace à l'appel au fonction count_word
print("Il y a " + str(nombre_de_mots) + " mots dans cette chaine de caractères")