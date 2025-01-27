#
# The first version of our function!
# Write doc strings 
#
def find_peaks(list_of_intensities):
    """Find peaks

    Find local maxima for a given list of intensities or tuples
    Intensities are defined as local maxima if the
    intensities of the elements in the list before and after
    are smaller than the peak we want to determine.

    For example given a list:
        [1, 5, 6, 4, 1, 2, 3, 2]

    We expect 6 and 3 to be returned.
    

    Args:
        list_of_intensities (list of floats, ints or tuple of ints): a list of
            numeric values

    Returns:
        list of floats or tuples: list of the identified local maxima

    Note:
        This is just a place holder for the TDD part :)

    """
    peaks = []
    

    for num, value in enumerate(list_of_intensities):
        if num == 0 or num == len(list_of_intensities)-1:
            continue
        pre_value = list_of_intensities[num -1]
        post_value = list_of_intensities[num + 1]
        if type(list_of_intensities[num]) == tuple:
            pre_value = sum(list_of_intensities[num -1])
            post_value = sum(list_of_intensities[num + 1])
            value_sum = sum(list_of_intensities[num])
            if pre_value < value_sum > post_value:
             peaks.append(value)
        else:
         if pre_value < value > post_value:
             peaks.append(value)


    return peaks
