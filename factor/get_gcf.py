from get_factor import get_factor

# gcf stands for get common factor or greatest common factor
def get_gcf(nums, show_all=False):
    """
    Given a list of numbers, return their greatest common factor or get common factor (GCF).
    >>> get_gcf([2, 4])
    2
    >>> get_gcf([4, 16, 8])
    4
    >>> get_gcf([4, 16, 8], show_all=True)
    [1, 2, 4]
    >>> get_gcf([12, 24], True)
    [1, 2, 3, 4, 6, 12]
    """

    #  Get the minimum number of nums
    m = min(nums)
    gcf = []

    # Iterate factors of the minimum number
    for i in get_factor(m):
        for n in nums:
            if n % i != 0:
                break
        else:
            gcf.append(i)

    # if show_all is True, return a list of common factors, else the greatest common factor
    return gcf if show_all else gcf[-1]