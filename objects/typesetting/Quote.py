import copy

from . import tatr
from .constants import DEFAULT_FILL
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
        :config [font_size]:
        """
        config = Quote.makeConfig(config)
        Tex.__init__(self, config)

    @staticmethod
    def makeConfig(config):
        DEF_QUOTE = 'no quote'
        DEF_AUTHOR = 'no author'
        res = copy.deepcopy(config)

        if not tatr.quote in res:
            res[tatr.quote] = DEF_QUOTE

        if not tatr.author in config:
            res[tatr.author] = DEF_AUTHOR

        res[tatr.content] = Quote.makeContent(res)
        return res

    @staticmethod
    def makeContent(config):
        quote = config[tatr.quote]
        author = config[tatr.author]
        quote_size = QUOTE_FONT_SIZE
        quote_spacing = QUOTE_FONT_SIZE * SPACING_SIZE
        res = rf'''
            \noindent\fontsize
            {{{quote_size}}}{{{round(quote_spacing)}}}
            \selectfont "{quote}"\\
            \rightline{{-{author}}}
        '''
        return res
