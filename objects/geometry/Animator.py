from .Circle import Circle
from .Line import Line
from .Point import Point

class Animator:
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
            res.append(next_line.node)
        return res
