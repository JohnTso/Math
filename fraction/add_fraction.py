import sys
sys.path.insert(0, '/Users/petertso/Code/Math/factor')
from get_lcm import get_lcm
from simplify_fraction import simplify_fraction

def add_fraction(*fractions):
    """
    >>> add_fraction('1/2','2/4')
    1/1
    >>> add_fraction('3/2','1/4','1/0')
    divided by zero error
    """

    # this sorts out the numerators and denominators
    fractions = list(fractions)
    nums = [i.replace('/', ' ').split() for i in fractions]
    numerators = [int(i[0]) for i in nums]
    denominators = [int(i[1]) for i in nums]

    # return error when divided by zero
    if 0 in denominators:
        return "divided by zero error"
    
    # get lcm of the denominators, add them up
    lcm = get_lcm(denominators)

    result_deno = 0
    result_num = 0
    for i in range(len(denominators)):
        num = lcm // denominators[i]
        result_deno = denominators[i] * num
        result_num += numerators[i] * num

    # return the simplified fraction
    return simplify_fraction(f"{result_num}/{result_deno}")