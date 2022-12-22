# Driver:    Christian Taylor
# Navigator: Anshul Raghuvanshi

# This program allows us to calculate the slope of a straight line given the coordinates of any two points.

# Use the input function to enable the user to assign a float value to the coordinates of each point.

x1 = float(input('Enter the x-coordinate for point1: '))
y1 = float(input('Enter the y-coordinate for point1: '))
x2 = float(input('Enter the x-coordinate for point2: '))
y2 = float(input('Enter the y-coordinate for point2: '))

# Assign the value of the slope in the form of a formula to a new variable called "slope".

slope = (y2-y1)/(x2-x1)

# Use the round function to round the slope to five decimal places.

roundedSlope = round(slope, 5)


print('The slope for the line that connects two points (', x1, ',', y1, ') and (', x2, ',', y2, ') is', roundedSlope,)

