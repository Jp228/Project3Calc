"""Addition Class"""
from calc.calculations.calculation import Calculation

class Addition(Calculation):
    """ calculation addition class"""
    def get_result(self):
        """get the addition results"""
        result = self.values[0]
        for value in self.values[1:]:
            result = value + result
        return result
