import lxml.etree as ET
from .styles import RESOLUTION

class Frame:
    def __init__(self, node, resolution=RESOLUTION):
        """
        dict -> None
        :param resolution: a dictionary specifying the resolution of the frame
        """
        self._root = ET.Element('svg', resolution)
        self.add(node)
        self.width = int(resolution['width'])
        self.height = int(resolution['height'])

    def add(self, node):
        """
        ET.Element -> None
        :param node: an ET.Element object that you want to add to the frame
        """
        self._root.append(node)

    def write(self, file, mode='wb'):
        """
        str, str -> None
        :param file: file name to write to
        :param [mode]: file write mode
        """
        tree = ET.ElementTree(self._root)
        with open(file, mode) as f:
            tree.write(open(file, mode))
