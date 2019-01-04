from .constants import DISPLAY
from .Tex import Tex
from . import tatr

class Math(Tex):
    def __init__(self, config):

        math = config[tatr.math]
        config[tatr.content] = Math.makeContent(math)
        Tex.__init__(config)

    @staticmethod
    def makeContent(math):
        return rf'$\displaystyle {math}$'
