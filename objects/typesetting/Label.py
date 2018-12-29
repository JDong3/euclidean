from .Tex import Tex
from .styles import DEFAULT_TEX_STYLE
from .constants import STD_TEX_NS

# TODO: new api, label(degree(radians), distance), position moved to tex

class Label(Tex):
    def __init__(self, label, position, style={}):
        self.label = label
        self.position = position
        self._format = label
        self._style = {**DEFAULT_TEX_STYLE, **style}
        Tex.__init__(self, self.label, self._style)
        # Label.setPositions(self.node, self.x, self.y)
