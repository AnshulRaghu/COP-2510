# Driver: Anshul Raghuvanshi, Navigator: Christian Taylor
# This program is intended to calculate the area of a hexagon using the user's input.
# We calculated this by the following formula: ((3√3)/2)*(s^2)

import math

s = float(input("\nEnter the side length of the hexagon: "))
b = (3 * math.sqrt(3)) / 2
z = b * (s * s)

print('The area of the hexagon with side length', s, 'is', round(z, 3))
