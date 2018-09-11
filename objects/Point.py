import styles
import lxml.etree as ET

class Point:
    def __init__(self, x, y, style_update={}):
        """
        int, int, dict -> None
        :param x: the x location of the point
        :param y: the y location of the point
        :param [style_update]: dictioary to update the default
        """
        self.update(x, y)
        self._style = {**styles.point, **style_update}

    def update(self, x, y):
        """
        int, int -> None
        :param x: new x coordinate
        :param y: new y coordinate
        """
        self.x = x
        self.y = y
        location = {
            'cx': str(self.x),
            'cy': str(self.y)
        }
        self._style = {**self._style, **location}


    def markup(self):
        """
        None -> str
        :return: the markup for the lxml.etree.Element that represents the point
        """
        return ET.tostring(self.node())

    def node(self):
        """
        None -> lxml.etree.Element
        :return: the lxml.etree.Element that represents the point
        """
        return ET.Element('circle', self._style)
