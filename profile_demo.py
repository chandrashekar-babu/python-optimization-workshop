import cProfile
import random
import time


def generate_numbers(n):
    """Generate a list of random integers."""
    numbers = [random.randint(1, 10000) for _ in range(n)]
    time.sleep(0.1)  # Simulate slow I/O
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
    return sum(1 for num in numbers if is_prime(num))


def sort_numbers(numbers):
    """Sort numbers with an intentionally inefficient sort."""
    return sorted(numbers, reverse=True)  # Descending sort


def string_processing(numbers):
    """Convert numbers to strings and process them."""
    strings = [str(num) for num in numbers]
    reversed_strings = [s[::-1] for s in strings]
    return "-".join(reversed_strings)


def main():
    nums = generate_numbers(5000)
    prime_count = count_primes(nums)
    sorted_nums = sort_numbers(nums)
    result_string = string_processing(sorted_nums)
    print(f"Found {prime_count} primes. Processed string length: {len(result_string)}")


if __name__ == "__main__":
    # Profile the 'main' function
    cProfile.run("main()")
