import unittest
"""
Repeat a String Repeat a String

Repeat a given string string (first argument) for num times (second argument).
Return an empty string if num is not a positive number. 

"""

def repeat_string_num_times(string, num):
    return string * num


print(repeat_string_num_times("abc", 3))

"""
Do not change anything below:
"""

class TestRepeatString(unittest.TestCase):

    def test_repeat1(self):
        self.assertEqual(repeat_string_num_times("*", 3), "***")

    def test_repeat2(self):
        self.assertEqual(repeat_string_num_times("abc", 3), "abcabcabc")

    def test_repeat3(self):
        self.assertEqual(repeat_string_num_times("abc", 4), "abcabcabcabc") 

    def test_repeat4(self):
        self.assertEqual(repeat_string_num_times("abc", 1), "abc")

    def test_repeat5(self):
        self.assertEqual(repeat_string_num_times("*", 8), "********")

    def test_repeat6(self):
        self.assertEqual(repeat_string_num_times("abc", -2), "")

    def test_repeat7(self):
        self.assertEqual(repeat_string_num_times("abc", 0), "")

if __name__ == "__main__":
    unittest.main()


