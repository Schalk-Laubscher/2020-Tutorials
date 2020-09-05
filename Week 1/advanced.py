from math import sin, cos  # noqa: F401


def compareFD(f, fd, x, h):
    """Compare the errors of different finite differences."""
    exact = fd(x)
    # Loop through the different FD methods
    for method in (part_a, part_b, part_c, part_d):
        approx = method(f, x, h)      # Calculate approximation
        error  = abs(approx - exact)  # Take the absolute error

        # Get the function name from __doc__ attribute
        print(f'{method.__doc__:<35} error: {error:.2e}')


def part_a(f, x, h):
    """Forward difference"""
    return (f(x+h) - f(x)) / h


def part_b(f, x, h):
    """Backward difference"""
    return (f(x) - f(x-h)) / h


def part_c(f, x, h):
    """Central difference"""
    return (f(x+h) - f(x-h)) / (2*h)


def part_d(f, x, h):
    """Second-order forward difference"""
    return (-3*f(x) + 4*f(x+h) - f(x+2*h)) / (2*h)


if __name__ == '__main__':
    # Use if __name__ == '__main__' to only run code when the
    # file itself is run. This means you can import this file
    # without the following running!

    functions = (  # Define each function to test
        'x**3',
        '3*x**2 - 2*x',
        'sin(x)'
    )
    derivatives = (  # Define the respective derivatives
        '3*x**2',
        '6*x - 2',
        'cos(x)'
    )

    x, h = 1, 0.1

    for f_str, fd_str in zip(functions, derivatives):
        # Construct each function from the strings
        f  = eval('lambda x:' + f_str)
        fd = eval('lambda x:' + fd_str)
        print(f'\nComparing FD on {f_str} to {fd_str}')
        # Compare the finite difference methods
        compareFD(f, fd, x, h)
