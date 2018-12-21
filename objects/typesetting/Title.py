from .Tex import Tex
from .constants import DEFAULT_FILL, SUBHEADING_FONT_SIZE
from .constants import HEADING_FONT_SIZE, SPACING_SIZE

class Title(Tex):
    def __init__(self, heading, subheading='', fill=DEFAULT_FILL, opacity=1, transform=''):
        self.heading = heading
        self.subheading = subheading
        self.format = self._format()
        Tex.__init__(self, self.format, fill=fill, opacity=opacity,
                     transform=transform)

    def _format(self):
        h = HEADING_FONT_SIZE
        hs = round(HEADING_FONT_SIZE * SPACING_SIZE)
        s = SUBHEADING_FONT_SIZE
        ss = round(SUBHEADING_FONT_SIZE * SPACING_SIZE)

        res = rf'''
        \noindent\begin{{center}}
            \textbf{{
                \fontsize{{{h}}}{{{hs}}}\selectfont
                {self.heading}
            }}
            \\
            \bigskip
            {{
                \fontsize{{{s}}}{{{ss}}}\selectfont
                {self.subheading}
            }}
        \end{{center}}
        '''
        return res
