# Driver: Anshul Raghuvanshi, Navigator: Christian Taylor
# This program is intended to calculate the runway length for an airplane's takeoff.
# We calculated this by the following formula: (x^2)/2a

x = float(input("\nEnter the plane's take off speed in m/s: "))
y = float(input("\nEnter the acceleration in m/s^2: "))
z = (x*x)/(2*y)

print('The minimum runway length needed for this airplane is', round(z, 4), 'meters.')
