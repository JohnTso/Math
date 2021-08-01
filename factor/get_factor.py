def get_factor(num):
    """
    Get a list of factors of a number.
    >>> get_factor(2)
    [1, 2]
    >>> get_factor(12)
    [1, 2, 3, 4, 6, 12]
    """

    factors = []
    for i in range(1, num+1):
        if not num % i:
            factors.append(i)

    return factors