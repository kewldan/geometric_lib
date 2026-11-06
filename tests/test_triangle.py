import math
import unittest

from triangle import area, perimeter


class TriangleAreaTestCase(unittest.TestCase):
    def test_zero_height(self):
        self.assertEqual(area(5, 0), 0)

    def test_integer_values(self):
        self.assertEqual(area(4, 3), 6)

    def test_odd_product(self):
        self.assertAlmostEqual(area(1, 1), 0.5)

    def test_negative_height(self):
        with self.assertRaises(ValueError):
            area(4, -3)

    def test_string_args(self):
        with self.assertRaises(TypeError):
            area("4", "-3")

    def test_inf_args(self):
        with self.assertRaises(ValueError):
            area(math.inf, 1)
        with self.assertRaises(ValueError):
            area(1, math.inf)

    def test_negative_inf_args(self):
        with self.assertRaises(ValueError):
            area(-math.inf, 1)
        with self.assertRaises(ValueError):
            area(1, -math.inf)

    def test_nan_args(self):
        with self.assertRaises(ValueError):
            area(math.nan, 1)
        with self.assertRaises(ValueError):
            area(1, math.nan)

    def test_negative_zero_height(self):
        self.assertEqual(area(5, -0.0), 0)

    def test_large_values(self):
        self.assertAlmostEqual(area(1e150, 1e150), 5e299, delta=1e290)

    def test_overflow(self):
        with self.assertRaises(OverflowError):
            area(1e200, 1e200)

    def test_huge_int_values(self):
        self.assertAlmostEqual(area(10**200, 10**100), 5e299, delta=1e290)

    def test_huge_int_overflow(self):
        with self.assertRaises(OverflowError):
            area(2 * 10**200, 10**200)

    def test_underflow(self):
        result = area(1e-200, 1e-200)
        self.assertTrue(math.isfinite(result))
        self.assertGreaterEqual(result, 0)


class TrianglePerimeterTestCase(unittest.TestCase):
    def test_equilateral(self):
        self.assertEqual(perimeter(1, 1, 1), 3)

    def test_right_triangle(self):
        self.assertEqual(perimeter(3, 4, 5), 12)

    def test_float_sides(self):
        self.assertAlmostEqual(perimeter(0.1, 0.2, 0.25), 0.55)

    def test_negative_side(self):
        with self.assertRaises(ValueError):
            perimeter(-3, 4, 5)

    def test_triangle_inequality(self):
        with self.assertRaises(ValueError):
            perimeter(1, 2, 10)

    def test_string_arguments(self):
        with self.assertRaises(TypeError):
            perimeter("1", "2", "10")

    def test_inf_sides(self):
        with self.assertRaises(ValueError):
            perimeter(math.inf, 1, 1)
        with self.assertRaises(ValueError):
            perimeter(1, 1, math.inf)

    def test_negative_inf_sides(self):
        with self.assertRaises(ValueError):
            perimeter(-math.inf, 1, 1)
        with self.assertRaises(ValueError):
            perimeter(1, 1, -math.inf)

    def test_nan_sides(self):
        with self.assertRaises(ValueError):
            perimeter(math.nan, 1, 1)
        with self.assertRaises(ValueError):
            perimeter(1, 1, math.nan)

    def test_all_inf_sides(self):
        with self.assertRaises(ValueError):
            perimeter(math.inf, math.inf, math.inf)

    def test_large_sides(self):
        self.assertAlmostEqual(
            perimeter(1e300, 1e300, 1e300), 3e300, delta=1e291)

    def test_overflow(self):
        with self.assertRaises(OverflowError):
            perimeter(1e308, 1e308, 1e308)

    def test_huge_int_sides(self):
        self.assertEqual(perimeter(10**400, 10**400, 10**400), 3 * 10**400)

    def test_thin_isosceles(self):
        self.assertAlmostEqual(
            perimeter(1e300, 1e300, 1e-300), 2e300, delta=1e291)

    def test_tiny_sides(self):
        self.assertAlmostEqual(
            perimeter(1e-300, 1e-300, 1e-300), 3e-300, delta=1e-309)
