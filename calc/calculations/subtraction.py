"""Subtraction Class"""

from calc.calculations.calculation import Calculation

class Subtraction(Calculation):
    """subtraction calculation object"""
    def get_result(self):
        """get the subtraction results"""
        result = self.values[0]
        for value in self.values[1:]:
            result =   result - value

        return result
