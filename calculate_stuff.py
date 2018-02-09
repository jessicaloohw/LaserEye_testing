import numpy as np

def sum_nums(input_list):
    sum = np.sum(input_list)
    return sum
# To calculate the maximum difference between two adjacent numbers
def max_diff(input_list):

    diff = np.diff(input_list)
    abs_diff = np.abs(diff)
    max_val = np.max(abs_diff)

    return max_val
