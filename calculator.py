import numpy as np
import logging as lg


class Calculator:

    def __init__(self, input_list=[1, 2], filename_log='calculator.log'):
        """ Initializer

        :param input_list: a list of numbers (default=[1, 2])
        :param filename_log: file log (default='calculator.log')
        """

        self.input_list = input_list
        self.filename_log = filename_log
        self.sum = None
        self.min = None
        self.max = None
        self.max_diff = None

        lg.basicConfig(filename=self.filename_log,
                       level=lg.DEBUG,
                       format='%(asctime)s %(message)s',
                       datefmt='%m/%d/%Y %I:%M:%S %p')

    def calculate_sum(self):
        """ Calculates the sum of numbers in the list

        :param input_list: a list of numbers
        :returns sum_val: the sum of numbers
        :raises TypeError: input_list is not a list of integers/floats
        :raises ValueError: input_list is empty
                            or sum_val is NaN
        """

        try:
            input_list = self.input_list
            if(input_list == []):
                raise ValueError

            sum_val = np.sum(input_list)
            if np.isnan(sum_val):
                raise ValueError
            self.sum = sum_val

            return sum_val

        except TypeError:
            raise TypeError('input_list must be a list of integers/floats.'
                            '\ninput_list is %s (%s)'
                            % (input_list, type(input_list)))
        except ValueError:
            raise ValueError('The sum is NaN.')
        except:
            print('An unknown error occurred.')
            lg.warning(' | WARNING::calculate_sum::UNKNOWN EXCEPTION')
            raise

    def calculate_min_max(self):
        """ Calculates the minimum and maximum value in the list

        :param input_list: a list of numbers
        :returns min_max: a tuple of the minimum and maximum values
        :raises TypeError: input_list is not a list of integers/floats
        :raises ValueError: input_list is empty
                            or min_max_val is NaN
        """

        try:
            input_list = self.input_list
            min_max_val = (np.min(input_list), np.max(input_list))
            if not (isinstance(min_max_val, tuple)):
                raise ValueError
            if(np.isnan(min_max_val[0]) or np.isnan(min_max_val[1])):
                raise ValueError
            self.min = min_max_val[0]
            self.max = min_max_val[1]

            return min_max_val

        except TypeError:
            raise TypeError('input_list must be a list of integers/floats.')
        except ValueError:
            raise ValueError('min_max_val is NaN.')
        except:
            print('An unknown error occurred.')
            lg.warning(' | WARNING::calculate_min_max::UNKNOWN EXCEPTION')
            raise

    def calculate_max_diff(self):
        """ Calculates the maximum absolute difference between two adjacent numbers
            in the list

        :param input_list: a list of numbers
        :returns max_diff_val: the maximum absolute difference
        :raises TypeError: input_list is not a list of integers/floats
        :raises ValueError: input_list contains less than two values
                            or max_diff_val is NaN
        """

        try:
            input_list = self.input_list
            diff = np.diff(input_list)
            abs_diff = np.abs(diff)
            max_diff_val = np.max(abs_diff)
            if(np.isnan(max_diff_val)):
                raise ValueError
            self.max_diff = max_diff_val

            return max_diff_val

        except TypeError:
            raise TypeError('input_list must be a list of integers/floats.')
        except ValueError:
            raise ValueError('Not enough values or max_diff_val is NaN.')
        except:
            print('An unknown error occurred.')
            lg.warning(' | WARNING::calculate_max_diff::UNKNOWN EXCEPTION')
            raise
