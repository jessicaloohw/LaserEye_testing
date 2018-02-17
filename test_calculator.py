from calculator import Calculator
import numpy as np
import pytest


def test_calculator():

    calc1 = Calculator(input_list=[1, 2, 3, 4, 5],
                       filename_log='test_calculator.log')
    calc1.calculate_sum()
    calc1.calculate_min_max()
    calc1.calculate_max_diff()
    assert(np.isclose(calc1.sum, 15))
    assert(calc1.min_max == (1, 5))
    assert(np.isclose(calc1.max_diff, 1))

    calc2 = Calculator(input_list=[-6.2, -5, -3, -1.45],
                       filename_log='test_calculator.log')
    calc2.calculate_sum()
    calc2.calculate_min_max()
    calc2.calculate_max_diff()
    assert(np.isclose(calc2.sum, -15.65))
    assert(calc2.min_max == (-6.2, -1.45))
    assert(np.isclose(calc2.max_diff, 2))

    calc3 = Calculator(input_list=[2, 5, -7.5],
                       filename_log='test_calculator.log')
    calc3.calculate_sum()
    calc3.calculate_min_max()
    calc3.calculate_max_diff()
    assert(np.isclose(calc3.sum, -0.5))
    assert(calc3.min_max == (-7.5, 5))
    assert(np.isclose(calc3.max_diff, 12.5))

    calc4 = Calculator(input_list=['a', 'b', 'c'],
                       filename_log='test_calculator.log')
    with pytest.raises(TypeError):
        calc4.calculate_sum()
    with pytest.raises(TypeError):
        calc4.calculate_min_max()
    with pytest.raises(TypeError):
        calc4.calculate_max_diff()

    calc5 = Calculator(input_list=[7, 3, float('nan')],
                       filename_log='test_calculator.log')
    with pytest.raises(ValueError):
        calc5.calculate_sum()
    with pytest.raises(ValueError):
        calc5.calculate_min_max()
    with pytest.raises(ValueError):
        calc5.calculate_max_diff()

    calc6 = Calculator(input_list=[7],
                       filename_log='test_calculator.log')
    calc6.calculate_sum()
    calc6.calculate_min_max()
    assert(np.isclose(calc6.sum, 7))
    assert(calc6.min_max == (7, 7))
    with pytest.raises(ValueError):
        calc6.calculate_max_diff()

    calc7 = Calculator(input_list=[],
                       filename_log='test_calculator.log')
    with pytest.raises(ValueError):
        calc7.calculate_sum()
    with pytest.raises(ValueError):
        calc7.calculate_min_max()
    with pytest.raises(ValueError):
        calc7.calculate_max_diff()
