import unittest

"""
Mutations

Return True if the string in the first element of the list contains all of the 
letters of the string in the second element of the list.

For example, ["hello", "Hello"], should return True because all of the letters in 
the second string are present in the first, ignoring case.

The arguments ["hello", "hey"] should return False because the string hello does 
not contain a y.

Lastly, ["Alien", "line"], should return True because all of the letters in line 
are present in Alien.

"""

def mutation(lst):
    return lst

print(mutation(["hello", "hey"]))


"""
Do not change anything below:
"""

class TestInsert(unittest.TestCase):

    def test_mutation1(self):
        self.assertEqual(mutation(["hello", "hey"]), False)

    def test_mutation2(self):
        self.assertEqual(mutation(["hello", "Hello"]), True)

    def test_mutation3(self):
        self.assertEqual(mutation(["zyxwvutsrqponmlkjihgfedcba", "qrstu"]), True)

    def test_mutation4(self):
        self.assertEqual(mutation(["Mary", "Army"]), True)

    def test_mutation5(self):
        self.assertEqual(mutation(["Mary", "Aarmy"]), True)

    def test_mutation6(self):
        self.assertEqual(mutation(["Alien", "line"]), True)

    def test_mutation7(self):
        self.assertEqual(mutation(["floor", "for"]), True)

    def test_mutation8(self):
        self.assertEqual(mutation(["Hello", "neo"]), False)

    def test_mutation9(self):
        self.assertEqual(mutation(["voodoo", "no"]), False)

    def test_mutation10(self):
        self.assertEqual(mutation(["ate", "date"]), False)

    def test_mutation11(self):
        self.assertEqual(mutation(["Tiger", "Zebra"]), False)

    def test_mutation12(self):
        self.assertEqual(mutation(["Noel", "Ole"]), True)


if __name__ == "__main__":
    unittest.main()
