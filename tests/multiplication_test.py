"""Testing Multiplication class"""
from calc.calculations.multiplication import Multiplication


def test_calculator_multiply():
    """testing that our calculator has a static method for addition"""
    #Arrange
    mynumbers = (1.0,2.0,3.0)
    multiplication = Multiplication(mynumbers)
    #Act
    #Assert
    assert multiplication.get_result() == 6.0
