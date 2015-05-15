import scene
from PIL import Image as PILImage

import structure
import system
import error

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)

__settings__ = structure.Struct({
    "background": BLACK,
    "foreground": WHITE,
    "fontname": None,
    "fontsize": None,
    "antialias": False,
    "width": 0,
    "height": 0,
    "tint": WHITE,
})

class Image(object):
    def __init__(self, path):
        try:
            self.__image = PILImage.open(system.getSystemPath(path))
            self.__image.save(path + ".png")
            self.__surface = scene.load_pil_image(self.__image)
        except IOError:
            raise error.ImageNotFoundError(path)

    def getWidth(self):
        return self.__image.size[0]

    def getHeight(self):
        return self.__image.size[0]

    def getSurface(self):
        return None
    
    def getImageName(self):
        return self.__surface

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

def getFontName():
    return __settings__.fontname

def setFontSize(fontsize):
    __settings__.fontsize = int(fontsize)

def getFontSize():
    return __settings__.fontsize

def setFont(fontname, fontsize):
    __settings__.fontname = str(fontname)
    __settings__.fontsize = int(fontsize)

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
    scene.image(image.getImageName(), x,
                getHeight() - image.getHeight() - y)

def drawSprite(sprite):
    draw(sprite.image, sprite.x, sprite.y)

def write(text, x, y):
    scene.text(
        text,
        __settings__.fontname,
        __settings__.fontsize,
        x,
        getHeight() - y,
        3
    )

setFont("Arial", 16)
