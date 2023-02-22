import arcade
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

COLORS = [arcade.color.BLUE, arcade.color.FANDANGO_PINK,
          arcade.color.FRENCH_ROSE, arcade.color.GOLDEN_POPPY]


class Cercle():
    def __init__(self, r, x, y, c):
        self.rayon = r
        self.centre_x = x
        self.centre_y = y
        self.color = (c)

    def draw(self):
        # arcade.draw_circle_filled(center_x, center_y, rayon, color)
        arcade.draw_circle_filled(self.centre_x, self.centre_y, self.rayon, self.color)


class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Exercice #1")
        self.liste_cercles = []

    def setup(self):
        for _ in range(20):
            rayon = random.randint(10, 50)
            center_x = random.randint(0 + rayon, SCREEN_WIDTH - rayon)
            center_y = random.randint(0 + rayon, SCREEN_HEIGHT - rayon)
            color = random.choice(COLORS)
            cercle = Cercle(rayon, center_x, center_y, color)
            self.liste_cercles.append(cercle)

    def on_update(self):
        cercle_change_x = 3
        cercle_change_y = 3
        cercle_x += cercle_change_x
        cercle_y += cercle_change_y
        if cercle_x < rayon_cercle:
            pass
        if cercle_x > SCREEN_WIDTH - rayon_cercle:
            pass
        if cercle_y < rayon_cercle:
            pass
        if cercle_y > SCREEN_HEIGHT - rayon_cercle:
            pass
        if cercle_x < rayon_cercle:
            cercle_x *= -1

    def on_draw(self):
        arcade.start_render()
        for cercle in self.liste_cercles:
            cercle.draw()

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        if button == arcade.MOUSE_BUTTON_LEFT:

        if button == arcade.MOUSE_BUTTON_RIGHT:




def main():
    my_game = MyGame()
    my_game.setup()

    arcade.run()


main()
