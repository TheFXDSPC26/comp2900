import unittest
import calc

class TestCalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calc.add(10,5), 15)
        self.assertEqual(calc.add(5,5), 10)
        self.assertEqual(calc.add(1,5), 6)

    def test_subtract(self):
        self.assertEqual(calc.subtract(10,5), 5)
        self.assertEqual(calc.subtract(10,8), 2)
        self.assertEqual(calc.subtract(10,12), -2)

    def test_mutliply(self):
        self.assertEqual(calc.mutliply(30,5), 150)
        self.assertEqual(calc.mutliply(3,5), 15)
        self.assertEqual(calc.mutliply(820,53), 43460)

    def test_divide(self):
        self.assertEqual(calc.divide(40,5), 8)
        self.assertEqual(calc.divide(80,40), 2)
        self.assertEqual(calc.divide(5,2), 2.5)

        with self.assertRaises(ValueError):
            calc.divide(10,0)
        
        