import sys
sys.path.insert(0, '../../objects')

from Point import Point
from Frame import Frame
from Line import Line
from Circle import Circle
import styles

frame = Frame(styles.resolution)

x, y = round(frame.width/2), round(frame.height/2)
point = Point(x, y)
frame.add(point.node())

x, y = 100, 100
lower_left = Point(x, y)
frame.add(lower_left.node())

line = Line(point, lower_left)
frame.add(line.node())

circle = Circle(point, lower_left)
frame.add(circle.node())

frame.write('test.svg')
