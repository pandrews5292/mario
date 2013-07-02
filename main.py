import os
import sys
import random
import time
import pygame
from pygame.locals import * 
import utils

BACKGROUND_COLOR = (135, 206, 250)
SCREEN_SIZE = (800, 500)

class Floor(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.image, self.rect = utils.load_image('bricks.png')
        self.x = 0
        self.y = 500

    def update(self):
        if self.rect.right - 20 < self.area.right:
            self.x = 0
        self.rect.bottomleft = (self.x, self.y)

    def slide(self):
        self.x -= 10


def main():
    #sky blue background color

    pygame.init()

    screen = pygame.display.set_mode((800, 500))
    pygame.display.set_caption('MARIO')
    background = pygame.Surface(screen.get_size())

    background.fill(BACKGROUND_COLOR)
    background = background.convert()
        
    #allsprites = pygame.sprite.RenderPlain((mario))   

    game_over = False

    hud = utils.HUD()

    clock = pygame.time.Clock()
    pygame.key.set_repeat(50,50)


    while not game_over:
        clock.tick(60)
        hud.get_time()
        hud.print_hud(background)

        
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
