import pygame

import system
import error

pygame.mixer.init()


class Source(object):
    def __init__(self, path):
        try:
            fileobj = open(system.getSystemPath(path))
            self.__sound = pygame.mixer.Sound(fileobj)
        except IOError:
            raise error.SourceNotFoundError(path)

    def play(self):
        self.__sound.play()

def newSource(path):
    return Source(path)
