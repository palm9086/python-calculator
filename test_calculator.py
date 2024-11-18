import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)
    def test_add_negative(self):
        self.assertEqual(self.calc.add(-1,-2),-3)
    def test_subtract_negative(self):
        self.assertEqual(self.calc.subtract(2,-1),3)
    def test_subtract(self):
        self.assertEqual(self.calc.subtract(2,1),1)
    def test_multiply_0(self):
        self.assertEqual(self.calc.multiply(5,0),0)
    def test_multiply_both_negative(self):
        self.assertEqual(self.calc.multiply(-1,-1),1)
    def test_multiply(self):
        self.assertEqual(self.calc.multiply(4,2),8)
    def test_multiply_negative(self):
        self.assertEqual(self.calc.multiply(-1,5),-5)
    def test_divide_0(self):
        self.assertEqual(self.calc.divide(1,0),"Error")
    def test_divide(self):
        self.assertEqual(self.calc.divide(6,2),3)
    def test_divide_one_negative(self):
        self.assertEqual(self.calc.divide(-4,2),-2)
    def test_divide_both_negative(self):
        self.assertEqual(self.calc.divide(-8,-4),2)
    def test_modulo_0(self):
        self.assertEqual(self.calc.modulo(5,0),"Error")
    def test_modulo_dividend_negative(self):
        self.assertEqual(self.calc.modulo(-10,3),2)
    def test_modulo_modulus_negative(self):
        self.assertEqual(self.calc.modulo(10,-3),-2)
    def test_modulo_both_negative(self):
        self.assertEqual(self.calc.modulo(-10,-3),-1)
    def test_modulo(self):
        self.assertEqual(self.calc.modulo(10,3),1)
    # Add the following test methods to the TestCalculator class:

if __name__ == '__main__':
    unittest.main()