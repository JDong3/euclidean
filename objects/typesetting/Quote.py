from . import tatr
from .constatns import DEFAULT_FILL
from .constants import QUOTE_FONT_SIZE
from .constants import SPACING_SIZE
from .styles import DEFAULT_TEX_STYLE
from .Tex import Tex

UNKNOWN_AUTHOR = 'Unknown'

class Quote(Tex):

    def __init__(self, config):
        """
        :param config:

        :config quote:
        :config author:
        :config font_size:
        """
        author = config[tatr.author]
        quote = config[tatr.quote]
        content = Quote.makeContent(quote, author)

        config[tatr.content] = content
        Tex.__init__(self, config)

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
