import unittest

"""
Slice and Splice

You are given two lists and an index.

Copy each element of the first list into the second list, in order.

Begin inserting elements at index n of the second list.

Return the resulting list. 

"""

def franken_splice(list1, list2, n):
    list2[n:n] = list1
    return list2

print(franken_splice([1, 2, 3], [4, 5, 6], 1))

"""
Do not change anything below:
"""

class TestFrankenSplice(unittest.TestCase):

    def test_splice1(self):
        self.assertListEqual(franken_splice([1, 2, 3], [4, 5], 1), [4, 1, 2, 3, 5])

    def test_splice2(self):
        self.assertListEqual(franken_splice([1, 2], ["a", "b"], 1), ["a", 1, 2, "b"])

    def test_splice3(self):
        self.assertListEqual(franken_splice(["claw", "tentacle"], ["head", "shoulders", "knees", "toes"], 2), ["head", "shoulders", "claw", "tentacle", "knees", "toes"])

    def test_splice4(self):
        self.assertListEqual(franken_splice([1, 2, 3, 4], [], 0), [1, 2, 3, 4])

if __name__ == "__main__":
    unittest.main()
