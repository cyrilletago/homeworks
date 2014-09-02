__author__ = 'cryrille'
from numbers import Number


def dim_validate(dim):
    """
    Test if dim is a Number and is >= 0.

    >>> dim_validate(5)
    True

    >>> dim_validate(-5)
    False

    >>> dim_validate("a string")
    False
    """
    return isinstance(dim, Number) and dim >= 0


def dim_sign(dim):
    """
    Tests the sign of the dimension.
    :param dim: dimension to be tested
    :return: True if the sing is positive and False if it is negative
    >>> dim_sign(5)
    True
    >>> dim_sign(-5)
    False
    """
    return dim >= 0


def dim_type(dim):
    """
    Tests if the type of the dimension is a number
    :param dim:the dimension to be tested
    :return:True if the dimension is a number and false if it is anything else
    >>> dim_type(7)
    True
    """
    return isinstance(dim, Number)


def dim_incomplete(dim):
    """
    Tests if the argument was not entered
    :param dim: the argument
    :return:True if the argument is None and False otherwise.

    """
    return dim == None
