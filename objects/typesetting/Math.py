from .constants import DISPLAY
from .Tex import Tex

class Math(Tex):
    def __init__(self, math, display=DISPLAY):
        self.display = display
        self.math = math
        self.format = self._format()
        Tex.__init__(self, self.format)

    def _format(self):
        return rf'$\{self.display} {self.content}$'
