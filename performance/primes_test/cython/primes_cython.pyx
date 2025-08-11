#cython: language_level = 3

def is_prime(unsigned int number):
    """Returns True if 'number' is prime"""
    cdef unsigned int limit
    cdef unsigned int d
    limit = int(number ** 0.5) + 1
    for d in range(2, limit):
        if number % d == 0:
            return False
    return True


def gen_primes(unsigned int num_primes):
    """Generates first 'num_primes' series of prime numbers"""
    cdef unsigned int v = 2
    while num_primes:
        if is_prime(v):
            print(v)
            num_primes -= 1
        v += 1
