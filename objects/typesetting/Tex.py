import copy
import lxml.etree as ET
import os
import subprocess as sp
from hashlib import sha256

from animation.Frameable import Frameable
from .constants import DEFAULT_FILL
from .constants import TEMPLATE_FILE
from .constants import TEX_AUXILIARY
from .constants import STD_TEX_NS
from .constants import TEX_OUTPUT
from .constants import TEX_SVG_OUTPUT
from .styles import DEFAULT_TEX_STYLE
from .TexWriter import TexWriter

OPACITY = 'opacity'
FILL = 'fill'
TRANSFORM = 'transform'

class Tex(Frameable):
    """
    parent class for handling all objects that need to be typeset in TeX
    """

    def __init__(self, content, style=None, position=None, cache=True):
        """
        str, [dict], [bool] -> None

        :param content: a string that represents a the content you want to
        typeset, 'content' must be a valid string in the document environment
        of a TeX document
        :param [style]: a dictionary of modifications you want to make to the
        style of the content you want to typeset, see the default style for
        hints on how to use this
        :param [cache]: whether you want to use the cached svg file for this
        object if one is available, if you choose not to use the cached one it
        will be overwritten during the creation of this object anyways
        """
        self.content = Tex.makeContent(content)
        self.name = Tex.makeName(self.content)
        self.path = Tex.makePath(self.name)

        self.style = Tex.makeStyle(style)
        self.position = position
        self.node = Tex.makeNode(self.content, self.name, self.path,
                                 self.style, self.position, cache)

        Frameable.__init__(self, self.node)

    @staticmethod
    def getGroups(node):
        return node.findall('./svg:g', namespaces=STD_TEX_NS)

    @staticmethod
    def getUses(node):
        return node.findall('./svg:g/svg:use', namespaces=STD_TEX_NS)

    @staticmethod
    def applyPosition(node, position):
        uses = Tex.getUses(node)

        for use in uses:
            new_x = float(use.get('x')) + position[0]
            new_y = float(use.get('y')) + position[1]
            use.set('x', str(new_x))
            use.set('y', str(new_y))

        viewbox = node.get('viewBox').split(' ')
        viewbox[0] = float(viewbox[0]) + position[0]
        viewbox[1] = float(viewbox[1]) + position[1]
        viewbox = [str(x) for x in viewbox]
        viewbox = ' '.join(viewbox)
        node.set('viewBox', viewbox)

    @staticmethod
    def applyStyle(node, style):
        for group in Tex.getGroups(node):
            for key in style:
                group.set(key, str(style[key]))

    @staticmethod
    def makeStyle(s):
        return s and {**DEFAULT_TEX_STYLE, **s}

    @staticmethod
    def makeNode(content, name, path, style, position, cache):
        """
        None -> ET.Element
        this only works if you wrote the file already
        """
        if not os.path.isfile(path) or not cache:
            writer = TexWriter(content)
            writer.write(clean=True)
        res = ET.parse(path).getroot()

        if style:
            Tex.applyStyle(res, style)

        if position:
            Tex.applyPosition(res, position)

        return res

    @staticmethod
    def makePath(name):
        return f'{TEX_SVG_OUTPUT}/{name}.svg'

    @staticmethod
    def makeContent(content):
        return '\\pagenumbering{gobble}\n' + content

    @staticmethod
    def makeName(content):
        hashObj = sha256()
        hashObj.update(content.encode('utf-8'))
        res = hashObj.hexdigest()
        return res


    def __copy__(self):
        """
        this is pretty much a deep copy

        None -> Tex
        :returns: copied Tex object
        """
        style_copy = copy.deepcopy(self.style)
        return Tex(self.content, style=style_copy, position=self.position)

    def partialCopy(self, content=None, position=None, style={}):
        """
        allows you to copy the current tex object while making some
        modifications

        [str], [dict], [bool] -> Tex
        """
        content = content or self.content
        position= position or self.position
        new_style = {**self.style, **style}
        return Tex(content, style=new_style, position=position)
