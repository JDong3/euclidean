import sys
sys.path.insert(0, '../../objects')

from Point import Point
from Frame import Frame
from Scene import Scene
from Line import Line
from Circle import Circle
import styles

a_x, a_y = 100, 100
a = Point(a_x, a_y)

b_x, b_y = 300, 300
b = Point(b_x, b_y)

line = Line(a, b)

lst = Line.construct(line, 300)

for i, element in enumerate(lst):
    frame = Frame(styles.resolution)
    frame.add(lst[i])
    lst[i] = frame

scene = Scene()
for i, frame in enumerate(lst):
    scene.add(frame)

scene.write('testdir')
# convert *.svg out_%05d.png
# ffmpeg -framerate 60 -i out_%05d.png -pix_fmt yuv420p out.mp4
