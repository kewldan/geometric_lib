import math
import sys
import unittest

from square import area, perimeter


class SquareAreaTestCase(unittest.TestCase):
    def test_zero_side(self):
        self.assertEqual(area(0), 0)

    def test_integer_side(self):
        self.assertEqual(area(5), 25)

    def test_float_side(self):
        self.assertAlmostEqual(area(2.5), 6.25)

    def test_negative_side(self):
        with self.assertRaises(ValueError):
            area(-5)

    def test_string_side(self):
        with self.assertRaises(TypeError):
            area("5")

    def test_inf_side(self):
        with self.assertRaises(ValueError):
            area(math.inf)

    def test_negative_inf_side(self):
        with self.assertRaises(ValueError):
            area(-math.inf)

    def test_nan_side(self):
        with self.assertRaises(ValueError):
            area(math.nan)

    def test_negative_zero_side(self):
        self.assertEqual(area(-0.0), 0)

    def test_large_side(self):
        self.assertAlmostEqual(area(1e150), 1e300, delta=1e291)

    def test_overflow(self):
        with self.assertRaises(OverflowError):
            area(1e200)

    def test_huge_int_side(self):
        self.assertEqual(area(10**200), 10**400)

    def test_tiny_side(self):
        self.assertAlmostEqual(area(1e-150), 1e-300, delta=1e-309)

    def test_underflow(self):
        result = area(1e-200)
        self.assertTrue(math.isfinite(result))
        self.assertGreaterEqual(result, 0)


class SquarePerimeterTestCase(unittest.TestCase):
    def test_zero_side(self):
        self.assertEqual(perimeter(0), 0)

    def test_integer_side(self):
        self.assertEqual(perimeter(5), 20)

    def test_float_side(self):
        self.assertAlmostEqual(perimeter(0.25), 1.0)

    def test_negative_side(self):
        with self.assertRaises(ValueError):
            perimeter(-5)

    def test_string_side(self):
        with self.assertRaises(TypeError):
            perimeter("5")

    def test_inf_side(self):
        with self.assertRaises(ValueError):
            perimeter(math.inf)

    def test_negative_inf_side(self):
        with self.assertRaises(ValueError):
            perimeter(-math.inf)

    def test_nan_side(self):
        with self.assertRaises(ValueError):
            perimeter(math.nan)

    def test_negative_zero_side(self):
        self.assertEqual(perimeter(-0.0), 0)

    def test_large_side(self):
        self.assertEqual(perimeter(1e300), 4e300)

    def test_overflow(self):
        with self.assertRaises(OverflowError):
            perimeter(sys.float_info.max)

    def test_huge_int_side(self):
        self.assertEqual(perimeter(10**400), 4 * 10**400)

    def test_tiny_side(self):
        self.assertEqual(perimeter(1e-300), 4e-300)

    def test_subnormal_side(self):
        self.assertEqual(perimeter(5e-324), 2e-323)
