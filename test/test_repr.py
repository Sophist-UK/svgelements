import io
import unittest

from svgelements import *


class TestElementsRepr(unittest.TestCase):
    """Tests the functionality of the repr for elements."""

    def test_repr_length(self):
        obj = Length("10cm")
        self.assertTrue(obj == eval(repr(obj)))
        self.assertFalse(obj != eval(repr(obj)))

    def test_repr_color(self):
        obj = Color("red")
        self.assertTrue(obj == eval(repr(obj)))
        self.assertFalse(obj != eval(repr(obj)))

    def test_repr_point(self):
        obj = Point("20.3,3.1615926535")
        self.assertTrue(obj == eval(repr(obj)))
        self.assertFalse(obj != eval(repr(obj)))

    def test_repr_angle(self):
        obj = Angle.parse("1.1turn")
        self.assertAlmostEqual(obj, eval(repr(obj)))

    def test_repr_matrix(self):
        obj = Matrix("rotate(20)")
        self.assertTrue(obj == eval(repr(obj)))
        self.assertFalse(obj != eval(repr(obj)))

    def test_repr_viewbox(self):
        obj = Viewbox("0 0 100 60")
        print(repr(obj))
        self.assertTrue(obj == eval(repr(obj)))
        self.assertFalse(obj != eval(repr(obj)))

    def test_repr_move(self):
        obj = Move(0.1, 50)
        self.assertTrue(obj == eval(repr(obj)))
        self.assertFalse(obj != eval(repr(obj)))

    def test_repr_close(self):
        obj = Close(0.1, 50)
        self.assertTrue(obj == eval(repr(obj)))
        self.assertFalse(obj != eval(repr(obj)))

    def test_repr_line(self):
        obj = Line(start=(0.2, 0.99), end=(0.1, 22.9996))
        self.assertTrue(obj == eval(repr(obj)))
        self.assertFalse(obj != eval(repr(obj)))

        obj = Line(end=(0.1, 22.9996))
        self.assertTrue(obj == eval(repr(obj)))
        self.assertFalse(obj != eval(repr(obj)))

    def test_repr_qbez(self):
        obj = QuadraticBezier(start=(0.2, 0.99), control=(-3,-3), end=(0.1, 22.9996))
        self.assertTrue(obj == eval(repr(obj)))
        self.assertFalse(obj != eval(repr(obj)))

    def test_repr_cbez(self):
        obj = CubicBezier(start=(0.2, 0.99), control1=(-3, -3), control2=(-4, -4), end=(0.1, 22.9996))
        self.assertTrue(obj == eval(repr(obj)))
        self.assertFalse(obj != eval(repr(obj)))

    def test_repr_arc(self):
        obj = Arc(start=(0,0), end=(0,100), control=(50,50))
        self.assertTrue(obj == eval(repr(obj)))
        self.assertFalse(obj != eval(repr(obj)))

    def test_repr_path(self):
        obj = Path("M0,0Z")
        self.assertTrue(obj == eval(repr(obj)))
        self.assertFalse(obj != eval(repr(obj)))

        obj = Path("M0,0L100,100Z")
        self.assertTrue(obj == eval(repr(obj)))
        self.assertFalse(obj != eval(repr(obj)))

        obj = Path("M0,0L100,100Z", transform="scale(4)")
        self.assertTrue(obj == eval(repr(obj)))
        self.assertFalse(obj != eval(repr(obj)))

    def test_repr_rect(self):
        obj = Rect(x=100, y=100, width=500, height=500)
        self.assertTrue(obj == eval(repr(obj)))
        self.assertFalse(obj != eval(repr(obj)))

        obj = Rect(x=100, y=100, width=500, height=500, transform="scale(2)", stroke="red", fill="blue")
        self.assertTrue(obj == eval(repr(obj)))
        self.assertFalse(obj != eval(repr(obj)))

    def test_repr_ellipse(self):
        obj = Ellipse(cx=100, cy=100, rx=500, ry=500)
        self.assertTrue(obj == eval(repr(obj)))
        self.assertFalse(obj != eval(repr(obj)))

        obj = Ellipse(cx=100, cy=100, rx=500, ry=500, transform="scale(2)", stroke="red", fill="blue")
        self.assertTrue(obj == eval(repr(obj)))
        self.assertFalse(obj != eval(repr(obj)))

    def test_repr_circle(self):
        obj = Circle(cx=100, cy=100, r=500)
        self.assertTrue(obj == eval(repr(obj)))
        self.assertFalse(obj != eval(repr(obj)))

        obj = Circle(cx=100, cy=100, r=500, transform="scale(2)", stroke="red", fill="blue")
        self.assertTrue(obj == eval(repr(obj)))
        self.assertFalse(obj != eval(repr(obj)))

    def test_repr_simpleline(self):
        obj = SimpleLine(start=(0,0), end=(100,100))
        self.assertTrue(obj == eval(repr(obj)))
        self.assertFalse(obj != eval(repr(obj)))

        obj = SimpleLine(start=(0, 0), end=(100, 100), transform="scale(2)", stroke="red", fill="blue")
        self.assertTrue(obj == eval(repr(obj)))
        self.assertFalse(obj != eval(repr(obj)))

    def test_repr_polyline(self):
        obj = Polyline("0,0 7,7 10,10 0 20")
        self.assertTrue(obj == eval(repr(obj)))
        self.assertFalse(obj != eval(repr(obj)))

        obj = Polyline("0,0 7,7 10,10 0 20", transform="scale(2)", stroke="red", fill="blue")
        self.assertTrue(obj == eval(repr(obj)))
        self.assertFalse(obj != eval(repr(obj)))

    def test_repr_polygon(self):
        obj = Polygon("0,0 7,7 10,10 0 20")
        self.assertTrue(obj == eval(repr(obj)))
        self.assertFalse(obj != eval(repr(obj)))

        obj = Polygon("0,0 7,7 10,10 0 20", transform="scale(2)", stroke="red", fill="blue")
        self.assertTrue(obj == eval(repr(obj)))
        self.assertFalse(obj != eval(repr(obj)))

    def test_repr_group(self):
        obj = Group()
        self.assertTrue(obj == eval(repr(obj)))
        self.assertFalse(obj != eval(repr(obj)))

        obj = Group(transform="scale(2)", stroke="red", fill="blue")
        self.assertTrue(obj == eval(repr(obj)))
        self.assertFalse(obj != eval(repr(obj)))

    def test_repr_clippath(self):
        obj = ClipPath()
        self.assertTrue(obj == eval(repr(obj)))
        self.assertFalse(obj != eval(repr(obj)))

    def test_repr_pattern(self):
        obj = Pattern()
        self.assertTrue(obj == eval(repr(obj)))
        self.assertFalse(obj != eval(repr(obj)))

    def test_repr_text(self):
        obj = Text(x=0, y=0, text="Hello")
        self.assertTrue(obj == eval(repr(obj)))
        self.assertFalse(obj != eval(repr(obj)))

        obj = Text(x=0, y=0, text="Hello", transform="scale(2)", stroke="red", fill="blue")
        self.assertTrue(obj == eval(repr(obj)))
        self.assertFalse(obj != eval(repr(obj)))

    def test_repr_image(self):
        obj = Image(url="test.png", transform="scale(2)")
        obj_repr = repr(obj)
        self.assertTrue(obj == eval(repr(obj)))
        self.assertFalse(obj != eval(repr(obj)))

    def test_repr_desc(self):
        obj = Desc("Describes Object")
        self.assertTrue(obj == eval(repr(obj)))
        self.assertFalse(obj != eval(repr(obj)))

    def test_repr_title(self):
        obj = Title(title="SVG Description")
        self.assertTrue(obj == eval(repr(obj)))
        self.assertFalse(obj != eval(repr(obj)))

