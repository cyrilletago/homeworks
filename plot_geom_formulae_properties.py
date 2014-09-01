__author__ = 'cryrille'
from pylab import *

from geom_formulae import *


def plot_rectangle_plot():
    v_rectangle_area = np.vectorize(rectangle_area)
    v_rectangle_perimeter = np.vectorize(rectangle_perimeter)

    s = np.linspace(0, 10)  # our side lengths

    a = v_rectangle_area(3, s)  # the areas
    p = v_rectangle_perimeter(3, s)  # the perimeters

    plot(s, a, '-r', label="Area")
    plot(s, p, ':b', label="Perimeter")

    xlabel('side length')
    ylabel('geo values')
    title('Rectangle Geo Properties')
    legend(loc='upper right')

    show()


def plot_parallelogram_props():
    v_parallelogram_area = np.vectorize(parallelogram_area)
    v_parallelogram_perimeter = np.vectorize(parallelogram_perimeter)

    s = np.linspace(0, 10)  # our side lengths
    h = np.linspace(0, 10)  # our height

    a = v_parallelogram_area(3, s)  # the areas
    p = v_parallelogram_perimeter(3, h)  # the perimeters

    plot(s, a, '-r', label="Area")
    plot(h, p, ':b', label="perimeter")

    xlabel('side length')
    ylabel('geo values')
    title('Rectangle Geo Properties')
    legend(loc='upper right')

    show()


def plot_circle_props():
    v_circle_area = np.vectorize(circle_area)
    v_circle_perimeter = np.vectorize(circle_perimeter)

    s = np.linspace(0, 10)  # our side lengths

    a = v_circle_area(s)  # the areas
    p = v_circle_perimeter(s)  # the perimeters

    plot(s, a, '-r', label="Area")
    plot(s, p, ':b', label="perimeter")

    xlabel('radius')
    ylabel('geo values')
    title('Circle Geometric Properties')
    legend(loc='upper right')

    show()


def plot_trapezium_props():
    v_trapezium_area = np.vectorize(trapezium_area)
    v_trapezium_perimeter = np.vectorize(trapezium_perimeter)

    side = np.linspace(0, 10)  # our side lengths
    height = np.linspace(0, 10)  # our height

    a = v_trapezium_area(3, height)  # the areas
    p = v_trapezium_perimeter(3, side)  # the perimeters

    plot(height, a, '-r', label="Area")
    plot(side, p, ':b', label="perimeter")

    xlabel('side length')
    ylabel('geo values')
    title('Trapezium Geo Properties')
    legend(loc='upper right')

    show()
