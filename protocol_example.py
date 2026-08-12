from typing import Protocol, List, Iterator, TypeVar
T = TypeVar('T')

class Sized(Protocol):
    """A protocol that requires a __len__ method."""
    def __len__(self) -> int:
        ...

class Iterable(Protocol[T]):
    """A protocol that requires an __iter__ method."""
    def __iter__(self) -> Iterator[T]:
        ...

def get_first_and_size(obj: Iterable[T] & Sized) -> tuple[T, int]:
    """Return the first element and the size of the object."""
    return next(iter(obj)), len(obj)
