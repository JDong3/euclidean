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
    tatr.radian: 1.5 * np.pi,
    tatr.position: b.position,
    tatr.distance: 25
}
la = Label(config)

ll = LabeledLine(li, la)
ll.Frame.write('frame1')
