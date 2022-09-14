#Rozhina Mousavi
#13 septembre 2022
#TP1 word_count
chaine = (input("Écriver une chaine de caractères:")) #variable chaine est egale au chaine au caractères qu'entre l"utilisateur

def count_word(): #fonction count_word() qui calcule et donne le nombre de mots dans le chaine de caracteres qu'a entre l'utilisateur
   print("Il y a " + str(len(chaine.split(" "))) + " mots dans cette chaine de caractères")

count_word() #appel au fonction count_word()