import math
import unittest

from circle import area, perimeter


class CircleAreaTestCase(unittest.TestCase):
    def test_zero_radius(self):
        self.assertEqual(area(0), 0)

    def test_unit_radius(self):
        self.assertAlmostEqual(area(1), math.pi)

    def test_integer_radius(self):
        self.assertAlmostEqual(area(2), 4 * math.pi)

    def test_float_radius(self):
        self.assertAlmostEqual(area(0.5), 0.25 * math.pi)

    def test_negative_radius(self):
        with self.assertRaises(ValueError):
            area(-1)

    def test_negative_side(self):
        with self.assertRaises(TypeError):
            area("3")

    def test_inf_radius(self):
        with self.assertRaises(ValueError):
            area(math.inf)

    def test_negative_inf_radius(self):
        with self.assertRaises(ValueError):
            area(-math.inf)

    def test_nan_radius(self):
        with self.assertRaises(ValueError):
            area(math.nan)

    def test_negative_zero_radius(self):
        self.assertEqual(area(-0.0), 0)

    def test_large_radius(self):
        self.assertAlmostEqual(area(1e150), math.pi * 1e300, delta=1e291)

    def test_overflow(self):
        with self.assertRaises(OverflowError):
            area(1e200)

    def test_huge_int_radius(self):
        with self.assertRaises(OverflowError):
            area(10**400)

    def test_tiny_radius(self):
        self.assertAlmostEqual(area(1e-150), math.pi * 1e-300, delta=1e-309)

    def test_underflow(self):
        result = area(1e-200)
        self.assertTrue(math.isfinite(result))
        self.assertGreaterEqual(result, 0)


class CirclePerimeterTestCase(unittest.TestCase):
    def test_zero_radius(self):
        self.assertEqual(perimeter(0), 0)

    def test_unit_radius(self):
        self.assertAlmostEqual(perimeter(1), 2 * math.pi)

    def test_float_radius(self):
        self.assertAlmostEqual(perimeter(2.5), 5 * math.pi)

    def test_negative_radius(self):
        with self.assertRaises(ValueError):
            perimeter(-1)

    def test_string_args(self):
        with self.assertRaises(TypeError):
            perimeter("2")

    def test_inf_radius(self):
        with self.assertRaises(ValueError):
            perimeter(math.inf)

    def test_negative_inf_radius(self):
        with self.assertRaises(ValueError):
            perimeter(-math.inf)

    def test_nan_radius(self):
        with self.assertRaises(ValueError):
            perimeter(math.nan)

    def test_negative_zero_radius(self):
        self.assertEqual(perimeter(-0.0), 0)

    def test_large_radius(self):
        self.assertAlmostEqual(
            perimeter(1e300), 2 * math.pi * 1e300, delta=1e291)

    def test_overflow(self):
        with self.assertRaises(OverflowError):
            perimeter(1e308)

    def test_tiny_radius(self):
        self.assertAlmostEqual(
            perimeter(1e-300), 2 * math.pi * 1e-300, delta=1e-309)

    def test_subnormal_radius(self):
        self.assertGreater(perimeter(5e-324), 0)
