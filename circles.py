#!/usr/bin/python3

from math import pi

def circle_area(r):
    return pi*(r**2)

#Test function
radii = [2, 0, -3, 2 + 5j, True, "radius"]

for r in radii:
    A = circle_area(r)
    print("Area of circle with r = {} is {}.".format(r, A))
