import pygame

import structure
import system
import error

pygame.font.init()

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)

__settings__ = structure.Struct({
    "background": BLACK,
    "foreground": WHITE,
    "fontname": None,
    "fontsize": None,
    "fontobj": None,
    "antialias": False,
    "width": 0,
    "height": 0,
    "tint": WHITE,
})

class Image(object):
    def __init__(self, path):
        try:
            self.__surface = pygame.image.load(system.getSystemPath(path))
        except pygame.error:
            raise error.ImageNotFoundError(path)

    def getWidth(self):
        return self.__surface.get_width()

    def getHeight(self):
        return self.__surface.get_height()

    def getSurface(self):
        return self.__surface

    def getImageName(self):
        return None

def newImage(path):
    return Image(path)

class Sprite(object):
    def __init__(self, image):
        self.image = image
        self.x = self.y = 0
        self.w = self.image.getWidth()
        self.h = self.image.getHeight()

    def contains(self, (x, y)):
        return (x >= self.x and x <= self.x + self.w and
                y >= self.y and y <= self.y + self.h)

    def collides(self, other):
        return (self.x < other.x + other.w and
                other.x < self.x + self.w and
                self.y < other.y + other.h and
                other.y < self.y + self.h)

# Settings-related functions
def setFontName(fontname):
    __settings__.fontname = str(fontname)
    __settings__.font = pygame.font.SysFont(
        __settings__.fontname,
        __settings__.fontsize
        )

def getFontName():
    return __settings__.fontname

def setFontSize(fontsize):
    __settings__.fontsize = int(fontsize)
    __settings__.font = pygame.font.SysFont(
        __settings__.fontname,
        __settings__.fontsize
        )

def getFontSize():
    return __settings__.fontsize

def setFont(fontname, fontsize):
    __settings__.fontname = str(fontname)
    __settings__.fontsize = int(fontsize)
    __settings__.font = pygame.font.SysFont(
        __settings__.fontname,
        __settings__.fontsize
        )

def getFont():
    return (getFontName(), getFontSize())

def setBackgroundColor(r, g, b):
    __settings__.background = (r, g, b)

def getBackgroundColor():
    return __settings__.background

def getWidth():
    return __settings__.width

def getHeight():
    return __settings__.height

def setSetting(key, value):
    __settings__[key] = value

# Drawing functions
def draw(image, x, y):
    pygame.display.get_surface().blit(image.getSurface(), (x, y))

def drawSprite(sprite):
    draw(sprite.image, sprite.x, sprite.y)

def write(text, x, y):
    surf = __settings__.font.render(
        text,
        __settings__.antialias,
        __settings__.tint,
    )

    pygame.display.get_surface().blit(surf, (x, y))

setFont("Arial", 16)
