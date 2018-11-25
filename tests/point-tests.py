import sys
import lxml.etree as ET

sys.path.insert(0, '../objects')

import unittest
from Point import Point

class SimpleTests(unittest.TestCase):
    def setUp(self):
        self.x = 15
        self.y = 25
        self.point = Point(self.x, self.y)

    def testXy(self):
        self.assertIs(type(self.point.x), int)
        self.assertIs(type(self.point.y), int)

        self.assertEqual(self.point.x, self.x)
        self.assertEqual(self.point.y, self.y)

    def testStyle(self):
        self.assertIs(type(self.point.style), dict)
        self.assertEqual(self.point.style['cx'], str(self.x))
        self.assertEqual(self.point.style['cy'], str(self.y))

    def testNode(self):
        self.assertIs(type(self.point.node), ET._Element)


if __name__ == '__main__':
    unittest.main()
