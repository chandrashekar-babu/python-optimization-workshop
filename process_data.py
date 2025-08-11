import cProfile
import random
import time


def generate_numbers(n):
    """Generate a list of random integers."""
    numbers = [random.randint(1, 10000) for _ in range(n)]
    return numbers


def is_prime(num):
    """Check if a number is prime."""
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def count_primes(numbers):
    """Count how many numbers in the list are prime."""
    total = 0
    for n in numbers:
        if is_prime(n):
            total += 1
    return total


def string_processing(numbers):
    """Convert numbers to strings and process them."""
    result = ""
    for n in numbers:
        result += str(n)
    return result

def main():
    nums = generate_numbers(5000)
    prime_count = count_primes(nums)
    result_string = string_processing(nums)
    print(f"Found {prime_count} primes. Processed string length: {len(result_string)}")


if __name__ == "__main__":
    # Profile the 'main' function
    cProfile.run("main()")
