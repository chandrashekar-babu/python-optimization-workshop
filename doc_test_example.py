
def square(x):
    """Returns the square of argument - x
    
    Example:
       >>> square(2)
       4

       >>> square(3)
       9

       >>> square([10, 20, 30])
       [100, 400, 900]

    """
    if type(x) is list:
        return [ v*v for v in x ]
    else:
        return x*x


if __name__ == '__main__':
    import doctest
    doctest.testmod()

