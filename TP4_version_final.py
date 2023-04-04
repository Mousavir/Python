import arcade
import random

#variable pour la largeur et la hauteur de la fenetre
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600

#crer liste de couleurs depuis la librarie arcade
COLORS = [arcade.color.BLUE, arcade.color.FANDANGO_PINK,arcade.color.GOLDEN_POPPY, arcade.color.TURQUOISE_BLUE,arcade.color.SPRING_GREEN,arcade.color.RED,arcade.color.LAVENDER_INDIGO]

#créer l'objet Balle:methodes pour definir les parametre de l'objet, permetre changer de position sur la fenetre (bouger en restant dans le cadre), et de dessiner l'objet balle d'après les parametres
class Balle():

    #methode intit: les atributs propriétés du cercle
    def __init__(self, rayon,position_x,position_y, vitesse_deplacement_x, vitesse_deplacement_y, couleur):
        self.rayon = rayon
        self.centre_x = position_x
        self.centre_y = position_y
        self.change_x = vitesse_deplacement_x
        self.change_y = vitesse_deplacement_y
        self.color = couleur

    #methode on_update definit deplacement balle
    def on_update(self):
        self.centre_x += self.change_x
        self.centre_y += self.change_y
        # valider et assurer que la balle ne sort pas de l'ecran
        if self.centre_x < self.rayon:
            self.change_x *= -1

        if self.centre_x > SCREEN_WIDTH - self.rayon:
            self.change_x *= -1

        if self.centre_y < self.rayon:
            self.change_y *= -1

        if self.centre_y > SCREEN_HEIGHT - self.rayon:
            self.change_y *= -1


#methode dessiner balle sur la fenetre
    def draw(self):
        arcade.draw_circle_filled(self.centre_x, self.centre_y, self.rayon, self.color)


#créer l'objet Rectangle:methodes pour definir les parametre de l'objet, permetre changer de position sur la fenetre (bouger en restant dans le cadre), et de dessiner l'objet rectangle d'après les parametres
class Rectangle():

    # methode intit: les atributs propriétés du rectangle
    def __init__(self,position_x,position_y, vitesse_deplacement_x, vitesse_deplacement_y, largeur, hauteur, couleur, nombre_float):

        self.centre_x = position_x
        self.centre_y = position_y
        self.change_x = vitesse_deplacement_x
        self.change_y = vitesse_deplacement_y
        self.width = largeur
        self.height = hauteur
        self.color = couleur
        self.angle = nombre_float

    #methode on_update definit deplacement rectangle
    def on_update(self):
        self.centre_x += self.change_x
        self.centre_y += self.change_y
        #valider et assurer que la balle ne sort pas de l'ecran
        if self.centre_x < self.width/2:
            self.change_x *= -1

        if self.centre_x > SCREEN_WIDTH - self.width/2:
            self.change_x *= -1

        if self.centre_y < self.height/2:
            self.change_y *= -1

        if self.centre_y > SCREEN_HEIGHT - self.height/2:
            self.change_y *= -1


    #methode dessiner balle sur la fenetre
    def draw(self):
        arcade.draw_rectangle_filled(self.centre_x, self.centre_y, self.width, self.height, self.color,self.angle)

#class MyGame definir les objets balle et rectangle et le jeu, qui permet d'afficher (dessiner) ces objets sur l'ecran selon le bouton clique
class MyGame(arcade.Window):
    def __init__(self):
        #creer la fenetre arcade
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "TP4")

        #crer la liste de balles et de rectangle qui sont tout les deux vides
        self.liste_balles= []
        self.liste_rectangles= []


    #methode on_draw qui permet de mettre en action fonction dessiner l'objet balle et rectangle selon un loop
    def on_draw(self):
        arcade.start_render()
        for balle in self.liste_balles:
            balle.draw()
        for rectangle in self.liste_rectangles:
            rectangle.draw()

    #methode on_update qui permet de mettre en action fonction changer position l'objet balle et rectangle selon un loop
    def on_update(self, delta_time: float):
        for balle in self.liste_balles:
            balle.on_update()
        for rectangle in self.liste_rectangles:
            rectangle.on_update()



    #methode: pour permetre d'afficher une balle est un rectangle a l'ecran l'endroit du clic respectivement selon le boutton gauche et droit
    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):

        #condition pour verifier si le boutton gauche est cllique
        if button == arcade.MOUSE_BUTTON_LEFT:

            #definir les valeurs des attributs de l'objet balle
            rayon = random.randint(10, 30)
            change_x = random.randint(1,10)
            change_y = random.randint(1,10)
            color = random.choice(COLORS)

            #associer variable balle a l`objet Balle
            balle = Balle(rayon, x, y, change_x, change_y, color)

            #ajouter un objet balle a la liste de balles
            self.liste_balles.append(balle)

        #condition pour verifier si le boutton droit est clique
        if button == arcade.MOUSE_BUTTON_RIGHT:

            #definir les valeurs des attributs de l'objet balle
            change_x = random.randint(1,10)
            change_y = random.randint(1,10)
            width = 50
            height = 30
            angle = 0.00
            color = random.choice(COLORS)

            #associer variable rectangle a l`objet Rectangle
            rectangle = Rectangle(x, y, change_x, change_y,width, height, color, angle)

            #ajouter un objet rectangle a la liste de rectangle
            self.liste_rectangles.append(rectangle)



#methode main:fait appel au class MyGame et tout son contenu et au fonction arcade.run pour faire fonctionner le jeu
def main():
    MyGame()
    arcade.run()

#appel au methode main
main()