class GamePieError(Exception): pass

# graphics.py
class ImageNotFoundError(GamePieError): pass

# audio.py
class SourceNotFoundError(GamePieError): pass

# keyboard.py
class UnknownKeyError(GamePieError): pass

# anywhere
