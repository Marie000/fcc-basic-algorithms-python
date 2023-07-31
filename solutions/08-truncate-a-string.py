import unittest

"""
Truncate a string

Truncate a string (first argument) if it is longer than the given maximum string 
length (second argument). Return the truncated string with a ... ending.
"""

def truncate_string(string, num):
    if (num >= len(string)):
        return string
    return string[:num] + '...'

print(truncate_string("A-tisket a-tasket A green and yellow basket", 8))

"""
Do not change anything below:
"""

class TestTruncateString(unittest.TestCase):

    def test_truncate1(self):
        self.assertEqual(truncate_string("A-tisket a-tasket A green and yellow basket", 8), "A-tisket...")

    def test_truncate2(self):
        self.assertEqual(truncate_string("Peter Piper picked a peck of pickled peppers", 11), "Peter Piper...")

    def test_truncate3(self):
        self.assertEqual(truncate_string("A-tisket a-tasket A green and yellow basket", len("A-tisket a-tasket A green and yellow basket")), "A-tisket a-tasket A green and yellow basket")

    def test_truncate4(self):
        self.assertEqual(truncate_string("A-tisket a-tasket A green and yellow basket", len("A-tisket a-tasket A green and yellow basket") + 2), "A-tisket a-tasket A green and yellow basket")

    def test_truncate5(self):
        self.assertEqual(truncate_string("A-", 1), "A...")

    def test_truncate6(self):
        self.assertEqual(truncate_string("Absolutely Longer", 2), "Ab...")


if __name__ == "__main__":
    unittest.main()


