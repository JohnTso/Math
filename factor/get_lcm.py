def get_lcm(nums):
    """
    Given a list of numbers, return the Least Common Multiple (LCM).
    >>> get_lcm([2, 4])
    4
    >>> get_lcm([4, 16, 8])
    16
    >>> get_lcm([27, 63])
    189
    """
    m = max(nums) # Get the maximum number of nums
    stop = False # This is for stopping while loop
    lcm = m   # Return the the final result
    def check_lcm(nums, lcm):
        for num in nums:
            if lcm % num != 0:   # This check_lcm function is for checking if it's the lcm
                return False
        return True
    while not stop:
        if not check_lcm(nums, lcm):  # This while loop return lcm
            lcm += m
        else:
            stop = True
            return lcm