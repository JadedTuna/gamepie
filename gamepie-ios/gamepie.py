import importlib
import time

import scene

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

class PieScene(scene.Scene):
    def __init__(self, game):
        super(PieScene, self).__init__()
        self.game = game
    
    def setup(self):
        self.game.size = self.size
        gamepie.graphics.setSetting("width", self.size[0])
        gamepie.graphics.setSetting("height", self.size[1])
        self.game.load()
    
    def draw(self):
        self.game.update(self.dt)
        scene.background(*gamepie.graphics.getBackgroundColor())
        self.game.draw(self.dt)
    
    def touch_began(self, touch):
        x, y = touch.location
        self.game.mousepressed(x, gamepie.graphics.getHeight() - y, -1)
    
    def touch_moved(self, touch):
        x, y = touch.location
        px, py = touch.prev_location
        self.game.mousemoved(x, gamepie.graphics.getHeight() - y,
                             x - px,
                             -(y - py))
    
    def touch_ended(self, touch):
        x, y = touch.location
        self.game.mousereleased(x, y, -1)

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

    if "graphics" in __required__:
        gamepie.graphics.setSetting("width", game.size[0])
        gamepie.graphics.setSetting("height", game.size[1])

    scene.run(PieScene(game), frame_interval=frame_delay)
