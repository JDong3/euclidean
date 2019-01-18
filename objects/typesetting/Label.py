import copy
import numpy as np

from . import tatr
from .constants import STD_TEX_NS
from .styles import DEFAULT_TEX_STYLE
from .Tex import Tex

# TODO: new api, label(degree(radians), distance), position moved to tex

class Label(Tex):
    def __init__(self, config):
        """
        :param config:

        :config radian: the angle at which you want to start the label
        :config position: the coordinates of the label
        :config distance: the distance from the position you want to start the
        label
        """
        config = Label.makeConfig(config)
        Tex.__init__(self, config)

    @staticmethod
    def makeConfig(config):
        """
        :pre:
        """
        res = copy.deepcopy(config)
        DEF_CACHE = True
        DEF_RADIAN = 1.5 * np.pi
        DEF_POSITION = (0, 0)
        DEF_DISTANCE = 10

        if not tatr.radian in res:
            res[tatr.radian] = DEF_RADIAN

        if not tatr.distance in res:
            res[tatr.distance] = DEF_DISTANCE

        if not tatr.position in res:
            res[tatr.position] = DEF_POSITION

        res[tatr.position] = Label.makePosition(res)

        return res

    @staticmethod
    def makePosition(config):
        radian = config[tatr.radian]
        position = config[tatr.position]
        distance = config[tatr.distance]
        x = (distance * np.cos(radian)) + position[0]
        y = (-1 * distance * np.sin(radian)) + position[1]

        # offset to center the label
        config = Tex.makeConfig(config)

        node = Tex.makeNodeGet(config)
        width = Tex.applySizeResults(node, config)[0]
        offset = width * 0.5 * -1
        x += offset

        return x, y
