def test_min_max():

    from min_max import min_max

    min_max_val1 = min_max([1, 2, 3, 4, 5]) # normal list
    min_max_val2 = min_max([-1, -3, -5, 4, 2, 0]) # with negatives, out of order
    min_max_val3 = min_max([-6, -5, -3, -1, 1, 1, 3])

    assert(min_max_val1 == (1,5))
    assert(min_max_val2 == (-5,4))
    assert(min_max_val3 == (-6,3))
