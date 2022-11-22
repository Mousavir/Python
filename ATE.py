import random
nombres_de_victoires =0
minimum = 1
maximum = 5
force_adversaire = random.randint(minimum,maximum)

print(force_adversaire)

def augmentation():
    if nombres_de_victoires > 3:
        global minimum
        global maximum
        minimum +=4
        maximum+=5
        force_adversaire(minimum,maximum)

boucle_jeu = True
while boucle_jeu:
    decision = (input("entrer votre decision:"))
    augmentation()
    if decision =="yes":
        nombres_de_victoires +=2

    elif decision == "non":
        nombres_de_victoires+=1