def is_prime(num):
    List = [i for i in range(2, num) if not num % i]
    return not bool(List)
print(is_prime(12))