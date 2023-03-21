import arcade
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

COLORS = [arcade.color.BLUE, arcade.color.FANDANGO_PINK,arcade.color.GOLDEN_POPPY, arcade.color.TURQUOISE_BLUE,arcade.color.SPRING_GREEN,arcade.color.RED,arcade.color.LAVENDER_INDIGO]

class Balle():
    def __init__(self, rayon,position_x,position_y, vitesse_deplacement_x, vitesse_deplacement_y, couleur):
        self.rayon = rayon
        self.centre_x = position_x
        self.centre_y = position_y
        self.change_x = vitesse_deplacement_x
        self.change_y = vitesse_deplacement_y
        self.color = couleur

    def on_update(self):
        self.centre_x += self.change_x
        self.centre_y += self.change_y

        if self.centre_x < self.rayon:
            self.change_x *= -1

        if self.centre_x > SCREEN_WIDTH - self.rayon:
            self.change_x *= -1

        if self.centre_y < self.rayon:
            self.change_y *= -1

        if self.centre_y > SCREEN_HEIGHT - self.rayon:
            self.change_y *= -1



    def draw(self):
        arcade.draw_circle_filled(self.centre_x, self.centre_y, self.rayon, self.color)


class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Exercice #1")
        self.liste_balles= []
    def on_draw(self):
        arcade.start_render()
        for balle in self.liste_balles:
            balle.draw()

    def on_update(self, delta_time: float):
        for balle in self.liste_balles:
            balle.on_update()

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):

        if button == arcade.MOUSE_BUTTON_LEFT:


            rayon = random.randint(10, 50)
            change_x = random.randint(1,10)
            change_y = random.randint(1,10)
            color = random.choice(COLORS)
            balle = Balle(rayon, x, y, change_x, change_y, color)
            self.liste_balles.append(balle)




def main():
    my_game = MyGame()


    arcade.run()


main()
