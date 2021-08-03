def is_prime(num):
    """
    Give a number, determine if it's a prime number
    >>> is_prime(7)
    True
    >>> is_prime(4)
    False
    """
    # If it's a prime number, the list would be none, which return True 
    factors = [i for i in range(2, num) if not num % i]
    
    return not factors                  