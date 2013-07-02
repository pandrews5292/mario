import os
import sys
import pygame
import random
import time
from pygame.locals import *


BACKGROUND_COLOR = (135, 206, 250)
SCREEN_SIZE = (800, 500)

def load_image(filename, color_key=None):
    full_path = os.path.join('images', filename)
    image = pygame.image.load(full_path)
    image = image.convert()
    if color_key is not None:
        if color_key is -1:
            color_key = image.get_at((0,0))
        image.set_colorkey(color_key, RLEACCEL)

    return image, image.get_rect()

class HUD():
    def __init__(self):
        self.start_time = time.time()
        self.time_over = False
        self.time_text_pos = (710, 50) 
        self.time_pos = (701, 30)
        self.world_num = 1
        self.level_num = 1
        self.world_level_num_pos = (550, 50)
        self.world_text_pos = (530, 30)
        self.num_lives = 05
        self.num_lives_pos = (322, 50)
        self.mario_text_pos = (300, 30)
        self.score_pos = (100, 30)
        self.score = 0000000
        self.coins_pos = (103, 50)
        self.coins = 0000000
     
    def get_start_time(self):
        return self.start_time

    def get_world_and_level(self):
        return (self.world_num, self.level_num)

    def set_level(self, level):
        self.level_num = level

    def set_world(self, world):
        self.world_num = level
        
    def get_time_over(self):
        return self.time_over

    def get_num_lives(self):
        return self.num_lives

    def set_num_lives(self, num):
        self.num_lives = num

    def get_score(self):
        return self.score

    def set_score(self, score):
        self.score = score

    def get_coins(self):
        return self.coins

    def set_coins(self, coins):
        self.coins = coins
        
    def get_time(self):
        if self.time_over:
            self.cur_time = 0
        else:
            self.cur_time = int(1000 - (time.time() - self.start_time))
            if (self.cur_time <= 0):
                self.time_over = True


    def print_hud(self, background):
        font = pygame.font.Font(None, 36)

        time_text = font.render("TIME", 1, (0, 0, 0))
        counting_time_text = font.render(str(self.cur_time), 1, (0, 0, 0))

        time_pos = time_text.get_rect(center=self.time_pos)
        counting_time_pos = counting_time_text.get_rect(center=self.time_text_pos)

        world_num_text = font.render(str(self.world_num) + " - " + str(self.level_num), 1, (0, 0, 0))
        world_num_pos = world_num_text.get_rect(center=self.world_level_num_pos)

        world_text = font.render("WORLD", 1, (0, 0, 0))
        world_text_pos = world_text.get_rect(center=self.world_text_pos)

        mario_lives = font.render("x " + str(self.num_lives), 1, (0, 0, 0))
        mario_name = font.render("MARIO", 1, (0, 0, 0))

        mario_lives_pos = mario_lives.get_rect(center=self.num_lives_pos)
        mario_name_pos = mario_name.get_rect(center=self.mario_text_pos)

        score_text = font.render("SCORE: " + str(self.score), 1, (0, 0, 0))
        score_pos = score_text.get_rect(center=self.score_pos)

        coins_text = font.render("COINS: " + str(self.coins), 1, (0, 0, 0))
        coins_pos = coins_text.get_rect(center=self.coins_pos)

                                  
        background.fill(BACKGROUND_COLOR)
        background.blit(time_text, time_pos)
        background.blit(counting_time_text, counting_time_pos)
        background.blit(world_num_text, world_num_pos)
        background.blit(world_text, world_text_pos)
        background.blit(mario_lives, mario_lives_pos)
        background.blit(mario_name, mario_name_pos)
        background.blit(score_text, score_pos)
        background.blit(coins_text, coins_pos)
                                             
                                             
        



        

        
