from get_gcf import get_gcf

def simplify_fraction(fraction):
    """
    Given a fraction, return the simplified fraction
    >>> simplify_fraction('10/100') 
    '1/10'
    >>> simplify_fraction('2/4')
    '1/2'
    >>> simplify_fraction('155000/1000000')
    '31/200'
    """
    # this turn the fraction(input) into a list[numerator, denominator]
    nums = fraction.replace('/', ' ').split()
    nums = [int(i) for i in nums] 
    
    # this will divide both numerator and denominator by their gcf value
    gcf = get_gcf(nums)
    nums = [str(i // gcf) for i in nums]    

    return "/".join(nums)