import unittest
from RomanNumeralConverter import *

class TestRoman(unittest.TestCase):

    def setUp(self):
        self.ConverterTester = RomanNumeralConverter()

    def test_integer1_returns_I(self):
        self.assertEqual(self.ConverterTester.converter(1),"I")

    def test_definedInteger_return(self):
        self.assertEqual(self.ConverterTester.converter(5),"V")

    def test_undefinedInteger_return(self):
        self.assertEqual(self.ConverterTester.converter(44),"XLIV")

    def test_mostcomplexnumeral_return(self):
        self.assertEqual(self.ConverterTester.converter(2999), "MMCMXCIX")

    def test_integer1_back(self):
        self.assertEqual(self.ConverterTester.convertback("I"), 1)

    def test_integer4_back(self):
        self.assertEqual(self.ConverterTester.convertback("IV"), 4)

    def test_integer2999_back(self):
        self.assertEqual(self.ConverterTester.convertback("MMCMXCIX"), 2999)



if __name__=='__main__':

    unittest.main()



