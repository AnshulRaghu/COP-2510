# Driver: Anshul Raghuvanshi (U69656337), Navigator: Christian Taylor (U75799592)
# This program is intended to calculate the wind-chill temperature using the user's input.
# We calculated this by the following formula: (35.74 + (0.6215t) - (35.75 * math.pow(v, 0.16)) + (0.4275t * math.pow(v, 0.16))

import math

finalTemp = 0
t = float(input('Enter a temperature between -58 degrees Fahrenheit and 41 degrees Fahrenheit '))

while t < -58 or t > 41:
    t = float(input('Invalid, please enter a new value between -58 F and 41 F '))

v = float(input('Enter a windchill greater than 2mph '))

while v < 2:
    v = float(input('Invalid, please enter a new value greater than or equal to 2 '))

finalTemp = 35.74 + (0.6215 * t) - (35.75 * math.pow(v, 0.16)) + (0.4275 * t * math.pow(v, 0.16))

print('The wind-chill temperature is', round(finalTemp, 3))