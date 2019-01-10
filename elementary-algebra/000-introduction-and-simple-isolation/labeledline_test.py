import sys
sys.path.insert(0, '../../objects')

import geometry.Point as Point
import geometry.Line as Line
import typesetting.Label as Label
import compound.LabeledLine as LabeledLine
import typesetting.tatr as tatr
import numpy as np

a = Point(10, 10)
b = Point(100, 100)
li = Line(a, b)

config = {
    tatr.content: '123',
    tatr.radian: 1.75 * np.pi,
    tatr.position: (100, 100),
    tatr.distance: 25,
    tatr.size: (sys.maxsize, 100)
}
la = Label(config)
la.frame.write('label1', png=True)

ll = LabeledLine(li, la)
ll.frame.write('frame1', png=True)
la.frame.write('label2', png=True)
