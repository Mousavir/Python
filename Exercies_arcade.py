import arcade
import random

#la largeur de l'ecran est de 800
#l'hauteur de l'ecran est de 600
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

#la variable COLORS est egale a la liste contenant 4 couleurs de la banque arcade
COLORS = [arcade.color.BLUE, arcade.color.FANDANGO_PINK,arcade.color.GOLDEN_POPPY, arcade.color.GOLDEN_POPPY]

#creer l'objet cercle
class Cercle():
    #definir les caracterstiques du sercle donc ses parametres soit le rayon le centre_x, le centre_y et la couleur qui ne sont pas encore concretement definit
   def __init__(self,rayon,x,y,color):
       self.rayon = rayon
       self.centre_x = x
       self.centre_y = y
       self.color = color

    #fonction draw  ui dessine un cercle remplie base sur les propriete du cercle definit ci-haut
   def draw(self):
       arcade.draw_circle_filled(self.centre_x, self.centre_y, self.rayon, self.color)


#definir les cercle en question base sur les caracteristiques de l'objet cercle cree
class MyGame(arcade.Window):

   def __init__(self):
       # crer les caracteristiques des mesures de l'ecran
       super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Exercice #1")
       # la liste cercle est un liste vide
       self.liste_cercles = []

    #fonctin setup
   def setup(self):
       # remplir la liste avec 20 objets de type Cercle
       for _ in range(20):
           rayon = random.randint(10, 50)
           centre_x = random.randint(0 + rayon, SCREEN_WIDTH - rayon)
           centre_y = random.randint(0 + rayon, SCREEN_HEIGHT - rayon)
           color = random.choice(COLORS)
           #la varible cercle est egale a l'objet cercle feniit avec les caracteristiques numeriques d'un cercle
           cercle = Cercle(rayon,centre_x,centre_y,color)
           #ajouter les cercle a la liste vide
           self.liste_cercles.append(cercle)

    #methode on_draw
   def on_draw(self):
       #permet a arcade de commencer a dessiner
       arcade.start_render()
        #pour chaque cercle dans la liste desiner un cercle
       for cercle in self.liste_cercles:
           cercle.draw()

    #mehode on mouse presse qui detecte quel button est clique et puis par la suite soit emeleve le cercle clique (gauche) ou change la couleur du cerlce clique (droite)
   def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
       #si le boutton gauche du souris est clique
       if button == arcade.MOUSE_BUTTON_LEFT:
           #pour chaque cercle dans la liste de cercle
           for cercle in self.liste_cercles:
               #verifier si le x et le y des coordones du point clique avec le souris sont plus petit et plus grand que la surface du cercle (se retrouvent dans le cercle base sur le rayon du cercle et les coordones de son centre
               if x < cercle.centre_x + cercle.rayon and cercle.centre_x + cercle.rayon < x and y < cercle.centre_y + cercle.rayon and cercle.centre_y + cercle.rayon < y:
                    #enlever le cercle en question (cercle clique) de la liste
                    self.liste_cercles.remove(cercle)


       elif button == arcade.MOUSE_BUTTON_RIGHT:
           for cercle in self.liste_cercles:
           # verifier si le x et le y des coordones du point clique avec le souris sont plus petit et plus grand que la surface du cercle (se retrouvent dans le cercle base sur le rayon du cercle et les coordones de son centre
                if x < cercle.centre_x + cercle.rayon and cercle.centre_x + cercle.rayon < x and y < cercle.centre_y + cercle.rayon and cercle.centre_y + cercle.rayon < y:
                    #changer la couleur du cercle en question (cercle clique) en rendant son propritete de couleur au hasard
                        cercle.color = random.choice

#fonction main qui fait appel a la classe my_game et ses conetues et met en action aracde
def main():
   my_game = MyGame()
   my_game.setup()
   arcade.run()

#appel a la fonction main
main()

