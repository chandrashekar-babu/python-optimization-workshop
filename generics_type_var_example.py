from typing import TypeVar, List

T = TypeVar('T') # Define a type variable

def first(items: List[T]) -> T:
    """Return the first item from a list."""
    if not items:
        raise ValueError("Empty list")
    return items[0]

# Usage with different types:
first([1, 2, 3]) # Returns int
first(["a", "b", "c"]) # Returns str
first([True, False]) # Returns bool