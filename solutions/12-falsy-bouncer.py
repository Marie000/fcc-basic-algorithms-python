import unittest

"""
Falsy Bouncer

Remove all falsy values from a list. Return a new list.

"""

def bouncer(lst):
    return [x for x in lst if bool(x)]

print(bouncer([7, "ate", "", False, 9]))


"""
Do not change anything below:
"""

class TestBouncer(unittest.TestCase):

    def test_bouncer1(self):
        self.assertListEqual(bouncer([7, "ate", "", False, 9]), [7, "ate", 9])

    def test_bouncer2(self):
        self.assertListEqual(bouncer(["a", "b", "c"]), ["a", "b", "c"])

    def test_bouncer3(self):
        self.assertListEqual(bouncer([False, None, 0, "", ()]), [])

    def test_bouncer4(self):
        self.assertListEqual(bouncer([None, 1, 2, []]), [1, 2])


if __name__ == "__main__":
    unittest.main()