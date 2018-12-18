import subprocess as sp
import os
from hashlib import sha256
import lxml.etree as ET
from .constants import TEMPLATE_FILE, TEX_OUTPUT, TEX_AUXILIARY, TEX_SVG_OUTPUT, DEFAULT_FILL
from .TexWriter import TexWriter

OPACITY = 'opacity'

class Tex:
    """
    class for handling objects that need to be typeset in tex
    """

    def __init__(self, content, opacity=1, fill=DEFAULT_FILL):
        self.content = content
        hashObj = sha256()
        hashObj.update(content.encode('utf-8'))
        self.name = hashObj.hexdigest()
        self.path_to_svg = f'{TEX_SVG_OUTPUT}/{self.name}.svg'
        self.writer = TexWriter(content)
        self.node = self._getNode()
        self._setOpaticy(opacity)
        self._setFill(fill)

    def _setOpaticy(self, opacity):
        self.node.set(OPACITY, str(opacity))

    def _setFill(self, fill):
        self.node.set('fill', fill)

    def _getNode(self):
        """
        None -> ET.Element
        this only works if you wrote the file already
        """
        if not os.path.isfile(self.path_to_svg):
            self.writer.write()
        res = ET.parse(self.path_to_svg).getroot()
        return res
