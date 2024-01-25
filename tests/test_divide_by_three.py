import unittest
from divide.divide_by_three import divide_by_three


class TestDivideByThree(unittest.TestCase):
    """
    Testing divide_by_three function in divide package
    """
    def test_divide_by_three(self):
        self.assertEqual(divide_by_three(12), 4)


unittest.main()
