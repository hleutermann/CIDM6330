
"""
CIDM6330 Week 1 - Roman Numerals Katan
Part 1
"""

import unittest
import math

numerals = {'I': 1, 'IV': 4, 'V': 5, 'IX': 9, 'X': 10, 'XL': 40, 'L':50, 'XC': 90, 'C': 100, 'CD': 400, 'D':500, 'CM': 900, 'M':1000}
intergers = {"": 0, "M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}

for k,v in numerals.items():
    print(k,v)
    print()

class RomanNumeralConverter(object):
    def converter(self, input):
        range = None

        for roman, number in numerals.items():
            if number == input:
                return roman
            if input > number:
                range = roman

        remainder = input - numerals[range]
        return range + self.converter(remainder)

    def convertback(self, input):
        
        for roman, number in intergers.items():
            if roman == input:
                return number
            
        char1, char2 = map(self.convertback, input[:2])
        if char1 < char2:
            return char2 - char1 + self.convertback(input[2:])
        else:
            return char1 + self.convertback(input[1:])