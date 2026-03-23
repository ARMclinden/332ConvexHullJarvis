import unittest
from main import convex_hull_jarvis


class TestMathFunctions(unittest.TestCase):
    
    def test_example_from_prompt(self):
        self.assertEqual(convex_hull_jarvis([(0, 3), (2, 2), (1, 1), (2, 1), (3, 0), (0, 0), (3, 3)]), [(0, 0), (0, 3), (3, 3), (3, 0)])

    def test_square_with_inner_points(self):
        self.assertEqual(convex_hull_jarvis([(0, 10), (6, 3), (9, 9), (3, 2), (10, 0), (0, 0), (10, 10)]), [(0, 0), (0, 10), (10, 10), (10, 0)])

    def test_duplicates(self):
        self.assertEqual(convex_hull_jarvis([(0, 3), (2, 2), (0, 3), (1, 1), (3, 0), (2, 1), (2, 1), (3, 0), (0, 0), (3, 3), (3, 3)]), [(0, 0), (0, 3), (3, 3), (3, 0)])

    def test_all_collinear(self):
        self.assertEqual(convex_hull_jarvis([(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7)]), [(1, 1), (2, 2)])

    def test_two_points(self):
        self.assertEqual(convex_hull_jarvis([(1, 1), (3, 3)]), [(1, 1), (3, 3)])

    def test_single_point(self):
       self.assertEqual(convex_hull_jarvis([(1, 1)]), [(1, 1)])

    def test_triangle(self):
        self.assertEqual(convex_hull_jarvis([(0, 0), (2, 4), (4, 0)]), [(0, 0), (2, 4), (4, 0)])

    def test_collinear_on_edges(self):
        self.assertEqual(convex_hull_jarvis([(0, 3), (2, 3), (2, 2), (1, 1), (2, 1), (3, 0), (3, 1), (0, 0), (3, 3)]), [(0, 0), (0, 3), (2, 3), (3, 3), (3, 0)])

if __name__ == "__main__":
    unittest.main()