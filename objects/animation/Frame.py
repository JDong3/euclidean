import lxml.etree as ET
import subprocess as sp

from .constants import DEFAULT_BACKGROUND
from .styles import RESOLUTION

class Frame:
    def __init__(self, node, resolution=RESOLUTION):
        """
        dict -> None
        :param resolution: a dictionary specifying the resolution of the frame
        """
        self._root = ET.Element('svg', resolution)
        self.add(node)
        print(node)
        self.width = int(resolution['width'])
        self.height = int(resolution['height'])

    def add(self, node):
        """
        ET.Element -> None
        :param node: an ET.Element object that you want to add to the frame
        """
        self._root.append(node)

    def write(self, file, mode='wb', png=False):
        """
        str, str -> None
        :param file: file name to write to
        :param [mode]: file write mode
        """
        tree = ET.ElementTree(self._root)

        with open(f'{file}.svg', mode) as f:
            print('prelim --------------------')
            print(ET.tostring(tree))
            tree.write(open(f'{file}.svg', mode))

        with open(f'{file}.svg', 'r') as f:
            print('part 1 --------------------')
            print(ET.tostring(tree))
            print('part 2 ---------------------')
            print(f.read())
            print('done ============================================')

        if png:
            args = [
                'inkscape',
                '-z',
                f'{file}.svg',
                '-e', f'{file}.png',
                '-b', DEFAULT_BACKGROUND
            ]
            sp.run(args)
