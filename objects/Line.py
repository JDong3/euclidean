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

        self.__style = {**styles.line, **style_update}
        self.__style['x1'] = str(self.a.x)
        self.__style['y1'] = str(self.a.y)
        self.__style['x2'] = str(self.b.x)
        self.__style['y2'] = str(self.b.y)

    def node(self):
        """
        None -> lxml.etree.Element
        :return: the lxml.etree.Element that represents the line
        """
        return ET.Element('line', self.__style)

    def length(self, roundOff=True):
        """
        bool -> int or float
        :param [roundOff]: if you want to round the result or note
        :return: the length of the line
        """
        res = math.sqrt(self.dx**2 + self.dy**2)
        return roundOff and round(res) or not roundOff and res

    @staticmethod
    def construct(line, frame_count):
        """
        int -> list<lxml.etree.Element>
        :returns: returns a list that is the animation of a line being drawn
            from self.a to self.b
        """
        res = []
        # offset_x/y computes the x/y of of b at the ith frame wrt a
        offset_x = lambda i: int((i * line.dx)/(frame_count-1))
        offset_y = lambda i: int((i * line.dy)/(frame_count-1))
        # b(i) compuths the location of b at the ith frame
        b = lambda i: (line.a.x + offset_x(i), line.a.y + offset_y(i))
        a = line.a
        for i in range(frame_count):
            b_i =  Point(*b(i))
            next_line = Line(a, b_i)
            res.append(next_line.node())
        return res
