"""Testing Division class"""
from calc.calculations.division import Division

def test_calculator_division():
    """testing that our calculator has a static method for addition"""
    #Arrange
    mynumbers = (3.0,3.0)
    division = Division(mynumbers)
    #Act
    #Assert
    assert division.get_result() == 1.0
