import sound

import system
import error


class Source(object):
    def __init__(self, path):
        self.__path = system.getSystemPath(path)
        try:
            open(self.__path).close()
            sound.load_effect(self.__path)
        except IOError:
            raise error.SourceNotFoundError(path)
    
    def play(self):
        sound.play_effect(self.__path)

def newSource(path):
    return Source(path)

