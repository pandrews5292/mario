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

class Mario(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.image_a, self.rect = utils.load_image('mario_a.png', -1)
        self.image_b = utils.load_image('mario_b.png', -1)[0]
        self.image_c = utils.load_image('mario_c.png', -1)[0]
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
        self.image = self.image_a
        self.cur_image = 1
        self.frame = 0
        self.facing_left = False
        self.facing_right = True

    def move(self, direction):
        self.frame += 1

        if direction == "R":
            self.facing_right = True
            self.facing_left = False
            if (self.frame % 4 == 0 and not self.jumping):
                if (self.cur_image == 1):
                    self.image = self.image_b
                    self.cur_image = 2
                elif (self.cur_image == 2):
                    self.image = self.image_c
                    self.cur_image = 3
                else:
                    self.image = self.image_a
                    self.cur_image = 1
            self.right_key_pressed = True
        elif direction == "L":
            self.facing_right = False
            self.facing_left = True
            if (self.frame % 4 == 0 and not self.jumping):
                if (self.cur_image == 1):
                    self.image = pygame.transform.flip(self.image_b, True, False)
                    self.cur_image = 2
                elif (self.cur_image == 2):
                    self.image = pygame.transform.flip(self.image_c, True, False)
                    self.cur_image = 3
                else:
                    self.image = pygame.transform.flip(self.image_a, True, False)
                    self.cur_image = 1
            self.left_key_pressed = True

    def jump(self):
        self.jump_key_pressed = True
        if (self.facing_right):
            self.image = self.image_c
        if (self.facing_left):
            self.image = pygame.transform.flip(self.image_c, True, False)

    def reset(self):
        self.jump_key_pressed = False
        self.right_key_pressed = False
        self.left_key_pressed = False
  
    def update(self, floor):
        floor_collision = pygame.sprite.spritecollide(self, floor, False)
        if (not self.jumping and self.jump_key_pressed):
            self.y_vel = -10
            self.y_pos += self.y_vel
            self.jumping = True
        if self.jumping:

            if len(floor_collision) == 0:
                self.y_pos += self.y_vel
                self.y_vel += self.gravity
            else:
                self.jumping = False

        if self.left_key_pressed and self.rect.midleft[0] > 0:
            self.x_vel = -6
  

        elif self.right_key_pressed and self.rect.midright[0] < 400:
            self.x_vel = 6
          
        else:
            self.x_vel = 0

        self.x_pos += self.x_vel
        if (not self.jumping and len(floor_collision) == 0):
            self.y_pos += 8
        self.rect.center = (self.x_pos, self.y_pos)
        self.reset()   

                                  
class Floor(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.image, self.rect = utils.load_image('bricks.png', -1, 1)
        self.x = -3
        self.y = 505
        self.rect.bottomleft = (self.x, self.y)

    def update(self):
        self.rect.bottomleft = (self.x, self.y)

