from typing import Union
def square(x: Union[int, float, complex]) -> int|float|complex:
    return x*x


a: str = "Hello world"
v: int = 10


if __name__ == '__main__':
    print(square(4))
    print(square(5.2))
    print(square(4+5j))
    print(a)
    a = "100"
    print(a)
