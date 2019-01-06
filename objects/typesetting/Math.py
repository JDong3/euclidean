from .constants import DISPLAY
from .Tex import Tex
from . import tatr

class Math(Tex):
    def __init__(self, config):

        math = config[tatr.math]
        config[tatr.content] = Math.makeContent(math)
        Tex.__init__(config)

    @staticmethod
    def makeConfig(config):
        DEF_MATH = r'no \. math'
        config = copy.deepcopy(config)

        if not tatr.math in config:
            config[tatr.math] = DEF_MATH
        config[tatr.math] = Math.makeContent(config)

    @staticmethod
    def makeContent(config):
        math = config[tatr.math]
        return rf'$\displaystyle {math}$'
