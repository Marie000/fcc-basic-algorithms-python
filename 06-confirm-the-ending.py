import unittest

"""
Confirm the Ending

Check if a string (first argument, str) ends with the given target string 
(second argument, target).

This challenge can be solved using .endswith(). But for the purpose of this 
challenge, we would like you to use string indexing instead.
"""

def confirm_ending(string, target):
    return string

print(confirm_ending("Bastian", "n"))



"""
Do not change anything below:
"""

class TestStringEnding(unittest.TestCase):

    def test_ending1(self):
        self.assertEqual(confirm_ending("Bastian", "n"), True)

    def test_ending2(self):
        self.assertEqual(confirm_ending("Congratulation", "on"), True)

    def test_ending3(self):
        self.assertEqual(confirm_ending("Connor", "n"), False)

    def test_ending4(self):
        self.assertEqual(confirm_ending("Walking on water and developing software from a specification are easy if both are frozen", "specification"), False)
 
    def test_ending5(self):
        self.assertEqual(confirm_ending("He has to give me a new name", "name"), True)

    def test_ending6(self):
        self.assertEqual(confirm_ending("Open sesame", "same"), True)

    def test_ending7(self):
        self.assertEqual(confirm_ending("Open sesame", "sage"), False)

    def test_ending8(self):
        self.assertEqual(confirm_ending("Open sesame", "game"), False)

    def test_ending9(self):
        self.assertEqual(confirm_ending("If you want to save our world, you must hurry. We dont know how much longer we can withstand the nothing", "mountain"), False)
    
    def test_ending10(self):
        self.assertEqual(confirm_ending("Abstraction", "action"), True)
        
if __name__ == "__main__":
    unittest.main()

