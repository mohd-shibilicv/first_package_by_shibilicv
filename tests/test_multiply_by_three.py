from unittest import TestCase, main
from multiply.multiply_by_three import multiply_by_three

class TestMultiplyByThree(TestCase):
    """
    Testing multiply_by_three function in multiple package
    """
    def test_multiply_by_three(self):
        self.assertEqual(multiply_by_three(3), 9)


main()
