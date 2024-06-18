import unittest
import math

from geometry import rectangle_area, rectangle_perimeter, circle_area, circle_circumference

class TestGeometry(unittest.TestCase):
    def test_rectangle_area(self):
        self.assertEqual(rectangle_area(2, 3), 6)
        self.assertEqual(rectangle_area(8, 5), 40)
        self.assertEqual(rectangle_area(1, 1), 1)

    def test_rectangle_perimeter(self):
        self.assertEqual(rectangle_perimeter(2, 3), 10)
        self.assertEqual(rectangle_perimeter(8, 5), 26)
        self.assertEqual(rectangle_perimeter(1, 1), 4)

    def test_circle_area(self):
        self.assertEqual(circle_area(10.0), 314.1592653589793)
        self.assertEqual(circle_area(4.0), 50.26548245743669)
        self.assertEqual(circle_area(2.0), 12.566370614359172)

    def test_circle_circumference(self):
        self.assertEqual(circle_circumference(10.0), 62.83185307179586)
        self.assertEqual(circle_circumference(4.0), 25.132741228718345)
        self.assertEqual(circle_circumference(2.0), 12.566370614359172) 
if __name__ == '__main__':
    unittest.main()
