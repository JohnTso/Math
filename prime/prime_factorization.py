from is_prime import is_prime

def prime_factorization(num):
    """
    return prime factorization to the given number
    >>> prime_factorization(1)
    ('', {})
    >>> prime_factorization(24)
    ('2^3 x 3^1', {2: 3, 3: 1})
    >>> prime_factorization(1234567)
    ('127^1 x 9721^1', {127: 1, 9721: 1})
    """
    prime_factor = [i for i in range(2, num+1) if not num % i and is_prime(i)] # get prime numbers of num
    factorization = {} # factorization is a dictionary, key stands for prime factor, and value stands for power
    n = num
    power = 0

    for i in prime_factor:
        
        while not n % i:   # this loop will keep divide n by its prime factor as long as it's divisible
            n = n / i
            power += 1
            
        if n % i:                      # when n is no longer divisible by the prime factor
            factorization[i] = power   # it will save the prime factor & power to factorization, and reset power
            power = 0                  
    
    result = []
    
    for i in factorization:     # this loop will turn factorization(dictionary) into a clear string result
        result.append(f"{i}^{factorization[i]}")

    return " x ".join(result) , factorization # return result and factorization(dictionary)


