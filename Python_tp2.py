import random
nombres_de_victoires =0
minimum = 1
maximum = 5
force_adversaire = random.randint(minimum,maximum)

print(force_adversaire)

def augmentation():
    if nombres_de_victoires >= 3:
        global minimum
        global maximum
        minimum +=5
        maximum+=5

boucle_jeu = True
while boucle_jeu:
    decision = (input("entrer votre decision:"))

    if decision =="yes":
        nombres_de_victoires +=2
        augmentation()
        print(nombres_de_victoires)
        print(minimum)
        print(maximum)