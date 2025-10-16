'''
problem 01:
Write a unittest class that checks:
1. 10 is found in the list [5, 7, 8, 10]
2. The type of 10 is int
3. Number 100 returns True
4. Empty list [] returns False
5. 100 is larger than or equal to 90
'''

import unittest

class TestListMethods(unittest.TestCase):

    def setUp(self):
        self.numbers = [5, 7, 8, 10]

    def test_1(self):
        self.assertIn(10, self.numbers, "10 should be in the list")

    def test_2(self):
        self.assertIsInstance(10, int, "10 should be of type int")

    def test_3(self):
        self.assertTrue(100, "100 should evaluate to True")

    def test_4(self):
        self.assertFalse([], "Empty list should evaluate to False")

    def test_5(self):
        self.assertGreaterEqual(100, 90, "100 should be >= 90")


if __name__ == '__main__':
    unittest.main()
#----------------------------------------- Task 01 Done ----------------------------------------
#-----------------------------------------------------------------------------------------------
