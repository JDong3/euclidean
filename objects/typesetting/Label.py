import copy
import numpy as np

from .Tex import Tex
from .styles import DEFAULT_TEX_STYLE
from .constants import STD_TEX_NS


# TODO: new api, label(degree(radians), distance), position moved to tex

class Label(Tex):
    def __init__(self, config):
        """
        :param config:

        :config radian: the angle at which you want to start the label
        :config position: the coordinates of the label
        :config distance: the distance from the position you want to start the
        label

        >>> config = {
                'radian': Pi/2,
                'position': '(100, 150)',
                'distance': 15
            }
        """
        config = copy.deepcopy(config)

        radian = config['radian']
        position = config['position']
        distance = config['distance']
        config['position'] = Label.makePosition(radian, position, distance)
        Tex.__init__(self, config)
        # Label.setPositions(self.node, self.x, self.y)

    @staticmethod
    def makePosition(radian, position, distance):
        x = (distance * np.cos(radian)) + position[0]
        y = (distance * np.sin(radian)) + position[1]
        return x, y
