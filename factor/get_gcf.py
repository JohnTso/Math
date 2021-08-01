from get_factor import get_factor 
def get_gcf(*nums):
    """
    Given a list of numbers, return their Greatest Common Factor(GCF)
    >>> get_gcf([2, 4])
    2
    >>> get_gcf([4, 16, 8])
    4
    """
    m = min(nums)
    gcf = 1
    for i in get_factor(m):
        for n in nums:
            if n % i != 0:
                break
        else:
            gcf = i
    return gcf

