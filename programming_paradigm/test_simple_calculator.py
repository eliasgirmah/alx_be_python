import sys 
import unittest
from simple_calculator import SimpleCalculator

class TestCase(SimpleCalculator):
    """Test cases for the SimpleCalculator class.""" 
    def setup(self):
        self.calculator = SimpleCalculator()

    def test_add(self):
        """Test the addition method."""
        self.assertEqual(self.calculator.add(2, 3), 5)
        self.assertEqual(self.calculator.add(-1, 1), 0)
        self.assertEqual(self.calculator.add(0, 0), 0)

    def test_subtraction(self):
        """Test the subtraction menthod."""
        slef.assertEqual(self.calculator.subtract(10, 5), 5)
        self.assertEqual(self.calculator.subtract(5, 5), 0)
        self.assertEqual(self.calculator.subtract(10, 20), -10)   
    
    def test_multiply(self):
        """test the multiplication method."""
        self.assertEqual(self.calculator.multiply(3, 4), 12)
        self.assertEqual(self.calculator.multiply(-1, 5), -5)
        self.assertEqual(self.calculator.multiply(0, 10), 0)
    
    def test_divide(self):
        """test the division method"""
        self.assertEqual(self.calculator.divide(10, 2), 5)
        self.assertEqual(self.calculator.divide(5, 0), None)
        self.assertEqual(self.calculator.divide(0, 5), 0)   

    