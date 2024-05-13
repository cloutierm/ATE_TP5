import arcade, game_state, attack_animations, random, time


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

        self.rock = attack_animations.AttackAnimations(attack_type=attack_animations.AttackType.ROCK, pos_x=100, pos_y=200)
        self.paper = attack_animations.AttackAnimations(attack_type=attack_animations.AttackType.PAPER, pos_x=175, pos_y=200)
        self.scissors = attack_animations.AttackAnimations(attack_type=attack_animations.AttackType.SCISSORS, pos_x=250, pos_y=200)
        self.bot_attack = attack_animations.AttackAnimations(attack_type=attack_animations.AttackType.BOT, pos_x=625, pos_y=200)

        self.draw_attacks = True

        self.draw_paper= True
        self.draw_rock = True
        self.draw_scissors = True

        self.update_paper = True
        self.update_rock = True
        self.update_scissors = True

        self.has_chosen_attack = False

        self.draw_bot_attack = False
        self.update_bot_attack = False


    def draw_attacks_animations(self):

        if self.update_rock: self.rock.on_update()
        if self.update_paper: self.paper.on_update()
        if self.update_scissors: self.scissors.on_update()

        if self.draw_rock: self.rock.draw()
        if self.draw_paper: self.paper.draw()
        if self.draw_scissors: self.scissors.draw()

        if self.draw_bot_attack: self.bot_attack.draw()
        if self.draw_bot_attack: self.bot_attack.on_update()

    def on_draw(self):
        arcade.start_render()
        arcade.set_background_color(arcade.color.BLACK_OLIVE)

        if self.game_state == game_state.GameState.GAME_NOT_STARTED:
            arcade.draw_text("Roche, Papier, Ciseaux", start_x= 195, start_y= 750, font_size=30, color=arcade.color.RED)
            arcade.draw_text("Appuyer sur espace pour commencer", start_x=185, start_y=700, font_size=20, color=arcade.color.LIGHT_BLUE)
        if self.game_state == game_state.GameState.ROUND_ACTIVE:
            self.not_moving_image()
            arcade.draw_text("Choisissez votre attaque", start_x= 195, start_y= 600, font_size=30, color=arcade.color.LIGHT_BLUE)

            if self.draw_attacks: self.draw_attacks_animations()


        if self.game_state == game_state.GameState.ROUND_DONE:
            pass

        if self.game_state == game_state.GameState.GAME_OVER:
            pass


    def not_moving_image(self):
        arcade.draw_text(text = "Pointage User: %d"%self.pointage_user, start_x=100, start_y=100, font_size=15, color=arcade.color.LIGHT_BLUE)
        arcade.draw_text(text = "Pointage Bot: %d"%self.pointage_bot, start_x=550, start_y=100, font_size=15, color=arcade.color.LIGHT_BLUE)

        arcade.draw_rectangle_outline(center_x=100, center_y=200, width=65, height=65, color=arcade.color.RED)
        arcade.draw_rectangle_outline(center_x=175, center_y=200, width=65, height=65, color=arcade.color.RED)
        arcade.draw_rectangle_outline(center_x=250, center_y=200, width=65, height=65, color=arcade.color.RED)
        arcade.draw_rectangle_outline(center_x=625, center_y=200, width=65, height=65, color=arcade.color.RED)

        self.sprite_list.draw()



    def on_key_press(self, symbol, modifiers):

        if symbol == 32 and self.game_state == game_state.GameState.GAME_NOT_STARTED:
            self.game_state = game_state.GameState.ROUND_ACTIVE


    def on_mouse_press(self, x, y, button, modifiers):
        if self.game_state == game_state.GameState.ROUND_ACTIVE and self.has_chosen_attack == False and (self.rock.collides_with_point((x, y)) or self.scissors.collides_with_point((x, y)) or self.paper.collides_with_point((x, y))):
            self.has_chosen_attack = True

            if self.rock.collides_with_point((x, y)):
                self.update_rock = False

                self.draw_paper = False
                self.draw_scissors = False

            if self.paper.collides_with_point((x, y)):
                self.update_paper = False

                self.draw_rock = False
                self.draw_scissors = False

            if self.scissors.collides_with_point((x, y)):
                self.update_scissors = False

                self.draw_paper = False
                self.draw_rock = False

            self.draw_bot_attack = True
            self.update_bot_attack = True





def main():
    game = MyGame()
    game.on_draw
    game.not_moving_image()
    arcade.run()






main()


