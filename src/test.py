from Point import Point
import lxml.etree as ET

point = Point(1, 2)
print(point.markup())

root = ET.Element('svg', {'width': '100', 'height': '100'})
root.append(point.node())
document = ET.ElementTree(root)
print(document)
print(ET.tostring(root))

with open('xd.svg', 'wb') as f:
    document.write(f)
