import arcade

import game_state


class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(800, 800, "TP5")

        self.game_state = game_state.GameState.GAME_NOT_STARTED

        self.reset_round()

        self.sprite_list = arcade.SpriteList()
        self.sprite_list.append(arcade.Sprite("assets/faceBeard.png", scale=0.35, center_x=175, center_y=350, ))
        self.sprite_list.append(arcade.Sprite("assets/compy.png", scale=1.5, center_x=625, center_y=350, ))
    def reset_round(self):
        self.pointage_user = 0
        self.pointage_bot = 0

    def on_draw(self):
        arcade.start_render()
        arcade.set_background_color(arcade.color.BLACK_OLIVE)

        if self.game_state == game_state.GameState.GAME_NOT_STARTED:
            arcade.draw_text("Roche, Papier, Ciseaux", start_x= 195, start_y= 750, font_size=30, color=arcade.color.RED)
            arcade.draw_text("Appuyer sur espace pour commencer", start_x=185, start_y=700, font_size=20, color=arcade.color.LIGHT_BLUE)
        if self.game_state == game_state.GameState.ROUND_ACTIVE:
            self.not_moving_image()
            arcade.draw_text("Choisissez votre attaque", start_x= 195, start_y= 600, font_size=30, color=arcade.color.LIGHT_BLUE)

        if self.game_state == game_state.GameState.ROUND_DONE:
            pass

        if self.game_state == game_state.GameState.GAME_OVER:
            pass


    def not_moving_image(self):
        arcade.draw_text(text = "Pointage User: %d"%self.pointage_user, start_x=100, start_y=100, font_size=15, color=arcade.color.LIGHT_BLUE)
        arcade.draw_text(text = "Pointage Bot: %d"%self.pointage_bot, start_x=550, start_y=100, font_size=15, color=arcade.color.LIGHT_BLUE)

        arcade.draw_rectangle_outline(center_x=125, center_y=200, width=45, height=45, color=arcade.color.RED)
        arcade.draw_rectangle_outline(center_x=175, center_y=200, width=45, height=45, color=arcade.color.RED)
        arcade.draw_rectangle_outline(center_x=225, center_y=200, width=45, height=45, color=arcade.color.RED)
        arcade.draw_rectangle_outline(center_x=625, center_y=200, width=45, height=45, color=arcade.color.RED)

        self.sprite_list.draw()



    def on_key_press(self, symbol, modifiers):

        if symbol == 32 and self.game_state == game_state.GameState.GAME_NOT_STARTED:
            self.game_state = game_state.GameState.ROUND_ACTIVE





def main():
    game = MyGame()
    game.on_draw
    game.not_moving_image()
    arcade.run()






main()
