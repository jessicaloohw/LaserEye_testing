from calculator import Calculator
import numpy as np
import pytest


def test_calculator():

    calc1 = Calculator(input_list=[1, 2, 3, 4, 5],
                       filename_log='test_calculator.log')
    sum1 = calc1.calculate_sum()
    min_max1 = calc1.calculate_min_max()
    max_diff1 = calc1.calculate_max_diff()
    assert(np.isclose(sum1, 15))
    assert(min_max1 == (1, 5))
    assert(np.isclose(max_diff1, 1))

    calc2 = Calculator(input_list=[-6.2, -5, -3, -1.45],
                       filename_log='test_calculator.log')
    sum2 = calc2.calculate_sum()
    min_max2 = calc2.calculate_min_max()
    max_diff2 = calc2.calculate_max_diff()
    assert(np.isclose(sum2, -15.65))
    assert(min_max2 == (-6.2, -1.45))
    assert(np.isclose(max_diff2, 2))

    calc3 = Calculator(input_list=[2, 5, -7.5],
                       filename_log='test_calculator.log')
    sum3 = calc3.calculate_sum()
    min_max3 = calc3.calculate_min_max()
    max_diff3 = calc3.calculate_max_diff()
    assert(np.isclose(sum3, -0.5))
    assert(min_max3 == (-7.5, 5))
    assert(np.isclose(max_diff3, 12.5))

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
    sum6 = calc6.calculate_sum()
    min_max6 = calc6.calculate_min_max()
    assert(np.isclose(sum6, 7))
    assert(min_max6 == (7, 7))
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
