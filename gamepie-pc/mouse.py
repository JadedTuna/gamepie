import pygame

BUTTON_1 = 0
BUTTON_2 = 1
BUTTON_3 = 2

def getPosition():
    return pygame.mouse.get_pos()

def setPosition(x, y):
    pygame.mouse.set_pos(x, y)
