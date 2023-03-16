import arcade
import random


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

COLORS = [arcade.color.BLUE, arcade.color.FANDANGO_PINK,arcade.color.GOLDEN_POPPY, arcade.color.GOLDEN_POPPY]

class Balle():

   def __init__(self,rayon,x,y,color):
       self.rayon = rayon
       self.centre_x = x
       self.change_x = deplacement_x
       self.change_y = deplacement_y
       self.centre_y = y
       self.color = color


   def draw(self):
       arcade.draw_circle_filled(self.centre_x, self.centre_y, self.rayon, self.color)



class MyGame(arcade.Window):

   def __init__(self):

       super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Exercice #1")

       self.liste_cercles = []


   def setup(self):

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


def main():
   my_game = MyGame()
   my_game.setup()
   arcade.run()


main()