"""Division Class"""
from calculator.calculations.calculation import Calculation

class Division(Calculation):
    """division calculation object"""
    def get_result(self):
        """get the division results"""
        value_list = []

        for value in self.values:
            value_list.append(value)
        result = value_list[0]
        for num in range(1, len(value_list)):
            try:
                result /= value_list[num]
            except ZeroDivisionError:
                return "ZeroDivisionError"
            else:
                continue
        return result
