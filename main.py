import os
import sys
import random
import time
import pygame
from pygame.locals import * 
import utils

BACKGROUND_COLOR = (135, 206, 250)
SCREEN_SIZE = (800, 500)
FLOOR_Y = 440

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.image, self.rect = utils.load_image('goomba.png', -1)
        self.gravity = .5
        self.right_key_pressed = False
        self.left_key_pressed = False
        self.jump_key_pressed = False
        self.jumping = False
        self.x_vel = 0
        self.y_vel = -10
        self.x_pos = 300
        self.y_pos = FLOOR_Y
        self.rect.center = (self.x_pos, self.y_pos)

        
    def move(self, direction):
        if direction == "R":
            self.right_key_pressed = True
        elif direction == "L":
            self.left_key_pressed = True

    def jump(self):
        self.jump_key_pressed = True

    def reset(self):
        self.jump_key_pressed = False
        self.right_key_pressed = False
        self.left_key_pressed = False
  
    def update(self):
        if (not self.jumping and self.jump_key_pressed):
            self.y_vel = -10
            self.jumping = True
        if self.jumping:
            if (self.rect.center[1] + self.y_vel < FLOOR_Y + 10):
                self.y_pos += self.y_vel
                self.y_vel += self.gravity
            else:
                self.jumping = False

        if self.left_key_pressed and self.rect.midleft[0] > 0:
            self.x_vel = -8

        elif self.right_key_pressed and self.rect.midright[0] < 400:
            self.x_vel = 8
        
        else:
            self.x_vel = 0

        self.x_pos += self.x_vel
        self.rect.center = (self.x_pos, self.y_pos)
        self.reset()                                    

 
class Floor():
    def __init__(self):
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.image, self.rect = utils.load_image('bricks.png', -1, 1)
        self.x = -5
        self.y = 464
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


def shift_game_objects(mario, objects, background, clean_background):
    background.blit(clean_background, Rect(0, 370, 30, 800))

    for o in objects:
        if (mario.right_key_pressed == True and mario.rect.midright[0] >= 400):
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
    pygame.key.set_repeat(1, 1)
    keystates={'jump': False, 'left':False, 'right':False}


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
            if event.type == KEYDOWN:

                if event.key == K_RIGHT:
                    keystates['right'] = True
                    
                if event.key == K_LEFT:
                    keystates['left'] = True
                
                if event.key == K_SPACE:
                    keystates['jump'] = True
            if event.type == KEYUP:
                if event.key == K_RIGHT:
                    keystates['right'] = False
                    
                if event.key == K_LEFT:
                    keystates['left'] = False
                
                if event.key == K_SPACE:
                    keystates['jump'] = False

        if keystates['right']:
            goomba.move("R")
            shift_game_objects(goomba, floor.floor_boards, background, clean_background)
        if keystates['left']:
            goomba.move("L")
        if keystates['jump']:
            goomba.jump()
                                
        goomba.update()

        screen.blit(background, (0, 0))
        allsprites.draw(screen)
        pygame.display.flip()

                

                
        
    


    

main();
