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

'''
problem 02:
create_serial_number(count) that generates a random serial number.

Requirements:
The serial number should include lowercase English letters (a–z) and digits (0–9).
The function should accept one argument count, which determines how many characters (letters or digits) are included.
After every 4 characters, a hyphen (-) should be added — except at the end of the serial number.
The function should print the final serial number as a single string.
'''

import string
import random

def create_serial_number(count):
    serial_number = []
    all_char = list(string.ascii_lowercase + string.digits)
    
    for i in range(count):
        serial_number.append(random.choice(all_char))
        if (i + 1) % 4 == 0 and i != count - 1:
            serial_number.append('-')

    print(''.join(serial_number))

create_serial_number(12)
