import arcade
import random


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

COLORS = [arcade.color.BLUE, arcade.color.FANDANGO_PINK,arcade.color.GOLDEN_POPPY, arcade.color.TURQUOISE_BLUE,arcade.color.SPRING_GREEN,arcade.color.RED,arcade.color.LAVENDER_INDIGO]

class Cercle():

   def __init__(self,rayon,x,y,color):
       self.rayon = rayon
       self.centre_x = x
       self.centre_y = y
       self.color = color

   def on_update(self):
       cercle_centre_x += cercle_change_x
       cercle_centre_y += cercle_change_y

       if cercle_centre_x < rayon_cercle:
           pass
       if cercle_centre_x > SCREEN_WIDTH - rayon_cercle:
           pass
       if cercle_centre_y < rayon_cercle:
           pass
       if cercle_centre_y > SCREEN_HEIGHT - rayon_cercle:
           pass

       if cercle_x < rayon_cercle:
           cercle_x *= -1
   def draw(self):
       arcade.draw_circle_filled(self.centre_x, self.centre_y, self.rayon, self.color)



class MyGame(arcade.Window):

   def __init__(self):

       super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Exercice #1")

       self.liste_balles = []


   def setup(self):

       for _ in range(20):
           rayon = random.randint(10, 30)
           centre_x = random.randint(0 + rayon, SCREEN_WIDTH - rayon)
           centre_y = random.randint(0 + rayon, SCREEN_HEIGHT - rayon)
           color = arcade.color
           balle = Balle(rayon,centre_x,centre_y,color)


   def on_draw(self):

       arcade.start_render()

       for cercle in self.liste_cercles:
           cercle.draw()


   def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):

       if button == arcade.MOUSE_BUTTON_LEFT:

           for cercle in self.liste_cercles:

               if x < cercle.centre_x + cercle.rayon and cercle.centre_x - cercle.rayon < x and y < cercle.centre_y + cercle.rayon and cercle.centre_y - cercle.rayon < y:

                    self.liste_cercles.remove(cercle)


       elif button == arcade.MOUSE_BUTTON_RIGHT:
           for cercle in self.liste_cercles:

                if x < cercle.centre_x + cercle.rayon and cercle.centre_x - cercle.rayon < x and y < cercle.centre_y + cercle.rayon and cercle.centre_y - cercle.rayon < y:

                        cercle.color = random.choice(COLORS)


def main():
   my_game = MyGame()
   my_game.setup()
   arcade.run()


main()

