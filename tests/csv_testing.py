"""testing Addition class"""
import pandas as pd
import pytest

from calc.calculator import Calculator
#from calc.calculations.calculation import Calculation

def test_csvreader_add():
    """testing with csv file"""
    data = pd.read_csv("./CSV_File/Addition1.csv")
    for row in data.iterrows():
        tuple_values = (row['value_1'], row['value_2'])
        result = Calculator.add_numbers(tuple_values)
        assert result == row['result']

def test_csvreader_addbig():
    """testing with csv file"""
    data = pd.read_csv("./CSV_File/Addition2.csv")
    for row in data.iterrows():
        tuple_values = (row['value_1'], row['value_2'])
        result = Calculator.add_numbers(tuple_values)
        assert result == row['result']

def test_csvreader_sub():
    """testing with csv file"""
    data = pd.read_csv("./CSV_File/Subtraction1.csv")
    for row in data.iterrows():
        tuple_values = (row['value_1'], row['value_2'])
        result = Calculator.subtract_numbers(tuple_values)
        assert result == row['result']

def test_csvreader_subbig():
    """testing with csv file"""
    data = pd.read_csv("./CSV_File/Subtraction2.csv")
    for row in data.iterrows():
        tuple_values = (row['value_1'], row['value_2'])
        result = Calculator.subtract_numbers(tuple_values)
        assert result == row['result']

def test_csvreader_multiply():
    """testing with csv file"""
    data = pd.read_csv("./CSV_File/Multiplication1.csv")
    for row in data.iterrows():
        tuple_values = (row['value_1'], row['value_2'])
        result = Calculator.multiply_numbers(tuple_values)
        assert result == row['result']

def test_csvreader_multiplybig():
    """testing with csv file"""
    data = pd.read_csv("./CSV_File/Multiplication2.csv")
    for row in data.iterrows():
        tuple_values = (row['value_1'], row['value_2'])
        result = Calculator.multiply_numbers(tuple_values)
        assert result == row['result']

def test_csvreader_divide():
    """testing with csv file"""
    data = pd.read_csv("./CSV_File/Division1.csv")
    for row in data.iterrows():
        tuple_values = (row['value_1'], row['value_2'])
        result = Calculator.divide_number(tuple_values)
        try:
            assert result == row['result']
        except ZeroDivisionError:
            with pytest.raises(ZeroDivisionError):
                assert result.get_result() is True

def test_csvreader_dividebig():
    """testing with csv file"""
    data = pd.read_csv("./CSV_File/Division2.csv")
    for row in data.iterrows():
        tuple_values = (row['value_1'], row['value_2'])
        result = Calculator.divide_number(tuple_values)
        try:
            assert result == row['result']
        except ZeroDivisionError:
            with pytest.raises(ZeroDivisionError):
                assert result.get_result() is True
