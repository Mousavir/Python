import arcade
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

COLORS = [arcade.color.BLUE, arcade.color.FANDANGO_PINK, arcade.color.FRENCH_ROSE, arcade.color.GOLDEN_POPPY]

class Cercle():
  def __init__(self, r, cx, cy, color):
      self.rayon = r
      self.centre_x = cx
      self.centre_y = cy
      self.color = color

  def draw(self):
      arcade.draw_circle_filled(self.rayon, self.centre_x, self.centre_y, self.color)


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
          cercle = Cercle(rayon, centre_x, centre_y, color)
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

