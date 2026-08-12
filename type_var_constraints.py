from typing import TypeVar, List, Union
from typing import TypeVar, List

T = TypeVar('T') # Define a type variable

# Type variable constrained to numeric types
Number = TypeVar('Number', int, float, complex)

def add_all(numbers: List[Number]) -> Number:
    """Sum all numbers in the list."""
    result: Number = numbers[0]
    for n in numbers[1:]:
        result += n
    return result

# Valid usage:
add_all([1, 2, 3]) # OK, returns int
add_all([1.0, 2.5, 3.7]) # OK, returns float

# Invalid usage (would be caught by type checker):
add_all(["a", "b", "c"]) # Error: strings aren't allowed