import os
import sys
import random
import time
import pygame
from pygame.locals import * 
import utils

BACKGROUND_COLOR = (135, 206, 250)
SCREEN_SIZE = (800, 500)

class Enemy(pygame.sprite.Sprite):
    def __init__(self, enemy_type=None):
        pygame.sprite.Sprite.__init__(self)
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.type = enemy_type
        self.image, self.rect = utils.load_image('goomba.png', -1)
        self.rect.topleft = (150, 193)
        self.moving_right = 0
        self.moving_left = 0
        self.still = 1

       
    def move_left(self):
        self.moving_left = 1
        if (self.rect.center[0] - 30 > self.area.left):
            self.rect.move_ip(-5, 0)
    
    def move_right(self):
        if (self.rect.center[0] < self.area.center[0]):
            self.rect.move_ip(5, 0)
        else:
            self.moving_right = 1

    def update(self):
        self.moving_right = 0
        self.moving_left = 0

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
        self.floor_boards.append([self.image, self.x, self.y])
        for i in range(50):
            new_floor = pygame.Surface.copy(self.image)
            cur += 145
            background.blit(new_floor, (cur, self.y)) 
            self.floor_boards.append([new_floor, cur, self.y])
        print self.floor_boards

def shift_game_objects(mario, objects, background, clean_background):
    background.blit(clean_background, Rect(0, 370, 30, 800))

    for o in objects:
        if (mario.moving_right == 1):
            o[1] -= 5
        background.blit(o[0], (o[1], o[2]))

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
    goomba = Enemy()
    floor.draw_floor(background)

        
    allsprites = pygame.sprite.RenderPlain((goomba))   

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
                    goomba.move_right()
                    shift_game_objects(goomba, floor.floor_boards, background, clean_background)

                if keys[K_LEFT]:
                    goomba.move_left()
                    shift_game_objects(goomba, floor.floor_boards, background, clean_background)

        screen.blit(background, (0, 0))
        allsprites.draw(screen)
        pygame.display.flip()
        goomba.update()

                

                
        
    


    

main();
