import styles
import lxml.etree as ET

class Point:
    def __init__(self, x, y, style_update=None, style=styles.point):
        self._x = x
        self._y = y

        self._style = style.update(style_update) if style_update else style


    def markup(self):
        return ET.tostring(self.node())

    def node(self):
        return ET.Element('circle', self._style)
