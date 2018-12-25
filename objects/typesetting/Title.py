from .constants import DEFAULT_FILL
from .constants import HEADING_FONT_SIZE
from .constants import SPACING_SIZE
from .constants import SUBHEADING_FONT_SIZE
from .styles import DEFAULT_TEX_STYLE
from .Tex import Tex

class Title(Tex):
    def __init__(self, heading, subheading='', style=DEFAULT_TEX_STYLE):
        self.heading = heading
        self.subheading = subheading
        self.format = self._format()
        Tex.__init__(self, self.format, style=style)

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
