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

    def draw_floor(self, background):
        cur = self.x
        background.blit(self.image, (self.x, self.y))
        for i in range(15):
            cur += 145
            background.blit(self.image, (cur, self.y)) 
 
    
def main():
    #sky blue background color

    pygame.init()

    screen = pygame.display.set_mode((800, 500))
    pygame.display.set_caption('MARIO')
    background = pygame.Surface(screen.get_size())

    background.fill(BACKGROUND_COLOR)
    background = background.convert()

    floor = Floor()
        
    #allsprites = pygame.sprite.RenderPlain((floor))   

    game_over = False

    hud = utils.HUD()

    clock = pygame.time.Clock()
    pygame.key.set_repeat(50,50)


    while not game_over:
        clock.tick(60)
        hud.get_time()
        hud.print_hud(background)
        floor.draw_floor(background)


        
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit(0)
            elif event.type == KEYDOWN:
                keys = pygame.key.get_pressed()
               

        #allsprites.update()
        screen.blit(background, (0, 0))
        #allsprites.draw(screen)
        pygame.display.flip()

                

                
        
    


    

main();
