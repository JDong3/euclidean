import sys
sys.path.insert(0, '../../objects')

from Point import Point
from Scene import Scene
import styles

scene = Scene(styles.resolution)

x, y = round(scene.width/2), round(scene.height/2)
point = Point(x, y)
scene.add(point.node())

x, y = 100, 100
lower_left = Point(x, y)
scene.add(lower_left.node())

scene.write('test.svg')
