__author__ = 'cryrille'
from geom_formulae import *


from nose.tools import *


def test_rectangle_area_int():
    assert rectangle_area(1, 1) == 1
    assert rectangle_area(2, 4) == 8
    length = 5
    width = 2
    assert rectangle_area(4*length, 4*width) == 16*rectangle_area(length, width)


def test_parallelogram_area_int():
    assert parallelogram_area(1, 1) == 1
    assert parallelogram_area(2, 4) == 8
    base = 5
    height = 2
    assert parallelogram_area(4*base, 4*height) == 16*parallelogram_area(base, height)


def test_trapezium_perimeter_int():
    assert trapezium_perimeter(1, 1, 1, 1) == 4
    assert trapezium_perimeter(2, 3, 1, 1) == 7
    side1 = 3
    side2 = 2
    side3 = 4
    side4 = 1
    assert trapezium_perimeter(4*side1, 4*side2, 4*side3, 4*side4) == 4*trapezium_perimeter(side1, side2, side3, side4)


def test_triangle_perimeter_int():
    assert triangle_perimeter(1, 1, 1) == 3
    assert triangle_perimeter(2, 3, 1) == 6
    side1 = 3
    side2 = 2
    side3 = 4
    assert triangle_perimeter(4*side1, 4*side2, 4*side3,) == 4*triangle_perimeter(side1, side2, side3)


def test_circle_area_int():
    assert circle_area(1) == 3.141592653589793
    assert circle_area(6) == 113.09733552923255
    radius = 4
    assert circle_area(3*radius) == 9*circle_area(radius)


def test_cube_volume_int():
    assert cube_volume(1) == 1
    assert cube_volume(4) == 64
    length = 3
    assert cube_volume(5*length) == 125*cube_volume(length)


def test_cone_volume_int():
    assert cone_volume(1, 1) == 1.0471975511965976
    assert cone_volume(2, 3) == 12.566370614359172
    radius = 1
    height = 2
    assert cone_volume(2*radius, 2*height) == 8*cone_volume(radius, height)


def test_cylinder_volume_int():
    assert cylinder_volume(1, 1) == 3.141592653589793
    assert cylinder_volume(2, 5) == 62.83185307179586
    radius = 3
    height = 4
    assert cylinder_volume(2*radius, 2*height) == 8*cylinder_volume(radius, height)


def test_rectangular_solid_volume_int():
    assert rectangular_solid_volume(1, 1, 1) == 1
    l = 4
    w = 3
    h = 1
    assert rectangular_solid_volume(2*l, 2*w, 2*h) == 8*rectangular_solid_volume(l, w, h)


def test_sphere_surface_area_int():
    assert sphere_surface_area(1, 'radius') == 12.566370614359172
    radius = 5
    assert sphere_surface_area(2*radius, 'radius') == 4*sphere_surface_area(radius, 'radius')