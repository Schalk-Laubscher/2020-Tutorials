from math import sin, cos


def compareFD(f, fd, x, h):
    exact = fd(x)
    # Calculate the differences
    forward_difference   = (f(x+h) - f(x)) / h
    backward_difference  = (f(x) - f(x-h)) / h
    central_difference   = (f(x+h) - f(x-h)) / (2*h)
    second_order_forward = (-3*f(x)+4*f(x+h)-f(x+2*h)) / (2*h)

    print('Forward difference error:  ', abs(exact - forward_difference))
    print('Backward difference error: ', abs(exact - backward_difference))
    print('Central difference error:  ', abs(exact - central_difference))
    print('Second order forward error:', abs(exact - second_order_forward))


x, h = 1, 0.1


def function(x):
    return x**3


def derivative(x):
    return 3*x**2


print('Comparing FD on x^3 to 3x^2')
compareFD(function, derivative, x, h)


def function(x):
    return 3*x**2 - 2*x


def derivative(x):
    return 6*x - 2


print('Comparing FD on 3x^2 - 2x to 6x - 2')
compareFD(function, derivative, x, h)


def function(x):
    return sin(x)


def derivative(x):
    return cos(x)


print('Comparing FD on sin(x) to cos(x)')
compareFD(function, derivative, x, h)
