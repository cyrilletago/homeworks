__author__ = 'cryrille'
from pylab import *

from geom_formulae import *

v_rectangle_area = np.vectorize(rectangle_area)
v_rectangle_perimeter = np.vectorize(rectangle_perimeter)

S = np.linspace(0, 10)  # our side lengths

A = v_rectangle_area(S, S)  # the areas
P = v_rectangle_perimeter(S, S)  # the perimeters

plot(S, A, '-r', label="Area")
plot(S, P, ':b', label="Perimeter")

xlabel('side length')
ylabel('geo values')
title('Rectangle Geo Properties')
legend(loc='upper right')

show()
