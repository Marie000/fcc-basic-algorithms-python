import unittest

"""

Title Case a Sentence

Return the provided string with the first letter of each word capitalized. 
Make sure the rest of the word is in lower case.

For the purpose of this exercise, you should also capitalize connecting words like 
the and of. Do not use the built-in title method.

"""

def title_case(string):
    words = string.split()
    new_words = []
    for word in words:
        new_words.append(word[0].upper() + word[1:].lower())
    return " ".join(new_words)

print(title_case("I'm a little tea pot"))

"""
Do not change anything below:
"""

class TestTitleCase(unittest.TestCase):

    def test_title1(self):
        self.assertIsInstance(title_case("I'm a little tea pot"), str)

    def test_title2(self):
        self.assertEqual(title_case("I'm a little tea pot"), "I'm A Little Tea Pot")

    def test_title3(self):
        self.assertEqual(title_case("sHoRt AnD sToUt"), "Short And Stout")

    def test_title4(self):
        self.assertEqual(title_case("HERE IS MY HANDLE HERE IS MY SPOUT"), "Here Is My Handle Here Is My Spout")


if __name__ == "__main__":
    unittest.main()