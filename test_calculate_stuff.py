def test_max_diff():

    from calculate_stuff import max_diff
    import numpy as np

    max_value1 = max_diff([1, 2, 3, 4, 5])
    max_value2 = max_diff([9.0, 1.5, 3.2])
    max_value3 = max_diff([-5, -7, 5, -2, 12, 15])

    assert(np.isclose(max_value1, 1))
    assert(np.isclose(max_value2, 7.5))
    assert(np.isclose(max_value3, 14))

def test_sum_nums():
    from calculate_stuff import sum_nums
    import numpy as np


    sum_1 = sum_nums([-1, 9.8, 7])
    sum_2 = sum_nums([-10, 0.5, 0.5, 5.5])
    sum_3 = sum_nums([2, 5, 7, 8, 1])

    assert(np.isclose(sum_1, 15.8))
    assert(np.isclose(sum_2, -3.5))
    assert(np.isclose(sum_3, 23))
