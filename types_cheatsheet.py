# This is how you declare the type of a variable type in Python 3.6
x: int = 1

# In Python 3.5 and earlier you can use a type comment instead
# (equivalent to the previous definition)
x = 1  # type: int

# You don't need to initialize a variable to annotate it
a: int  # Ok (no value at runtime until assigned)

# The latter is useful in conditional branches
child: bool
if age < 18:
    child = True
else:
    child = False

# --------------------------------------------------------------

from typing import List, Set, Dict, Tuple, Optional

# For simple built-in types, just use the name of the type
x: int = 1
x: float = 1.0
x: bool = True
x: str = "test"
x: bytes = b"test"

# For collections, the name of the type is capitalized, and the
# name of the type inside the collection is in brackets
x: List[int] = [1]
x: Set[int] = {6, 7}

# Same as above, but with type comment syntax
x = [1]  # type: List[int]

# For mappings, we need the types of both keys and values
x: Dict[str, float] = {'field': 2.0}

# For tuples, we specify the types of all the elements
x: Tuple[int, str, float] = (3, "yes", 7.5)

# Use Optional[] for values that could be None
x: Optional[str] = some_function()
if x is not None:
    print(x)
# --------------------------------------------------------------
from typing import Callable, Iterable, Union, Optional, List

# This is how you annotate a function definition


def stringify(num: int) -> str:
    return str(num)

# And here's how you specify multiple arguments


def plus(num1: int, num2: int) -> int:
    return num1 + num2

# Add default value for an argument after the type annotation


def f(num1: int, my_float: float = 3.5) -> float:
    return num1 + my_float


# This is how you annotate a callable (function) value
x: Callable[[int, float], float] = f

# A generator function that yields ints is secretly just a function that
# returns an iterable (see below) of ints, so that's how we annotate it


def f(n: int) -> Iterable[int]:
    i = 0
    while i < n:
        yield i
        i += 1

# You can of course split a function annotation over multiple lines


def send_email(address: Union[str, List[str]],
               sender: str,
               cc: Optional[List[str]],
               bcc: Optional[List[str]],
               subject='',
               body: Optional[List[str]] = None
               ) -> bool:
    ...

# An argument can be declared positional-only by giving it a name
# starting with two underscores:


def quux(__x: int) -> None:
    pass


quux(3)  # Fine
quux(__x=3)  # Error

#---------------------------------------------------------------------
from typing import Union, Any, List, Optional, cast

# To find out what type mypy infers for an expression anywhere in
# your program, wrap it in reveal_type().  Mypy will print an error
# message with the type; remove it again before running the code.
reveal_type(1)  # -> Revealed type is 'builtins.int'

# Use Union when something could be one of a few types
x: List[Union[int, str]] = [3, 5, "test", "fun"]

# Use Any if you don't know the type of something or it's too
# dynamic to write a type for
x: Any = mystery_function()

# If you initialize a variable with an empty container or "None"
# you may have to help mypy a bit by providing a type annotation
x: List[str] = []
x: Optional[str] = None

# This makes each positional arg and each keyword arg a "str"


def call(self, *args: str, **kwargs: str) -> str:
    request = make_request(*args, **kwargs)
    return self.do_api_query(request)


# Use a "type: ignore" comment to suppress errors on a given line,
# when your code confuses mypy or runs into an outright bug in mypy.
# Good practice is to comment every "ignore" with a bug link
# (in mypy, typeshed, or your own code) or an explanation of the issue.
x = confusing_function()  # type: ignore  # https://github.com/python/mypy/issues/1167

# "cast" is a helper function that lets you override the inferred
# type of an expression. It's only for mypy -- there's no runtime check.
a = [4]
b = cast(List[int], a)  # Passes fine
c = cast(List[str], a)  # Passes fine (no runtime check)
reveal_type(c)  # -> Revealed type is 'builtins.list[builtins.str]'
print(c)  # -> [4]; the object is not cast

# If you want dynamic attributes on your class, have it override "__setattr__"
# or "__getattr__" in a stub or in your source code.
#
# "__setattr__" allows for dynamic assignment to names
# "__getattr__" allows for dynamic access to names


class A:
    # This will allow assignment to any A.x, if x is the same type as "value"
    # (use "value: Any" to allow arbitrary types)
    def __setattr__(self, name: str, value: int) -> None: ...

    # This will allow access to any A.x, if x is compatible with the return type
    def __getattr__(self, name: str) -> int: ...


a.foo = 42  # Works
a.bar = 'Ex-parrot'  # Fails type checking

#------------------------------------------------------------------
