
import unittest

"""
The formula to convert from Celsius to Fahrenheit is the temperature in Celsius
times 9/5, plus 32.

You are given a variable celsius representing a temperature in Celsius. Use 
the variable fahrenheit already defined and assign it the Fahrenheit temperature 
equivalent to the given Celsius temperature. Use the formula mentioned above 
to help convert the Celsius temperature to Fahrenheit.

"""

def convert_C_to_F(celsius):
    fahrenheit = celsius * (9/5) + 32
    return fahrenheit

print(convert_C_to_F(30))


"""
DO NOT CHANGE ANYTHING BELOW THIS
"""

class TestCtoF(unittest.TestCase):

    def test_convert(self):
        self.assertIsInstance(convert_C_to_F(0), float)

    def test_convert2(self):
        self.assertEqual(convert_C_to_F(-30), -22)
    
    def test_convert3(self):
        self.assertEqual(convert_C_to_F(-10), 14)

    def test_convert4(self):
        self.assertEqual(convert_C_to_F(0), 32)

    def test_convert5(self):
        self.assertEqual(convert_C_to_F(20), 68)

    def test_convert6(self):
        self.assertEqual(convert_C_to_F(30), 86)


if __name__ == "__main__":
    unittest.main()
