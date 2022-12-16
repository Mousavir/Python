import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WINDOW_TITLE = "Tests"

arcade.open_window(SCREEN_WIDTH,SCREEN_HEIGHT, WINDOW_TITLE)

arcade.set_background_color(arcade.color.SKY_BLUE)

arcade.start_render()
arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT /2, 0, arcade.csscolor.DARK_GREEN)
arcade.draw_rectangle_filled(200, SCREEN_HEIGHT /2 ,30, 60, arcade.csscolor.BROWN)
arcade.draw_circle_outline(200,200,60, arcade.color.BUBBLE_GUM, num_segments = 8, tilt_angle=35)
arcade.draw_circle_outline(400,200,60,arcade.color.BUBBLE_GUM, num_segments = 8)
arcade.finish_render()
arcade.run()