import arcade
import random

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800


COULEUR = [arcade.color.GOLDEN_YELLOW, arcade.color.DARK_TURQUOISE, arcade.color.DEEP_PINK, arcade.color.MEDIUM_SPRING_GREEN, arcade.color.MEDIUM_SLATE_BLUE, arcade.color.DARK_ORANGE, arcade.color.SEA_GREEN]
rayon = random.randint(10, 70)
center_x = random.randint(0, SCREEN_WIDTH - rayon)
center_y = random.randint(0, SCREEN_HEIGHT - rayon)
color = random.choice(COULEUR)
def main():
    window = arcade.Window(SCREEN_WIDTH,SCREEN_HEIGHT, "screen dimentions")

main()
class MyGame():
    def setup(self):

        cercle = (rayon, center_x, center_y, color)
    def on_draw(self):
        arcade.start_render()
        for _ in range(20):
            arcade.draw_circle_filled(cercle)




def start():
        my_game = MyGame()
        my_game.setup()
        my_game.on_draw()

        arcade.run()
start()







