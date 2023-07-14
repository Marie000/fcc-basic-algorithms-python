import unittest

"""
Where do I Belong

Return the lowest index at which a value (second argument) should be inserted into 
a list (first argument) once it has been sorted. The returned value should be a 
number.

For example, getIndexToIns([1,2,3,4], 1.5) should return 1 because it is greater 
than 1 (index 0), but less than 2 (index 1).

Likewise, getIndexToIns([20,3,5], 19) should return 2 because once the list has 
been sorted it will look like [3,5,20] and 19 is less than 20 (index 2) and greater 
than 5 (index 1).

"""

def get_index_to_ins(lst, n):
    return n

print(get_index_to_ins([40, 60], 50))

"""
Do not change anything below:
"""

class TestInsert(unittest.TestCase):

    def test_insert1(self):
        self.assertEqual(get_index_to_ins([10, 20, 30, 40, 50], 35), 3)

    def test_insert2(self):
        self.assertIsInstance(get_index_to_ins([10, 20, 30, 40, 50], 35), int)

    def test_insert3(self):
        self.assertEqual(get_index_to_ins([10, 20, 30, 40, 50], 30), 2)

    def test_insert4(self):
        self.assertEqual(get_index_to_ins([40, 60], 50), 1)

    def test_insert5(self):
        self.assertEqual(get_index_to_ins([3, 10, 5], 3), 0)

    def test_insert6(self):
        self.assertEqual(get_index_to_ins([5, 3, 20, 3], 5), 2)

    def test_insert7(self):
        self.assertEqual(get_index_to_ins([2, 20, 10], 19), 2)

    def test_insert8(self):
        self.assertEqual(get_index_to_ins([2, 5, 10], 15), 3)

    def test_insert9(self):
        self.assertEqual(get_index_to_ins([], 1), 0)

if __name__ == "__main__":
    unittest.main()
