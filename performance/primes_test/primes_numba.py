"""
A simple python program to test CPU performance by
generating a series of prime numbers
"""
from numba import njit, boolean, uint64, void

NUM_PRIMES = 100_000


@njit(boolean(uint64))
#@jit(boolean(uint64), nopython=True )
def is_prime(number):
    "Returns True if 'number' is prime"
    limit = int(number ** 0.5) + 1
    for d in range(2, limit):
        if number % d == 0:
            return False
    return True


@njit(void(uint64))
def gen_primes(num_primes):
    """Prints the first 'num_primes' series of prime numbers"""
    v = 2
    while num_primes:
        if is_prime(v):
            print(v)
            num_primes -= 1
        v += 1


if __name__ == '__main__':
    from time import time
    import sys

    print(f"Print the first {NUM_PRIMES} prime numbers...", file=sys.stderr)
    start_time = time()
    gen_primes(NUM_PRIMES)
    duration = time() - start_time
    print(f"print_primes({NUM_PRIMES}) took {duration:.6f} seconds.",
          file=sys.stderr)
