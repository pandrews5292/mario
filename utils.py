import os
import sys
import pygame
import random
from pygame.locals import *


def load_image(filename, color_key=None):
    full_path = os.path.join('images', filename)
    image = pygame.image.load(full_path)
    image = image.convert()
    if color_key is not None:
        if color_key is -1:
            color_key = image.get_at((0,0))
        image.set_colorkey(color_key, RLEACCEL)

    return image, image.get_rect()
