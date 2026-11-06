import math
import unittest

from rectangle import area, perimeter


class RectangleAreaTestCase(unittest.TestCase):
    def test_zero_mul(self):
        self.assertEqual(area(10, 0), 0)

    def test_square_mul(self):
        self.assertEqual(area(10, 10), 100)

    def test_different_sides(self):
        self.assertEqual(area(3, 4), 12)

    def test_commutative(self):
        self.assertEqual(area(3, 4), area(4, 3))

    def test_float_sides(self):
        self.assertAlmostEqual(area(1.5, 2), 3.0)

    def test_negative_side(self):
        with self.assertRaises(ValueError):
            area(-3, 4)

    def test_string_args(self):
        with self.assertRaises(TypeError):
            area("-3", "4")

    def test_inf_side(self):
        with self.assertRaises(ValueError):
            area(math.inf, 1)
        with self.assertRaises(ValueError):
            area(1, math.inf)

    def test_negative_inf_side(self):
        with self.assertRaises(ValueError):
            area(-math.inf, 1)
        with self.assertRaises(ValueError):
            area(1, -math.inf)

    def test_nan_side(self):
        with self.assertRaises(ValueError):
            area(math.nan, 1)
        with self.assertRaises(ValueError):
            area(1, math.nan)

    def test_inf_times_zero(self):
        with self.assertRaises(ValueError):
            area(math.inf, 0)

    def test_negative_zero_side(self):
        self.assertEqual(area(-0.0, 5), 0)

    def test_large_and_tiny_sides(self):
        self.assertAlmostEqual(area(1e200, 1e-200), 1.0, delta=1e-9)

    def test_overflow(self):
        with self.assertRaises(OverflowError):
            area(1e200, 1e200)

    def test_huge_int_sides(self):
        self.assertEqual(area(10**200, 10**300), 10**500)

    def test_tiny_sides(self):
        self.assertAlmostEqual(area(1e-150, 1e-150), 1e-300, delta=1e-309)

    def test_underflow(self):
        result = area(1e-200, 1e-200)
        self.assertTrue(math.isfinite(result))
        self.assertGreaterEqual(result, 0)


class RectanglePerimeterTestCase(unittest.TestCase):
    def test_zero_sides(self):
        self.assertEqual(perimeter(0, 0), 0)

    def test_different_sides(self):
        self.assertEqual(perimeter(3, 4), 14)

    def test_float_sides(self):
        self.assertAlmostEqual(perimeter(1.5, 2.5), 8.0)

    def test_negative_side(self):
        with self.assertRaises(ValueError):
            perimeter(-3, 4)

    def test_string_args(self):
        with self.assertRaises(TypeError):
            perimeter("-3", "4")

    def test_inf_side(self):
        with self.assertRaises(ValueError):
            perimeter(math.inf, 1)
        with self.assertRaises(ValueError):
            perimeter(1, math.inf)

    def test_negative_inf_side(self):
        with self.assertRaises(ValueError):
            perimeter(-math.inf, 1)
        with self.assertRaises(ValueError):
            perimeter(1, -math.inf)

    def test_nan_side(self):
        with self.assertRaises(ValueError):
            perimeter(math.nan, 1)
        with self.assertRaises(ValueError):
            perimeter(1, math.nan)

    def test_negative_zero_side(self):
        self.assertEqual(perimeter(-0.0, 5), 10)

    def test_overflow(self):
        with self.assertRaises(OverflowError):
            perimeter(1e308, 1e308)

    def test_huge_int_sides(self):
        self.assertEqual(perimeter(10**400, 1), 2 * 10**400 + 2)

    def test_tiny_sides(self):
        self.assertEqual(perimeter(1e-300, 1e-300), 4e-300)
