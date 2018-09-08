import styles
import lxml.etree as ET

class Point:
    def __init__(self, x, y, style_update=dict()):
        """
        int, int, dict -> None
        :param x: the x location of the point
        :param y: the y location of the point
        :param [style_update]: dictioary to update the default
        """
        let default = styles.point

        self.x = x
        self.y = y
        self._location = {
            'cx': str(self.x),
            'cy': str(self.y)
        }
        self._style = {**default, **style_update, **self._location}


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
