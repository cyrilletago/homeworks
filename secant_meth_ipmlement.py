__author__ = 'cryrille'
from math import *
from dimension_validate import *
from numpy import *


def secant_method(func, first, second, err):
    """
    This function computes the roots of a given function whe given two values,
    assumed to be close to the root(one higher and one lower)
    :param func: The function for which the roots are to be calculated.
    :param first: The fist estimate or starting Guess
    :param second: The second estimate or other guess
    :param err: The error
    :return: root, the root of the function
    >>> round(secant_method(math.sin, pi/2, 3*pi/2, 1e-6), 6)
    3.141593
    """

    if dim_complete(func) and dim_complete(first) and dim_complete(second) and dim_complete(err):
        if dim_type(first) and dim_type(second) and dim_type(err)and callable(func):
            if dim_sign(err):
                x0, x1 = first, second
                while fabs(func(x1)) > err and func(x0) != func(x1):
                    x2 = (x0*func(x1) - x1*func(x0))/(func(x1) - func(x0))
                    x0 = x1
                    x1 = x2
                root = x1
                return root
            else:
                raise ValueError("Please enter positive numbers: "+str(err))
        raise TypeError("One or more arguments is(are) not number(s)! Enter a Number")
    raise AttributeError("OH!!! one of the arguments was forgotten, Check it!")

"""
def sine(x):
    return sin
print(secant_method(sin, pi+1, pi-1, 1e-6))
"""


def trapezoid_method(func, start_point, end_point, count):
    """
    This computes the integral of a given function from start_point to end_point.
    :param func: The function whose integral is required
    :param start_point:The lower limit  of the integral
    :param end_point: The upper limit of the integral
    :param count: The number of sections we want to divide the graph into
    :return: The integral of function entered
    >>> print(round(trapezoid_method(math.sin, 0, pi, 1000000), 6))
    2.0
    """
    if dim_complete(func) and dim_complete(start_point) and dim_complete(end_point) and dim_complete(count):
        if dim_type(start_point) and dim_type(end_point) and dim_type(count) and callable(func):
            if dim_sign(count):
                step = (end_point - start_point)/count
                x1 = start_point
                x2 = x1 + step
                temp = 0
                for i in range(1, count + 1):
                    temp += func(x2) + func(x1)
                    x1 = x2
                    x2 = x2 + step
                return step*temp/2.0
            else:
                raise ValueError("Please enter positive numbers: "+str(count))
        raise TypeError("One or more arguments is(are) not number(s)! Enter a Number")
    raise AttributeError("OH!!! one of the arguments was forgotten, Check it!")


"""
def linear(x):
    return 1
print(trapezoid_method(linear, 0, 5, 5))
"""


def midpoint_method(func, lower_limit, upper_limit, count):
    """
    This function computes the integral of a function given its limit of integration
    :param func: The function whose integral is to be computed
    :param lower_limit: The lower_limit of the integral
    :param upper_limit: The upper limit of the integral
    :param count: the number of intervals you want to subdivide
    :return: The integral value of the function from the lower
    limit to the upper limit
    >>> def linear(x):
    >>> return 1
    >>> print(midpoint_method(linear, 0, 5, 5))
    5.0
    """
    if dim_complete(func) and dim_complete(upper_limit) and dim_complete(upper_limit) and dim_complete(count):
            if dim_type(lower_limit) and dim_type(upper_limit) and dim_type(count) and callable(func):
                if dim_sign(count):
                    h = (upper_limit - lower_limit)/count
                    x = linspace(lower_limit, upper_limit, count+1)
                    midpoints_array = [0]*count
                    summ = 0
                    for i in range(1, count + 1):
                        midpoints_array[i-1] = (x[i] + x[i-1])/2
                        summ += func(midpoints_array[i-1])
                    return summ*h
                else:
                    raise ValueError("Please enter positive numbers: "+str(count))
            raise TypeError("One or more arguments is(are) not number(s)! Enter a Number")
    raise AttributeError("OH!!! one of the arguments was forgotten, Check it!")

# print(round(midpoint_method(math.sin, 0, pi, 100000), 6))
"""
def linear(x):
    return 1
print(trapezoid_method(linear, 0, 2, )
"""


def simpsons_method(func, lower_limit, upper_limit, count):
    """
    Computes the integral of a given function given its lower and upper limits by
    approximating the function with a quadratic.
    :param func: The function whose integral is required
    :param lower_limit: The lower limit
    :param upper_limit: The upper limit
    :param count:The number of interval desired
    :return: The integral of the function
    >>> def linear(x):
    >>> return 1
    >>> print(simpsons_method(linear, 0, 5, 5))
    5
    """
    if dim_complete(func) and dim_complete(upper_limit) and dim_complete(upper_limit) and dim_complete(count):
            if dim_type(lower_limit) and dim_type(upper_limit) and dim_type(count) and callable(func):
                if dim_sign(count):
                    h = (upper_limit - lower_limit)/count
                    x = linspace(lower_limit, upper_limit, count)
                    sum_ends = func(x[0]) + func(x[count - 1])
                    sum_odd = 0
                    sum_even = 0
                    for i in range(1, count, 2):
                        sum_odd += func(x[i])
                    for i in range(2, count, 2):
                        sum_even += func(x[i])
                    return h*(sum_ends + 2*sum_even + 4*sum_odd)/3
                else:
                    raise ValueError("Please enter positive numbers: "+str(count))
            raise TypeError("One or more arguments is(are) not number(s)! Enter a Number")
    raise AttributeError("OH!!! one of the arguments was forgotten, Check it!")


print(round(simpsons_method(math.sin, 0, pi, 1000000), 6))

"""def newt_raph_method(func, derivative, guess, err):
    x0 = guess

    while fabs(func(x0) != 0):
        if derivative(x0)
        result = x0 - (func(x0)/derivative(x0))
    return result"""