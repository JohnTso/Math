def get_factor(num):

    factors = []
    for i in range(num):
        if not num % i:
            factors.append(i)

    return factors