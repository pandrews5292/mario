import os
import sys
import random
import time
import pygame
from pygame.locals import * 
import utils

BACKGROUND_COLOR = (135, 206, 250)
SCREEN_SIZE = (800, 500)

class Floor():
    def __init__(self):
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.image, self.rect = utils.load_image('bricks.png', -1, 1)
        self.x = -610
        self.y = -20
        self.floor_boards = []

    def draw_floor(self, background):
        cur = self.x
        background.blit(self.image, (self.x, self.y))
        self.floor_boards.append(self.image)
        for i in range(5):
            new_floor = pygame.Surface.copy(self.image)
            cur += 145
            background.blit(new_floor, (cur, self.y)) 
            self.floor_boards.append(new_floor)
        print self.floor_boards

    def walk(self, background, clean_background):
        for i in range(6):
            self.floor_boards[i].get_rect().move_ip(-5, 0)

class Camera():
    def __init__(self, camera_func, width, height):
        self.camera_func = camera_func
        self.state = Rect(0, 0, width, height)

    def apply(self, target):
        return target.rect.move(self.state.topleft)

    def update(self, target):
        self.state = self.camera_func(self.state, target.rect)
 
    
def main():
    #sky blue background color

    pygame.init()

    screen = pygame.display.set_mode((800, 500))
    pygame.display.set_caption('MARIO')
    background = pygame.Surface(screen.get_size())
    

    background.fill(BACKGROUND_COLOR)
    background = background.convert()
    clean_background = pygame.Surface.copy(background)

    floor = Floor()
    floor.draw_floor(background)

        
    #allsprites = pygame.sprite.RenderPlain()   

    game_over = False

    hud = utils.HUD()
    hud.set_up_statics(background)


    clock = pygame.time.Clock()
    pygame.key.set_repeat(50,50)



    while not game_over:
        clock.tick(60)
        hud.update_time(background, clean_background)
        hud.load_cur_world(background, clean_background)
        hud.load_cur_num_lives(background, clean_background)
        hud.load_score(background, clean_background)
        hud.load_num_coins(background, clean_background)

        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit(0)
            elif event.type == KEYDOWN:
                keys = pygame.key.get_pressed()
                if keys[K_RIGHT]:
                    floor.walk()
               

        #allsprites.update()
        screen.blit(background, (0, 0))
        #allsprites.draw(screen)
        pygame.display.flip()

                

                
        
    


    

main();
