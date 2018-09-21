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
        self.x = x
        self.y = y
        self.__style = {**styles.point, **style_update}
        self.__style['cx'] = str(self.x)
        self.__style['cy'] = str(self.y)

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
        return ET.Element('circle', self.__style)
