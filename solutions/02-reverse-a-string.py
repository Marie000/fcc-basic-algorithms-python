import unittest
"""

Reverse the provided string and return the reversed string.

For example, "hello" should become "olleh".

"""

def reverse_string(str):
    result = ''
    for letter in reversed(str):
        result += letter
    return result

print(reverse_string("hello"))

"""
Do not change anything below:
"""

class TestReverseString(unittest.TestCase):

    def test_reverse(self):
        self.assertIsInstance(reverse_string("hello"), str)

    def test_reverse2(self):
        self.assertEqual(reverse_string("hello"), "olleh")
    
    def test_reverse3(self):
        self.assertEqual(reverse_string("Howdy"), "ydwoH")

    def test_reverse4(self):
        self.assertEqual(reverse_string("Greetings from Earth"), "htraE morf sgniteerG")


if __name__ == "__main__":
    unittest.main()
