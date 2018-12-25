import copy
import lxml.etree as ET
import os
import subprocess as sp
from hashlib import sha256

from .constants import DEFAULT_FILL
from .constants import TEMPLATE_FILE
from .constants import TEX_AUXILIARY
from .constants import TEX_OUTPUT
from .constants import TEX_SVG_OUTPUT
from .styles import DEFAULT_TEX_STYLE
from .TexWriter import TexWriter

OPACITY = 'opacity'
FILL = 'fill'
TRANSFORM = 'transform'

class Tex:
    """
    class for handling objects that need to be typeset in TeX
    """

    def __init__(self, content, style=DEFAULT_TEX_STYLE, cache=True):
        self.content = content
        hashObj = sha256()
        hashObj.update(content.encode('utf-8'))
        self.name = hashObj.hexdigest()
        self.path_to_svg = f'{TEX_SVG_OUTPUT}/{self.name}.svg'
        self.writer = TexWriter(content)

        self.node = self._getNode(cache)
        self._style = {**DEFAULT_TEX_STYLE, **style}
        self.cache = cache
        self._setOpacity(self._style['opacity'])
        self._setFill(self._style['fill'])
        self._setTransform(self._style['transform'])

    def __copy__(self):
        style_copy = copy.deepcopy(self._style)
        return Tex(self.content, style_copy, self.cache)

    def partialCopy(self, content=None, style={}):
        content = content or self.content
        new_style = {**self._style, **style}
        return Tex(content, new_style)

    def _getGroups(self):
        ns = {
            'svg': 'http://www.w3.org/2000/svg'
        }
        return self.node.findall('svg:g', namespaces=ns)

    def _setOpacity(self, opacity):
        for group in self._getGroups():
            group.set(OPACITY, str(opacity))

    def _setFill(self, fill):
        for group in self._getGroups():
            group.set(FILL, fill)

    def _setTransform(self, transform):
        for group in self._getGroups():
            group.set(TRANSFORM, transform)

    def _getNode(self, cache):
        """
        None -> ET.Element
        this only works if you wrote the file already
        """
        if not os.path.isfile(self.path_to_svg) or not cache:
            self.writer.write(clean=True)
        res = ET.parse(self.path_to_svg).getroot()
        return res
