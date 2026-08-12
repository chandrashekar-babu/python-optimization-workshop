from typing import TypeVar, Generic, List, Optional

T = TypeVar('T')

class Stack(Generic[T]):
    def __init__(self) -> None:
        self.items: List[T] = []

    def push(self, item: T) -> None:
        self.items.append(item)

    def pop(self) -> Optional[T]:
        if not self.items:
            return None
        return self.items.pop()

    def peek(self) -> Optional[T]:
        if not self.items:
            return None
        return self.items[-1]

# Integer stack
int_stack = Stack[int]()
int_stack.push(1)
int_stack.push(2)
print(int_stack.pop())  # Output: 2

# String stack
str_stack = Stack[str]()
str_stack.push("hello")
str_stack.push("world")
print(str_stack.pop())  # Output: "world"

# The type checker will catch the following error:
# int_stack.push("not an int")  # Error: Argument 1 to "push" of "Stack" has incompatible type "str"; expected "int"
