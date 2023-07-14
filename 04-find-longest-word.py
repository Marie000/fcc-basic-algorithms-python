import unittest

"""
Find the Longest Word in a String

Return the length of the longest word in the provided sentence.

Your response should be a number.

"""

def find_longest_word_length(string):
    return len(string)

print(find_longest_word_length("The quick brown fox jumped over the lazy dog"))



"""
Do not change anything below:
"""

class TestLongestWord(unittest.TestCase):

    def test_longest1(self):
        self.assertIsInstance(find_longest_word_length("The quick brown fox jumped over the lazy dog"), int)

    def test_longest2(self):
        self.assertEqual(find_longest_word_length("The quick brown fox jumped over the lazy dog"), 6)
    
    def test_longest3(self):
        self.assertEqual(find_longest_word_length("May the force be with you"), 5)

    def test_longest4(self):
        self.assertEqual(find_longest_word_length("Google do a barrel roll"), 6)
    
    def test_longest5(self):
        self.assertEqual(find_longest_word_length("What is the average airspeed velocity of an unladen swallow"), 8)
    
    def test_longest6(self):
        self.assertEqual(find_longest_word_length("What if we try a super-long word such as otorhinolaryngology"), 19)    

if __name__ == "__main__":
    unittest.main()


