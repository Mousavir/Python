import arcade
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

COLORS = [arcade.color.BLUE, arcade.color.FANDANGO_PINK,
arcade.color.FRENCH_ROSE, arcade.color.GOLDEN_POPPY]

class Balle():
    def __init__(self, rayon,position_x,position_y, vitesse_deplacement_x, vitesse_deplacement_y, couleur):
        self.rayon = rayon
        self.centre_x = position_x
        self.centre_y = position_y
        self.change_x = vitesse_deplacement_x
        self.change_y = vitesse_deplacement_y
        self.color = couleur
        cercle = Balle(rayon,centre_x,cercle_y.change_x, change_y, color)
    def on_update(self):
        cercle_centre_x += cercle_change_x
        cercle_centre_y += cercle_change_y

        if cercle_x
    def draw(self):
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
            cercle= Cercle(rayon, center_x, center_y, color)
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
