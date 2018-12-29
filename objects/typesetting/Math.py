from .constants import DISPLAY
from .Tex import Tex

class Math(Tex):
    def __init__(self, math, display=DISPLAY):
        self.display = display
        self.math = math
        self.content = Math.makeContent()
        Tex.__init__(self, self.content)

    @staticmethod
    def makeContent(self):
        return rf'$\{self.display} {self.content}$'
