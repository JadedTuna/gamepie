import os

def getOS():
    return "iOS"

def getSystemPath(path):
    return os.path.join(*path.split("/"))
