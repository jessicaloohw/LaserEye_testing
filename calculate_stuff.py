def max_diff(input_list):
    """Returns the maximum absolute difference between two adjacent numbers

    :param input_list: a list of numbers
    :returns max_val: maximum absolute difference between two adjacent numbers
    :raises ImportError: if required modules are not found
    :raises TypeError: if input_list contains anything other than numbers
    :raises ValueError: if maximum difference is NaN
    """

    try:

        import numpy as np
        import logging as lg

        lg.basicConfig(filename='max_diff.log',
                       level=lg.DEBUG,
                       format='%(asctime)s %(message)s',
                       datefmt='%m/%d/%Y %I:%M:%S %p')
        
        if not (type(input_list) is list):
            raise TypeError

        diff = np.diff(input_list)
        abs_diff = np.abs(diff)
        max_val = np.max(abs_diff)
        if(np.isnan(max_val)):
            raise ValueError
        
        lg.info(' | SUCCESS: input_list %s returned %g' % (input_list, max_val))
        return max_val

    except ImportError as e:
        print('ImportError: %s module not found.' % e.name)
        lg.debug(' | ABORTED: ImportError: %s' % e.name)
    except TypeError:
        print('TypeError: This function accepts a list of integers or floats only.')
        lg.debug(' | ABORTED: TypeError: input_list is %s (%s)' % (input_list, type(input_list)))
    except ValueError:
        if(len(input_list)==1):
            print('ValueError: input_list must have at least two values.')
            lg.debug(' | ABORTED: ValueError: input_list is %s' % input_list)
        else:
            print('ValueError: max_val is %g' % max_val)
            lg.debug(' | ABORTED: ValueError: max_val is %g' % max_val)
    except:
        print('An unknown error occurred.')
        lg.warning(' | WARNING: OMG AN UNKNOWN ERROR OCCURRED!')
