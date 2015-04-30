import operations
import unittest
import random

class TestOperations(unittest.TestCase):

    def setUp(self):
        pass


    def test_add(self):
        self.assertEqual( operations.add_two_numbers(2, 3), 5 )
        self.assertEqual( operations.add_two_numbers(5, 6), 11)
        self.assertEqual( operations.add_two_numbers(5, 0), 5)


    def test_sub(self):
        self.assertEqual( operations.subtract_two_numbers(2, 3), -1 )
        self.assertEqual( operations.subtract_two_numbers(5, 6), -1)
        self.assertEqual( operations.subtract_two_numbers(5, 0), 5)

if __name__ == '__main__':
    unittest.main()

