"""
A simple python program to test CPU performance by
generating a series of prime numbers
"""
import pyximport
pyximport.install()
from primes_cython import gen_primes

NUM_PRIMES = 100_000

if __name__ == '__main__':
    from time import time
    import sys

    print(f"Generating {NUM_PRIMES} prime numbers...", file=sys.stderr)
    start_time = time()
    gen_primes(NUM_PRIMES)
    duration = time() - start_time
    print(f"gen_primes({NUM_PRIMES}) took {duration} seconds", file=sys.stderr)
