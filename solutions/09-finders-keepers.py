import unittest

"""
Finders Keepers

Create a function that looks through a list lst and returns the first element in
 it that passes a 'truth test'. This means that given an element x, the 'truth test' 
 is passed if func(x) is true. If no element passes the test, return None.

"""

def find_element(lst, func):
    num = None
    for item in lst:
        if func(item) == True:
            num = item
            break
    return num

print(find_element([1, 2, 3, 4], lambda x: x %2 == 0))

"""
Do not change anything below:
"""

class TestFindersKeepers(unittest.TestCase):

    def test_finders1(self):
        self.assertEqual(find_element([1, 3, 5, 8, 9, 10], lambda x: x %2 == 0), 8)

    def test_finders2(self):
        self.assertEqual(find_element([1, 3, 5, 9,], lambda x: x %2 == 0), None)

if __name__ == "__main__":
    unittest.main()


