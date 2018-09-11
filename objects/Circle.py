import lxml.etree as ET
import styles
from Line import Line

class Circle:
    def __init__(self, center, outer, style_update={}):
        """
        Point, Point, dict -> None
        :param center: the Point that is the center of the circle
        :param outer: a point on the circle
        :param [style_update]: dictionary to update the default style of the
            circle
        """
        default = styles.circle

        self.center = center
        self.r = Line(self.center, outer).length()
        properties = {
            'r': str(self.r),
            'cx': str(self.center.x),
            'cy': str(self.center.y)
        }
        self._style = {**default, **style_update, **properties}

    def node(self):
        """
        None -> lxml.etree.Element
        :return: the lxml.etree.Element that represents the circle
        """
        return ET.Element('circle', self._style)
