from typing import override
class Base:
    def process(self, value: str) -> int:
        return len(value)

class Derived(Base):
    @override
    def process(self, value: str) -> int:
        # This will be checked by type checkers
        # to ensure it actually overrides a method
        # in the parent class
        return len(value) * 2

    @override
    def proces(self, value: str) -> int: # Error!
        # Type checker will catch this misspelling
        return len(value) * 2
    