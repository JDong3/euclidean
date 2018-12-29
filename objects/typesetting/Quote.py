from .constants import QUOTE_FONT_SIZE, DEFAULT_FILL, SPACING_SIZE
from .styles import DEFAULT_TEX_STYLE
from .Tex import Tex

UNKNOWN_AUTHOR = 'Unknown'

class Quote(Tex):
    """
    class that represents a quote
    """
    def __init__(self, quote, author=UNKNOWN_AUTHOR, font_size=QUOTE_FONT_SIZE,
                 style=DEFAULT_TEX_STYLE, position=None, cache=True):
        self.quote = quote
        self.author = author
        self.content = Quote.makeContent(self.quote, self.author)
        Tex.__init__(self, self.content, style, position)

    @staticmethod
    def makeContent(quote, author):
        quote_size = QUOTE_FONT_SIZE
        quote_spacing = QUOTE_FONT_SIZE * SPACING_SIZE
        res = rf'''
            \noindent\fontsize
            {{{quote_size}}}{{{round(quote_spacing)}}}
            \selectfont "{quote}"\\
            \rightline{{-{author}}}
        '''
        return res
