import importlib
import time

import pygame

import gamepie

__all__ = ["Game", "getVersion", "isPieSupported", "require", "run"]
__required__ = []
__supported__ = [
    # A list of supported GamePie versions
    "0.1",
]
__version__ = "0.1"


class Game(object):
    def __init__(self):
        self.__running = True
        self.title = "GamePie"
        self.gamepie = gamepie.getVersion
        self.size = (640, 480)

    def conf(self):
        pass

    def load(self):
        pass

    def mousepressed(self, x, y, button):
        pass

    def mousereleased(self, x, y, button):
        pass

    def mousemoved(self, x, y, dx, dy):
        pass

    def update(self):
        pass

    def draw(self):
        pass

    def exit(self):
        self.__running = False

    def isRunning(self):
        return self.__running

class ErrorPie(Game):
    def __init__(self, text):
        super(ErrorPie, self).__init__()
        self.title = "Error"
        self.text = text

    def load(self):
        gamepie.graphics.setBackgroundColor(80, 80, 255)

    def draw(self):
        gamepie.graphics.write(self.text, 0, 0)

def getVersion():
    return __version__

def isPieSupported(pie):
    return pie in __supported__

def require(*args):
    global __required__
    __required__ = args[:]

def run(game, frame_delay=1):
    game.conf()
    if not gamepie.isPieSupported(game.gamepie):
        game = gamepie.ErrorPie(
            "Target GamePie version is not supported: %s" % game.gamepie)

    for module in __required__:
        setattr(gamepie, module,
            importlib.import_module("gamepie." + module))

    pygame.init()
    window = pygame.display.set_mode(game.size)
    pygame.display.set_caption(game.title)

    if "graphics" in __required__:
        gamepie.graphics.setSetting("width", game.size[0])
        gamepie.graphics.setSetting("height", game.size[1])
    game.load()

    delay = 60/frame_delay
    clock = pygame.time.Clock()
    last = time.time()
    new = last
    while game.isRunning():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.exit()

            elif event.type == pygame.KEYUP:
                keyboard.setKey(event.key, False)
            elif event.type == pygame.KEYDOWN:
                keyboard.setKey(event.key, True)

            elif event.type == pygame.MOUSEBUTTONUP:
                game.mousereleased(event.pos[0],
                                    event.pos[1],
                                    event.button)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                game.mousepressed(event.pos[0],
                                    event.pos[1],
                                    event.button)
            elif event.type == pygame.MOUSEMOTION:
                game.mousemoved(event.pos[0], event.pos[1],
                                event.rel[0], event.rel[1])

        new = time.time()
        game.update(new - last)
        window.fill(gamepie.graphics.getBackgroundColor())
        game.draw(new - last)
        last = new
        pygame.display.update()
        clock.tick(delay)

    pygame.quit()
