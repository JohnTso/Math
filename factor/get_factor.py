def get_factor(num):

    factors = []
    for i in range(1, num):
        if not num % i:
            factors.append(i)

    return factors