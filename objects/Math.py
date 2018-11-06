from constants import DISPLAY
from styles import STD_COLOR

class Math:
    def __init__(self, content, display=DISPLAY, color=STD_COLOR):
        self.display = display
        self.b_color = color
        self.content = content
        self.out = self._format()

    def _format(self):
        return rf'$\{self.display} {self.content}$'

