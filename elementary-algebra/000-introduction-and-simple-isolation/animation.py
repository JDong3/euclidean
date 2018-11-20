import sys
sys.path.insert(0, '../../objects')

import os
from Tex import Tex
from Math import Math
from Template import Template
from Point import Point
from Frame import Frame
from Scene import Scene
from Line import Line
from Circle import Circle
from Quote import Quote
import styles


# make quote
p = Point(400, 400)
outer = Point(500, 500)
c = Circle(p, outer)
f = Frame()
f.add(c.node())
f.write('circ.svg')




t = Tex(Math(r'\sum_{i = 0}^{n} i + i2^i').out)
if False:
    # tex demo
    x = Template(['mathtools'])
    x.writeTemplate()

    t.writeSvg()

    # video demo
    a_x, a_y = 0, 0
    a = Point(a_x, a_y)

    b_x, b_y = 1920, 1080
    b = Point(b_x, b_y)

    line = Line(a, b)

    lst = Line.construct(line, 60)

    scene = Scene.fromNodeList(lst)
    scene.writeVideo('video-out')

if False:
    os.remove(f'{t.name}.svg')
    os.remove('video-out/out.mp4')
    os.removedirs('video-out')
    os.remove('template.tex')
