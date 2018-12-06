from .Tex import Tex
from .constants import QUOTE_FONT_SIZE

class Quote(Tex):
    """
    class that represents a quote
    """
    def __init__(self, quote, author='', font_size=QUOTE_FONT_SIZE):
        self.quote = quote
        self.author = author
        self.format = self._format()
        super().__init__(self.format)

    def _format(self):
        quote_size = QUOTE_FONT_SIZE
        quote_spacing = QUOTE_FONT_SIZE * 1.2

        res = ''
        res += r'\noindent\fontsize'
        res += f'{{{quote_size}}}{{{round(quote_spacing)}}}'
        res += rf'\selectfont "{self.quote}"\\'
        res += rf'\rightline{{-{self.author}}}'
        return res
