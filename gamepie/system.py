import os

def getOS():
    if os.name == "nt":
        return "Windows"
    elif os.name == "posix":
        return "Linux"

def getSystemPath(path):
    return os.path.join(*path.split("/"))
