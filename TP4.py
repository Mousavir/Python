import arcade
import random

class MyGame(arcade.Window):
   def __init__(self, width, height, title):
       # Call the parent class's init function
       super().__init__(width, height, title)


def main():

   window = MyGame(640, 480, "Drawing Example")

   arcade.run()
main()

couleur = random.randint()











transparency = random.random(0,256)
transparent = random.random(0,256)
opacity = random.random(0,256)

couleur = (transparency, transparent, opacity)

position = random.random((0,620))
yposition = random.random(0,460)
def on_draw(self):
   arcade.start_render()

   arcade.draw_circle_filled(position, yposition, (couleur))

on_draw()





