"""
A simple python program to test CPU performance by
generating a series of prime numbers
"""

NUM_PRIMES = 100_000

def is_prime(number):
    "Returns True if 'number' is prime"
    limit = int(number ** 0.5) + 1
    for d in range(2, limit):
        if number % d == 0:
            return False
    return True

def gen_primes(num_primes):
    "Generates first 'num' series of prime numbers"
    v = 2
    while num_primes:
        if is_prime(v):
            print(v)
            num_primes -= 1
        v += 1

if __name__ == '__main__':
    from time import time
    import sys

    print(f"Generating {NUM_PRIMES} prime numbers...", file=sys.stderr)
    start_time = time()
    gen_primes(NUM_PRIMES)
    duration = time() - start_time
    print(f"gen_primes({NUM_PRIMES}) took {duration} seconds", file=sys.stderr)
