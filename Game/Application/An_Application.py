import pygame

from Application.Display.Measurements import *
from Application.Container.container import *
from Application.Display.Close import close_game_function
from Application.Default_Object.Keyboard_Movement import key_pressed_conditions
from pygame import mixer

class Application(DisplayMeasurements,Container):
    def __init__(self):
        DisplayMeasurements.__init__(self) #screen measurements

        Container.__init__(self)  # All elements to be display

        self.victory = None
        self.clock = pygame.time.Clock()

    def set_victory(self, victory):
        self.victory = victory

    def run(self):

        mixer.init()
        mixer.music.load('Application/Background_music/background_music.mp3')
        mixer.music.play()


        pygame.init()
        self.gameDisplay = pygame.display.set_mode((self.display_width, self.display_height))
        won = 0
        while True:
            close_game_function()
            self.gameDisplay.fill((0, 0, 0))
            #run all in container.
            for category, array in self.container.items():
                for element in array:
                    self.gameDisplay.blit(element.img,(element.x, element.y))

            for element in self.container['mushroom']:
                condition_1 = self.container['player'][0].x > element.x - 110
                condition_2 = self.container['player'][0].x < element.x + 60
                condition_3 = self.container['player'][0].y > element.y - 90
                condition_4 = self.container['player'][0].y < element.y + 60
                if condition_1 and condition_2 and condition_3 and condition_4:
                    self.container['player'][0].set_color(element.character_img_transformation)
                    self.container['player'][0].set_images_movements('left', [f'Left_{element.character_img_transformation}/1.png', f'Left_{element.character_img_transformation}/2.png',f'Left_{element.character_img_transformation}/3.png'])
                    self.container['player'][0].set_images_movements('right', [f'Right_{element.character_img_transformation}/1.png', f'Right_{element.character_img_transformation}/2.png', f'Right_{element.character_img_transformation}/3.png'])
                    self.container['player'][0].set_images_movements('top', [f'Top_{element.character_img_transformation}/1.png', f'Top_{element.character_img_transformation}/2.png', f'Top_{element.character_img_transformation}/3.png'])
                    self.container['player'][0].set_images_movements('down', [f'Down_{element.character_img_transformation}/1.png', f'Down_{element.character_img_transformation}/2.png', f'Down_{element.character_img_transformation}/3.png'])

            key_pressed = pygame.key.get_pressed()
            key_pressed_conditions(key_pressed, self.container['player'][0],self.container['mushroom'] + self.container['walls'] + self.container['victory_flag'],
                                   self.container['player'][0].left,
                                   self.container['player'][0].right,
                                   self.container['player'][0].top,
                                   self.container['player'][0].down)

            #If player wins breaks
            condition_1 = self.container['player'][0].x > self.container['victory_flag'][0].x - 100
            condition_2 = self.container['player'][0].y > self.container['victory_flag'][0].y - 82
            condition_3 = self.container['player'][0].x < self.container['victory_flag'][0].x + self.container['victory_flag'][0].img.get_width() - 20
            condition_4 = self.container['player'][0].y < self.container['victory_flag'][0].y + self.container['victory_flag'][0].img.get_height() - 20
            if condition_1 and condition_2 and condition_3 and condition_4:
                won += 1
                if won > 20:
                    break #won
            self.clock.tick(40)
            pygame.display.update()

        mixer.music.stop()
        mixer.music.load('Application/Background_music/victory.mp3')
        mixer.music.play()
        while True:
            close_game_function()
            self.gameDisplay.fill((0, 0, 0))
            self.gameDisplay.blit(self.victory.img, (self.victory.x, self.victory.y))

            self.clock.tick(40)
            pygame.display.update()



