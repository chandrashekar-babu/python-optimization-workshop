"""
A simple python program to test CPU performance by
generating a series of prime numbers
"""
import sys
from time import time
from primes_pythran import gen_primes

NUM_PRIMES = 100_000


if __name__ == '__main__':
    print(f"Generating {NUM_PRIMES} prime numbers...", file=sys.stderr)
    start_time = time()
    gen_primes(NUM_PRIMES)
    duration = time() - start_time
    print(f"print_primes({NUM_PRIMES}) took {duration:.6f} seconds",
          file=sys.stderr)
