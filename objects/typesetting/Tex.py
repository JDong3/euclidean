import copy
import lxml.etree as ET
import os
import subprocess as sp
import sys
from hashlib import sha256

from . import tatr
from animation.Frameable import Frameable
from .constants import DEFAULT_FILL
from .constants import TEMPLATE_FILE
from .constants import TEX_AUXILIARY
from .constants import STD_TEX_NS
from .constants import TEX_OUTPUT
from .constants import TEX_SVG_OUTPUT
from .styles import DEFAULT_TEX_STYLE
from .TexWriter import TexWriter

class Tex(Frameable):
    """
    parent class for handling all objects that need to be typeset in TeX
    """

    def __init__(self, config):
        """
        does not mutate config

        dict -> None

        :param config: dictionary that represents the configuration of the
        object

        :config [cache]: whether you want to use the cached svg file for this
        object if one is available, if you choose not to use the cached one it
        will be overwritten during the creation of this object anyways
        :config [content]: a string that represents a the content you want to
        typeset, 'content' must be a valid string in the document environment
        of a TeX document
        :config [fill]:
        :config [position]:
        :config [size]: the size in px of the svg in form '(width, height)'
        """
        config = copy.deepcopy(config)

        self.config = Tex.makeConfig(config)
        node = Tex.makeNode(self.config)
        Frameable.__init__(self, self.node)

    @staticmethod
    def applyFill(node, config):
        group = Tex.getGroup(node)
        fill = config[tatr.fill]
        group.set('fill', fill)

    @staticmethod
    def applyPosition(node, config):
        group = Tex.getGroup(node)
        x, y = config[tatr.position]
        transform = group.get('transform')
        transform = f'{transform} translate({x} {y})'
        group.set('transform', tranform)

    @staticmethod
    def applyPosition2(node, position):
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
    def applySize(node, config):
        size = config[tatr.size]
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
    def applyStyle2(node, style):
        """
        :deprecated:
        """
        for group in Tex.getGroups(node):
            for key in style:
                group.set(key, str(style[key]))

    @staticmethod
    def getGroup(node):
        return node.find('./svg:g', namespaces=STD_TEX_NS)

    @staticmethod
    def getGroups(node):
        return node.findall('./svg:g', namespaces=STD_TEX_NS)

    @staticmethod
    def getUse(node):
        return node.find('./svg:g/svg:use', namespaces=STD_TEX_NS)

    @staticmethod
    def getUses(node):
        return node.findall('./svg:g/svg:use', namespaces=STD_TEX_NS)

    @staticmethod
    def makeConfig(config):
        DEF_CACHE = True
        DEF_CONTENT = 'no content'
        DEF_SIZE = (sys.maxsize, 1080/4)
        DEF_FILL = '#ffffff'
        DEF_POSITION = (0, 0)

        config = copy.deepcopy(config)

        if not tatr.cache in config:
            config[tatr.cache] = DEF_CACHE

        if not tatr.content in config:
            config[tatr.content] = DEF_CONTENT
        config[tatr.content] = Tex.makeContent(config)

        if not tatr.fill in config:
            config[tatr.fill] = DEF_FILL

        if not tatr.position in config:
            config[tatr.position] = DEF_POSITION

        if not tatr.size in config:
            config[tatr.size] = DEF_SIZE

        return res

    @staticmethod
    def makeContent(config):
        res = config[tatr.content]
        res = '\\pagenumbering{gobble}\n' + res
        return res

    @staticmethod
    def makeName(config):
        content = config[tatr.content]
        hashObj = sha256()
        hashObj.update(content.encode('utf-8'))
        res = hashObj.hexdigest()
        return res

    @staticmethod
    def makeNode(config):
        """
        None -> ET.Element
        this only works if you wrote the file already
        """
        content = config[tatr.content]
        name = config[tatr.name]

        name = Tex.makeName(config)
        path = Tex.makePath(config)

        if not os.path.isfile(path) or not cache:
            writer = TexWriter(content)
            writer.write(clean=True)
        res = ET.parse(path).getroot()

        Tex.applyFill(res, config)
        Tex.applyPosition(res, config)
        Tex.applySize(res, config)

        # deprecated, use translate
        # if position:
        #     Tex.applyPosition(res, position)

        return res

    @staticmethod
    def makePath(config):
        name = Tex.makeName(config)
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
