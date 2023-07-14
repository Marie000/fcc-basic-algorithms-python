import unittest
"""
Return Largest Numbers in Lists

Return a list consisting of the largest number from each provided sub-list. 
For simplicity, the provided list will contain exactly 4 sub-lists.

"""

def largest_of_four(lst):
    return lst

print(largest_of_four([[4, 5, 1, 3], [13, 27, 18, 26], [32, 35, 37, 39], [1000, 1001, 857, 1]]))



"""
Do not change anything below:
"""

class TestLargestNumber(unittest.TestCase):

    def test_largest1(self):
        self.assertIsInstance(largest_of_four([[4, 5, 1, 3], [13, 27, 18, 26], [32, 35, 37, 39], [1000, 1001, 857, 1]]), list)

    def test_largest2(self):
        self.assertListEqual(largest_of_four([[13, 27, 18, 26], [4, 5, 1, 3], [32, 35, 37, 39], [1000, 1001, 857, 1]]), [27, 5, 39, 1001])

    def test_largest3(self):
        self.assertListEqual(largest_of_four([[4, 9, 1, 3], [13, 35, 18, 26], [32, 35, 97, 39], [1000000, 1001, 857, 1]]), [9, 35, 97, 1000000])

    def test_largest4(self):
        self.assertListEqual(largest_of_four([[17, 23, 25, 12], [25, 7, 34, 48], [4, -10, 18, 21], [-72, -3, -17, -10]]), [25, 48, 21, -3])


if __name__ == "__main__":
    unittest.main()




