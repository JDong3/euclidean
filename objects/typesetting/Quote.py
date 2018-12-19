from .Tex import Tex
from .constants import QUOTE_FONT_SIZE, DEFAULT_FILL

class Quote(Tex):
    """
    class that represents a quote
    """
    def __init__(self, quote, author='', font_size=QUOTE_FONT_SIZE,
                 fill=DEFAULT_FILL, transform='', cache=True):
        self.quote = quote
        self.author = author
        self.format = self._format()
        Tex.__init__(self, self.format, fill=fill, transform=transform)


    def _format(self):
        quote_size = QUOTE_FONT_SIZE
        quote_spacing = QUOTE_FONT_SIZE * 1.2

        res = ''
        res += r'\noindent\fontsize'
        res += f'{{{quote_size}}}{{{round(quote_spacing)}}}'
        res += rf'\selectfont "{self.quote}"\\'
        res += rf'\rightline{{-{self.author}}}'
        return res
