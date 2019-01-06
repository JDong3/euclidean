import copy
from . import tatr
from .constants import DEFAULT_FILL
from .constants import HEADING_FONT_SIZE
from .constants import SPACING_SIZE
from .constants import SUBHEADING_FONT_SIZE
from .styles import DEFAULT_TEX_STYLE
from .Tex import Tex

class Title(Tex):
    def __init__(self, config):
        """
        :param config:

        :config heading:
        :config subheading:
        """
        config = Title.makeConfig(config)
        Tex.__init__(self, config)

    @staticmethod
    def makeConfig(config):
        DEF_HEADING = 'no heading'
        DEF_SUBHEADING = 'no subheading'

        config = copy.deepcopy(config)
        if not tatr.heading in config:
            config[tatr.heading] = DEF_HEADING

        if not tatr.subheading in config:
            config[tatr.subheading] = DEF_SUBHEADING

        content = Title.makeContent(config)
        config[tatr.content] = content

        return config

    @staticmethod
    def makeContent(config):
        heading = config[tatr.heading]
        subheading = config[tatr.subheading]
        h = HEADING_FONT_SIZE
        hs = round(HEADING_FONT_SIZE * SPACING_SIZE)
        s = SUBHEADING_FONT_SIZE
        ss = round(SUBHEADING_FONT_SIZE * SPACING_SIZE)

        res = rf'''
        \noindent\begin{{center}}
            \textbf{{
            \fontsize{{{h}}}{{{hs}}}\selectfont
                {heading}
            }}
            \\
            \bigskip
            {{
                \fontsize{{{s}}}{{{ss}}}\selectfont
                {subheading}
            }}
        \end{{center}}
        '''
        return res
