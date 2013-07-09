import os
import sys
import random
import time
import pygame
from pygame.locals import * 
import utils
import sprites

BACKGROUND_COLOR = (135, 206, 250)
SCREEN_SIZE = (800, 500)
FLOOR_Y = 440
FLOOR_LENGTH = 145


def shift_game_objects(mario, floor_boards):
    if (mario.right_key_pressed == True and mario.rect.midright[0] >= 400):
        for floor in floor_boards:
            floor.x -= 6
    floor_boards.update()


def draw_floor(num_floor_boards):
    floor_boards = pygame.sprite.RenderPlain()
    offset = 0
    
    for i in range(num_floor_boards):
        floor = sprites.Floor()
        floor.x += offset
        offset += FLOOR_LENGTH
        floor_boards.add(floor)
    floor_boards.update()

    return floor_boards

def generate_platform(floor_boards, x_pos, y_pos):
    floor = sprites.Floor()
    floor.x = x_pos
    floor.y = y_pos
    floor_boards.add(floor)
    floor_boards.update()
    
    
def main():
    #sky blue background color

    pygame.init()

    screen = pygame.display.set_mode((800, 500))
    pygame.display.set_caption('MARIO')
    background = pygame.Surface(screen.get_size())
    

    background.fill(BACKGROUND_COLOR)
    background = background.convert()
    clean_background = pygame.Surface.copy(background)

    mario = sprites.Mario()
    floor_boards = draw_floor(10)
    floor_boards.draw(screen)
    
    generate_platform(floor_boards, 300, 400)

        
    mario_group = pygame.sprite.RenderPlain((mario))   

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
            mario.move("R")
            shift_game_objects(mario, floor_boards)
        if keystates['left']:
            mario.move("L")
        if keystates['jump']:
            mario.jump()
                                
        mario.update(floor_boards)

        screen.blit(background, (0, 0))
        mario_group.draw(screen)
        floor_boards.draw(screen)
        pygame.display.flip()

                

                
        
    


    

main();
