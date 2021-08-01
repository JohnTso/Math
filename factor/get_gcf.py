from get_factor import get_factor

def get_gcf(*nums):
    """
    Given a list of numbers, return their Greatest Common Factor (GCF).
    >>> get_gcf([2, 4])
    2
    >>> get_gcf([4, 16, 8])
    4
    """

    #  Get the minimum number of nums
    m = min(nums)
    gcf = 1

    # Iterate factors of the minimum number
    for i in get_factor(m):
        for n in nums:
            if n % i != 0:
                break
        else:
            gcf = i
    return gcf