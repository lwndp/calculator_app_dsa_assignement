import math
import pytest
from classes import Circle

def test_calculate_area():
    # Test with different radiuses
    assert Circle(1).calculate_area() == pytest.approx(math.pi)
    assert Circle(2).calculate_area() == pytest.approx(4 * math.pi)
    assert Circle(5).calculate_area() == pytest.approx(25 * math.pi)
    
    # Test with zero (edge case)
    assert Circle(0).calculate_area() == 0
    
    # Test with negative value - should raise ValueError
    with pytest.raises(ValueError):
        Circle(-3).calculate_area()

def test_calculate_circumference():
    # Test with different radiuses
    assert Circle(1).calculate_perimeter() == pytest.approx(2 * math.pi)
    assert Circle(2).calculate_perimeter() == pytest.approx(4 * math.pi)
    assert Circle(7).calculate_perimeter() == pytest.approx(14 * math.pi)
    
    # Test with zero (edge case)
    assert Circle(0).calculate_perimeter() == 0
    
    # Test with negative value - should raise ValueError
    with pytest.raises(ValueError):
        Circle(-4).calculate_perimeter()