#cython: language_level = 3

import cython

@cython.locals(limit=cython.uint, d=cython.uint, number=cython.uint)
def is_prime(number):
    """Returns True if 'number' is prime"""
    limit = int(number ** 0.5) + 1
    for d in range(2, limit):
        if number % d == 0:
            return False
    return True


def gen_primes(num_primes: cython.uint):
    """Generates first 'num_primes' series of prime numbers"""
    v: cython.uint = 2
    while num_primes:
        if is_prime(v):
            print(v)
            num_primes -= 1
        v += 1
