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

    def __init__(self, config):
        """
        dict -> None

        :param config: dictionary that represents the configuration of the
        object

        :config content: a string that represents a the content you want to
        typeset, 'content' must be a valid string in the document environment
        of a TeX document
        :config [style]: a dictionary of modifications you want to make to the
        style of the content you want to typeset, see the default style for
        hints on how to use this
        :config [size]: the size in px of the svg in form '(width, height)'
        :config [cache]: whether you want to use the cached svg file for this
        object if one is available, if you choose not to use the cached one it
        will be overwritten during the creation of this object anyways
        """
        self.config = config
        self.content = Tex.makeContent(config['content'])
        self.name = Tex.makeName(self.content)
        self.path = Tex.makePath(self.name)

        self.style = Tex.makeStyle(config['style'])
        self.size = config['size']
        self.node = Tex.makeNode(self.content, self.style, self.size)

        Frameable.__init__(self, self.node)

    @staticmethod
    def applyPosition(node, position):
        '''
        :deprecated:
        '''
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
    def applySize(node, size):
        aspect_ratio = size[0] / size[1]
        old_size = [node.get('width'), node.get('height')]

        for i, dim in enumerate(old_size):
            res = dim[:-2]
            res = float(res)
            old_size[i] = res
        old_aspect_ratio = old_size[0] / old_size[1]

        # if new ratio is larger than older ratio then our desired picture is wider than the available screen
        if aspect_ratio > old_aspect_ratio:
            scale = size[1]/old_size[1]
        else:
            scale = size[0]/old_size[0]

        new_size = [str(x * scale) for x in old_size]
        node.set('width', new_size[0])
        node.set('height', new_size[1])

    @staticmethod
    def applyStyle(node, style):
        for group in Tex.getGroups(node):
            for key in style:
                group.set(key, str(style[key]))

    @staticmethod
    def getGroups(node):
        return node.findall('./svg:g', namespaces=STD_TEX_NS)

    @staticmethod
    def getUses(node):
        return node.findall('./svg:g/svg:use', namespaces=STD_TEX_NS)

    @staticmethod
    def makeStyle(s):
        return s and {**DEFAULT_TEX_STYLE, **s}

    @staticmethod
    def makeNode(content, style, size, cache=True):
        """
        None -> ET.Element
        this only works if you wrote the file already
        """
        name = Tex.makeName(content)
        path = Tex.makePath(name)

        if not os.path.isfile(path) or not cache:
            writer = TexWriter(content)
            writer.write(clean=True)
        res = ET.parse(path).getroot()

        if style:
            Tex.applyStyle(res, style)

        if size:
            Tex.applySize(res, size)

        # deprecated, use translate
        # if position:
        #     Tex.applyPosition(res, position)

        return res

    @staticmethod
    def makeContent(content):
        return '\\pagenumbering{gobble}\n' + content

    @staticmethod
    def makeName(content):
        hashObj = sha256()
        hashObj.update(content.encode('utf-8'))
        res = hashObj.hexdigest()
        return res

    @staticmethod
    def makePath(name):
        return f'{TEX_SVG_OUTPUT}/{name}.svg'

    def __copy__(self):
        """
        this is pretty much a deep copy

        None -> Tex
        :returns: copied Tex object
        """
        config_copy = copy.deepcopy(self.config)
        return Tex(config_copy)

    def partialCopy(self, config):
        """
        allows you to copy the current tex object while making some
        modifications

        [str], [dict], [list] -> Tex
        """
        if config:
            config = {**self.config, **config}
        else:
            config = self.config
        return Tex(config)
