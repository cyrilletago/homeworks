__author__ = 'cryrille'
from numbers import Number
from math import *


def rectangle_perimeter(length, width: Number) -> Number:
    """
    calculate perimeter of a rectangle from the length and the width
    :param length:the length
    :param width:the width
    :return:The perimeter(same unit as the side length)
    >>> rectangle_perimeter(2,4)
    12
    """
    return 2*(length + width)


def rectangle_area(length, width: Number) -> Number:
    """
    calculate area of a rectangle from the length and the width
    :param length:the length
    :param width:the width
    :return:The perimeter(same unit as the side length)
    >>> rectangle_perimeter(2,4)
    8
    """
    return length * width


def parallelogram_perimeter(first_side, second_side: Number) -> Number:
    """
    calculate perimeter of a parallelogram from the length of the
    two non parallel sides
    :param first_side: one side
    :param second_side: the other side(non parallel to the first)
    :return:The perimeter(same unit as the length of the sides)
     >>> parallelogram_perimeter(2,4)
    12
    """
    return 2*(first_side + second_side)


def parallelogram_area(base, height: Number) -> Number:
    """
    Calculate the area of a parallelogram from the base and the height
    :param base: the base of the paralellogram
    :param height:the height of the parallelogram
    :return: The area of the parallelogram
     >>> parallelogram_area(2,4)
    8
    """
    return base*height


def trapezium_perimeter(side1, side2, side3, side4: Number) -> Number:
    """
Calculate the perimeter of a trapezium when we have the four sides
    :param side1: the first side
    :param side2: the second side
    :param side3: the third side
    :param side4: the fourth side
    :return: the perimeter of the trapezium
    >>> trapezium_perimeter(2,4,5,3)
    14
    """
    return side1 + side2 + side3 + side4


def trapezium_area(parallel_side1, parallel_side2, height: Number) -> Number:
    """
Calculate the area of a trapezium when we have the length of the parallel sides
    :param parallel_side1: one of the parallel side
    :param parallel_side2: the other parallel side
    :param height: the height of the trapezium
    :return: the area of the trapezium
    >>> trapezium_area(2,4,6)
    13
    """
    return 0.5*(parallel_side1 + parallel_side2)*height


def triangle_perimeter(first_side, second_side, third_side: Number) -> Number:
    """
Calculate the perimeter of a triangle when we have the length of the three
     sides.
    :param first_side:first side
    :param second_side: second side
    :param third_side: third side
    :return: The perimeter of the triangle
    >>>triangle_perimeter(5,7,3)
    15
    """
    return first_side + second_side + third_side


def triangle_area(base, height: Number) -> Number:
    """
Calculate the area of a triangle given the base and the height
    :param base: the base of the triangle
    :param height: the height of the triangle
    :return:the area of the triangle
    >>>triangle_area(6,3)
    9
    """
    return 0.5*base*height


def circle_perimeter(radius: Number) -> Number:
    """
    Calculates the perimeter of a circle when given its radius
    :param radius: the radius
    :return:the perimeter of the triangle
    >>>circle_perimeter(3)
    18.84955592153876
    """
    return 2*pi*radius


def circle_area(radius: Number) -> Number:
    """
    calculates the area of a triangle when given its radius
    :param radius: the radius
    :return:the area of the triangle
    >>>circle_area(3)
    28.274333882308138
    """
    return pi*(radius**2)


def cube_surface_area(length: Number) -> Number:
    """
    Calculates the volume of a cube when given its length
    :param length: length
    :return:the volume of the cube
    >>>cube_surface_area(6)
    216
    """
    return 6*(length**2)


def cube_volume(length: Number) -> Number:
    """
    Calculates the volume of the cube, given the length of
    one side
    :param length: length on one side
    :return:the volume of the cube
    >>>cube_volume(6)
    216
    """
    return length**3


def cone_surface_area(radius, side: Number) -> Number:
    """
    Calculates the Surface area of a cone when given the radius and
    the length of the side
    :param radius: the radius
    :param side: the side of the cone(the hypotenuse to the angle
    between tha radius and the height
    :return:the surface area of the cone
    >>>cone_surface_area(2,5)
    43.982297150257104
    """
    return pi*((radius*side) + (radius**2))


def cone_volume(radius, height: Number) -> Number:
    """
    Calculates the volume of a cone when given the radius and the
    height
    :param radius: The radius of the cone
    :param height: The height of the cone
    :return:the volume of the cone
    >>>cone_volume(3,5)
    47.1238898038469
    """
    return (pi*(radius**2)*height)/3.0


def cylinder_surface_area(radius, height: Number) -> Number:
    """
    Calculates the surface area of a cylinder when given the radius
    and the height
    :param radius: the radius of the cone
    :param height: the height of the cone
    :return:The surface area of the cone
    >>>cylinder_surface_area(7,7)
    615.7521601035994
    """
    return 2*pi*((radius**2) + (radius*height))


def cylinder_volume(radius, height: Number) -> Number:
    """
    Calculates the volume of a cylinder given its radius and height
    :param radius: the radius of the cylinder
    :param height: the height of the cylinder
    :return:the volume of the cylinder
    >>>cylinder_volume(4,6)
    301.59289474462014
    """
    return pi*(radius**2)*height


def rectangular_solid_surface_area(length, width, height: Number) -> Number:
    """
    Calculates the surface area of a rectangular solid when given the length,
    width and height
    :param length: length of rectangular solid
    :param width: width of rectangular solid
    :param height: height of rectangular solid
    :return:the surface area of the rectangular solid
    >>>rectangular_solid_surface_area(4,9,6)
    228
    """
    return 2*((length*width) + (length*height) + (width*height))


def rectangular_solid_volume(length, width, height: Number) -> Number:
    """
    Calculates the volume of a rhombus when given the length, width and
    height
    :param length: the length of the rectangular solid
    :param width: the width of the rectangular solid
    :param height:the height of the rectangular solid
    :return:the value of the volume of the rectangular solid
    >>>rectangular_solid_volume(4,7,4)
    112
    """
    return length*width*height


def sphere_surface_area(value, choice='radius'):
    """
    Calculates the surface area of a sphere from radius or diameter.
    The choice is either the 'radius'(default) or
    'diameter' depending on the user. 'None' will be returned in case
    a value other than these two is
    entered as parameter.
    :param value: the value input by the user
    :param choice: the choice the user enters
    :return: The surface area of the sphere
    >>>sphere_surface_area(4,'diameter')
    50.265482457
    """
    if choice == 'radius':
        pass
    elif choice == 'diameter':
        value = (value/2.0)
    else:
        return None
    return 4*pi*value**2


def sphere_volume(value, choice='radius'):
    """
    Calculates the volume of a sphere when given its radius or diameter.
    The choices are 'radius'(default) or 'diameter'. None is returned in
    case a value other than this is entered
    :param value: the value entered by the user
    :param choice: the choice the user made
    :return:the volume of the sphere
    >>>sphere_volume(3, 'radius')
    113.09733552923
    """
    if choice == 'radius':
        pass
    elif choice == 'diameter':
        value = (value/2.0)
    else:
        return None
    return (4.0/3.0)*pi*value**3


def rhombus_area(length_diagonal1, length_diagonal2: Number) -> Number:
    """
    Calculates the area a rhombus when given the length of two distinct sides.
    :param length_diagonal1: length of one diagonal
    :param length_diagonal2: length of the other diagonal
    :return:the area of the rhombus
    >>>rhombus_area(4,5)
    10.0
    """
    return length_diagonal1*length_diagonal2/2.0


def rhombus_area1(length_of_side, any_interior_angle) -> Number:
    """
    computes the area of a rhombus when given the length of any side
    and any interior angle.
    :param length_of_side: the length of any side of the rhombus
    :param any_interior_angle: any interior angle of the rhombus
    :return:the area of the rhombus
    >>>rhombus_area1(4,45)
    13.6144564
    """
    return (sin(any_interior_angle))*length_of_side**2
