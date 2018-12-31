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
        heading, subheading = config['heading'], config['subheading']
        content = Title.makeContent(heading, subheading)
        config['content'] = content
        Tex.__init__(self, config)

    @staticmethod
    def makeContent(heading, subheading):
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
