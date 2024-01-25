from unittest import TestCase, main
from subtraction.subtraction_by_three import subtraction_by_three

class TestMultiplyByThree(TestCase):
    """
    Testing subtraction_by_three function in multiple package
    """
    def test_subtraction_by_three(self):
        self.assertEqual(subtraction_by_three(3), 9)


main()
