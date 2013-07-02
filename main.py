import os
import sys
import random
import time
import pygame
from pygame.locals import * 
from utils import *

BACKGROUND_COLOR = (135, 206, 250)
SCREEN_SIZE = (800, 500)

class Floor(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.image, self.rect = load_image('bricks.png')
        self.x = 0
        self.y = 500

    def update(self):
        if self.rect.right - 20 < self.area.right:
            self.x = 0
        self.rect.bottomleft = (self.x, self.y)

    def slide(self):
        self.x -= 10
        

class TimeCount():
    def __init__(self):
        self.start_time = time.time()
        self.time_over = False
        self.t_count_pos = (710, 50) 
        self.t_pos = (701, 30)

    def is_time_up(self):
        return self.time_over

    def get_time(self):
        if self.time_over:
            self.cur_time = 0
        else:
            self.cur_time = int(1000 - (time.time() - self.start_time))
            if (self.cur_time <= 0):
                self.time_over = True


    def print_time(self, background):
        font = pygame.font.Font(None, 36)
        timer_text = font.render("TIME", 1, (0, 0, 0))
        time_text = font.render(str(self.cur_time), 1, (0, 0, 0))
        
        timer_pos = timer_text.get_rect(center=self.t_pos)
        time_pos = time_text.get_rect(center=self.t_count_pos)
        
        background.fill(BACKGROUND_COLOR)
        background.blit(time_text, time_pos)
        background.blit(timer_text, timer_pos)

class Mario(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.image, self.rect = load_image('mario.png', (0, 0, 0))
        self.x = 50
        self.y = 450

    def update(self):
        self.rect.bottom = self.area.bottom


def main():
    #sky blue background color

    pygame.init()

    screen = pygame.display.set_mode((800, 500))
    pygame.display.set_caption('MARIO')
    background = pygame.Surface(screen.get_size())

    background.fill(BACKGROUND_COLOR)
    mario = Mario()
        

    allsprites = pygame.sprite.RenderPlain((mario))   

    screen.blit(background, (0, 0))
    pygame.display.flip()

    game_over = False
    timer = TimeCount()
    clock = pygame.time.Clock()
    pygame.key.set_repeat(50,50)


    
    while not game_over:
        clock.tick(60)
        timer.get_time()
        timer.print_time(background)
        
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit(0)
            elif event.type == KEYDOWN:
                keys = pygame.key.get_pressed()
               

        allsprites.update()
        screen.blit(background, (0, 0))
        allsprites.draw(screen)
        pygame.display.flip()

                

                
        
    


    

main();
