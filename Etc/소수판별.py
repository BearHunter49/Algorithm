import math


def is_prime_number(x):
    # for i in range(2, x):
    for i in range(2, int(math.sqrt(x)) + 1):  # root(16) = 4 이기 때문에
        if x % i == 0:
            return False

    return True


print(is_prime_number(7))




