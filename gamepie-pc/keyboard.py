import pygame
import string

import error

__special__ = {
    "escape": pygame.K_ESCAPE,
    "up":     pygame.K_UP,
    "right":  pygame.K_RIGHT,
    "down":   pygame.K_DOWN,
    "left":   pygame.K_LEFT,
    "space":  pygame.K_SPACE,
}

pygame.init()
# Create an empty key list
__keys__ = [False] * len(pygame.key.get_pressed())

def isKeyPressed(*keys):
    for key in keys:
        if __keys__[convertKey(key)]:
            return True

    return False

def setKey(key, value):
    __keys__[key] = value

def convertKey(key):
    if key in __special__.keys():
        return __special__[key]
    elif key.lower() in string.digits + string.lowercase:
        return getattr(pygame, "K_" + key)
    else:
        raise error.UnknownKeyError(key)