import numpy as np


# To calculate the sum of list of numbers
def sum_nums(input_list):

    ans = np.sum(input_list)

    return ans


# To calculate the maximum difference between two adjacent numbers
def max_diff(input_list):

    diff = np.diff(input_list)
    abs_diff = np.abs(diff)
    max_val = np.max(abs_diff)

    return max_val
