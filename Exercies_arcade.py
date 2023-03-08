import arcade
import random
from math import pi

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

COLORS = [arcade.color.BLUE, arcade.color.FANDANGO_PINK,arcade.color.GOLDEN_POPPY, arcade.color.GOLDEN_POPPY]

class Cercle():
   def __init__(self,rayon,x,y,color):
       self.rayon = rayon
       self.centre_x = x
       self.centre_y = y
       self.color = color

   def draw(self):
       arcade.draw_circle_filled(self.centre_x, self.centre_y, self.rayon, self.color)



class MyGame(arcade.Window):
   def __init__(self):
       super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Exercice #1")
       self.liste_cercles = []

   def setup(self):
       # remplir la liste avec 20 objets de type Cercle
       for _ in range(20):
           rayon = random.randint(10, 50)
           centre_x = random.randint(0 + rayon, SCREEN_WIDTH - rayon)
           centre_y = random.randint(0 + rayon, SCREEN_HEIGHT - rayon)
           color = random.choice(COLORS)
           cercle = Cercle(rayon,centre_x,centre_y,color)
           self.liste_cercles.append(cercle)



   def on_draw(self):
       arcade.start_render()

       for cercle in self.liste_cercles:
           cercle.draw()

   def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
       aire_cercle = pi * rayon ** 2 #aire d'un cercle c'est pi*r**2
       if button == arcade.MOUSE_BUTTON_LEFT:
           #cercle == coordonnes point dans leqeul il y a le point x et y
           #if x & y fait partie aire_cerlce:
            #cercle_changement=cercle(rayon) #identifier cercle qui doit subir changement
            #liste_cerlce.remove(cercle()) #enlever le cercle avec les coordones identifies de la liste


           print("Left mouse button pressed at", x, y)

       if button == arcade.MOUSE_BUTTON_RIGHT:
           #identifier ou button est appuye
            #change couleur(color.random.choice)
           print("Right mouse button pressed at", x, y)


def main():
   my_game = MyGame()
   my_game.setup()

   arcade.run()


main()

