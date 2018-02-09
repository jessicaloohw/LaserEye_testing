import numpy as np

# To return the maximum difference between two adjacent numbers:
def max_diff(input_list):

    diff = np.diff(input_list)
    abs_diff = np.abs(diff)
    max_val = np.max(abs_diff)

    return max_val
