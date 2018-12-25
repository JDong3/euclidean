from Point import Point
import lxml.etree as ET
import styles
import math

class Line:
    def __init__(self, a, b, style_update={}):
        """
        point, point, dict -> None
        :param a: a point on the line
        :param b: a point on the line
        :param [style_update]: the updated style of the line
        """
        self.a = a
        self.b = b

        self.dx = self.b.x - self.a.x
        self.dy = self.b.y - self.a.y

        # length of the line
        self.length = math.sqrt(self.dx**2 + self.dy**2)
        # rounded length of the line
        self.rlength = round(self.length)

        # style sheet for the line
        self.__style = {**styles.line, **style_update}
        self.__style['x1'] = str(a.x)
        self.__style['y1'] = str(a.y)
        self.__style['x2'] = str(b.x)
        self.__style['y2'] = str(b.y)

        self.node = ET.Element('line', self.__style)
