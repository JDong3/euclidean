import lxml.etree as ET
import styles

class Scene:
    def __init__(self, resolution=styles.resolution):
        self._root = ET.Element('svg', resolution)

    def add(self, node):
        """
        ET.Element -> Scene
        """
        return None

    def write(self, file, mode='wb'):
        """
        str, str -> None
        file: file name to write to
        [mode]: file write mode
        """
        tree = ET.ElementTree(self._root)
        tree.write(open(file, mode))
