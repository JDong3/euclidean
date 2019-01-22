import copy
import geometry.Line as Line
import geometry.Point as Point
import compound.LabeledLine as LabeledLine

from animation.constants import STD_HEIGHT
from animation.constants import STD_WIDTH



class NumberLine():
    """
    number line is drawn full screen
    """
    def __init__(self, config):
        """
        :param config:

        :config [arrow]:
        :config [dot]:
        :config [height]: height of entire image
        :config [label height]: height of entire image
        :config [value]:
        :config [width]: width of entire image
        :config [xmin]:
        :config [xmax]:
        :config [sparseness]:
        """
        return None

    @staticmethod
    def makeConfig(config):
        """
        dot takes precedent over arrow, if none are provided dot is the default
        display
        """
        res = copy.deepcopy(config)

        DEF_ARROW = False
        DEF_DOT = True
        DEF_HEIGHT = STD_HEIGHT * 0.2
        DEF_LABEL_HEIGHT = STD_HEIGHT * 0.08
        DEF_SPARSENESS = 1
        DEF_VALUE = 666
        DEF_WIDTH = STD_WIDTH
        DEF_XMAX = DEF_VALUE + 5
        DEF_XMIN = DEF_VALUE - 5

        if not nlatr.arrow in res and not nlatr.dot in res:
            res[nlatr.dot] = DEF_DOT
        if not nlatr.height in res:
            res[nlatr.height] = DEF_HEIGHT
        if not nlatr.label_height in res:
            res[nlatr.label_height] = DEF_LABEL_DEIGHT
        if not nlatr.spareseness in res:
            res[nlatr.sparseness] = DEF_SPARSENESS
        if not nlatr.value in res:
            res[nlatr.value] = DEF_value
        if not nlatr.width in res:
            res[nlatr.width] = DEF_WIDTH
        if not nlatr.xmin in res:
            res[nlatr.xmin] = DEF_XMIN
        if not nlatr.xmax in res:
            res[nlatr.xmax] = DEF_xMAX

        return res

    @staticmethod
    def makeXline(config):
        width = config[nlatr.width]
        height = config[nlatr.height] - config[nlatr.label_height]
        
        return None

    @staticmethod
    def makeNode(config):
        return None
