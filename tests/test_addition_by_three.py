from unittest import TestCase, main
from addition.addition_by_three import addition_by_three

class TestMultiplyByThree(TestCase):
    """
    Testing addition_by_three function in multiple package
    """
    def test_addition_by_three(self):
        self.assertEqual(addition_by_three(3), 9)


main()
