import subprocess as sp
import os
from hashlib import sha256
import lxml.etree as ET
from .constants import TEMPLATE_FILE, TEX_OUTPUT, TEX_AUXILIARY, TEX_SVG_OUTPUT, DEFAULT_FILL
from .TexWriter import TexWriter

OPACITY = 'opacity'
FILL = 'fill'
TRANSFORM = 'transform'

class Tex:
    """
    class for handling objects that need to be typeset in tex
    """

    def __init__(self, content, opacity=1, fill=DEFAULT_FILL, transform='',
                 cache=True):

        self.content = content
        hashObj = sha256()
        hashObj.update(content.encode('utf-8'))
        self.name = hashObj.hexdigest()
        self.path_to_svg = f'{TEX_SVG_OUTPUT}/{self.name}.svg'
        self.writer = TexWriter(content)

        self.node = self._getNode(cache)
        self.opacity = opacity
        self.fill = fill
        self.transform = transform
        self.cache = cache
        self._setOpacity(opacity)
        self._setFill(fill)
        self._setTransform(transform)

    def __copy__(self):
        return Tex(self.content, self.opacity, self.fill, self.transform,
                   self.cache)

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
