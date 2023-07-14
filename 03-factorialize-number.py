import unittest

"""
Factorialize a Number

Return the factorial of the provided integer.

If the integer is represented with the letter n, a factorial is the product of 
all positive integers less than or equal to n.

Factorials are often represented with the shorthand notation n!

For example: 5! = 1 * 2 * 3 * 4 * 5 = 120

Only integers greater than or equal to zero will be supplied to the function.

"""

def factorialize(num):
    return num

print(factorialize(5))


"""
Do not change anything below:
"""

class TestFactorialize(unittest.TestCase):

    def test_fact(self):
        self.assertIsInstance(factorialize(5), int)

    def test_fact2(self):
        self.assertEqual(factorialize(5), 120)
    
    def test_fact3(self):
        self.assertEqual(factorialize(10), 3628800)

    def test_fact4(self):
        self.assertEqual(factorialize(20), 2432902008176640000)

    def test_fact5(self):
        self.assertEqual(factorialize(0), 1)

if __name__ == "__main__":
    unittest.main()