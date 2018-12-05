from .Tex import Tex
from .constants import QUOTE_FONT_SIZE

class Quote(Tex):
    """
    class that represents a quote
    """
    def __init__(self, quote, font_size=QUOTE_FONT_SIZE):
        self.quote = quote
        self.format = self._format()
        super().__init__(self.format)

    def _format(self):
        res = ''
        res += r'\noindent'
        res += r'\fontsize'
        res += f'{{{QUOTE_FONT_SIZE}}}'
        res += f'{{{round(QUOTE_FONT_SIZE * 1.2)}}}'
        res += r'\selectfont '
        res += '"'
        res += self.quote
        res += '"'
        return res
