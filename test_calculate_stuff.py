import numpy as np
import pytest


def test_max_diff():

    from calculate_stuff import max_diff
    import numpy as np
    import pytest

    max_value1 = max_diff([1, 2, 3, 4, 5])
    max_value2 = max_diff([9.0, 1.5, 3.2])
    max_value3 = max_diff([-5, -7, 5, -2, 12, 15])

    assert(np.isclose(max_value1, 1))
    assert(np.isclose(max_value2, 7.5))
    assert(np.isclose(max_value3, 14))

    with pytest.raises(TypeError):
        max_diff(['a', 'b', 'c'])

    with pytest.raises(ValueError):
        max_diff([7])

    with pytest.raises(ValueError):
        max_diff([4, 5, float('nan')])


def test_min_max():

    from calculate_stuff import min_max

    min_max_val1 = min_max([1, 2, 3, 4, 5])
    min_max_val2 = min_max([-1, -3, -5, 4, 2, 0])
    min_max_val3 = min_max([-6.2, -5, -3, -1, 1.4, 1.4, 3])

    assert(min_max_val1 == (1, 5))
    assert(min_max_val2 == (-5, 4))
    assert(min_max_val3 == (-6.2, 3))

    with pytest.raises(ImportError):
        import Number

    with pytest.raises(TypeError):
        min_max([1, 'b', 'c'])

    with pytest.raises(ValueError):
        min_max([])



def test_sum_nums():
    from calculate_stuff import sum_nums

    sum_1 = sum_nums([-1, 9.8, 7])
    sum_2 = sum_nums([-10, 0.5, 0.5, 5.5])
    sum_3 = sum_nums([2, 5, 7, 8, 1])

    assert(np.isclose(sum_1, 15.8))
    assert(np.isclose(sum_2, -3.5))
    assert(np.isclose(sum_3, 23))
