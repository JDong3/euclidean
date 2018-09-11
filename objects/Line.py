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
        self._style = {**styles.line, **style_update}
        self.update(a, b)

    def update(self, a, b):
        """
        Point, Point -> None
        :param a: the new location for point a
        :param b: the new location for point b
        """
        self.a = a
        self.b = b

        points_location = {
            'x1': str(self.a.x),
            'y1': str(self.a.y),
            'x2': str(self.b.x),
            'y2': str(self.b.y)
        }

        self._style = {**self._style, **points_location}

    def node(self):
        """
        None -> lxml.etree.Element
        :return: the lxml.etree.Element that represents the line
        """
        return ET.Element('line', self._style)

    def length(self, roundOff=True):
        """
        bool -> int or float
        :param [roundOff]: if you want to round the result or note
        :return: the length of the line
        """
        delta_x = self.a.x - self.b.x
        delta_y = self.a.y - self.b.y
        res = math.sqrt(delta_x**2 + delta_y**2)
        return roundOff and round(res) or not roundOff and res

    def dx(self):
        """
        None -> int
        """
        return self.a.x - self.b.x

    def dy(self):
        """
        None -> int
        """
        return self.a.y - self.b.y

    def construct(self, frame_count):
        """
        int -> list<lxml.etree.Element>
        :returns: returns a list that is the animation of a line being drawn
            from self.a to self.b
        """
        res = []

        # offset_x/y computes the x/y of of b at the ith frame wrt a
        offset_x = lambda i: self.a.x + (i * self.dx)/(1-frame_count)
        offset_y = lambda i: self.a.y + (i * self.dy)/(1-frame_count)
        # b(i) compuths the location of b at the ith frame
        b = lambda i: (self.a.x + offset_x(i), self.b.x + offset_y(i))

        for i in range(frame_count):
            x_i, y_i = b(i)
            b_i =
            self.update()


        return None
