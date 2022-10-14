# Driver: Anshul Raghuvanshi (U69656337), Navigator: Christian Taylor (U75799592)
# This program is intended to calculate the final price after discount of the packages bought by using the user's input.
# We calculated the discount by multiplying 99 by the number of packages the user entered and the discounted percent
# We calculated the finalPrice by subtracting the non-discounted total price from the discount amount.

a = 99
x = float(input('Enter the number of packages '))
discount = 0

if x >= 100:
    print('Number of packages: ', x)
    discount = x * a * 0.4
    print('Your discount amount after 40% is: $', discount)
    finalPrice = (x * a) - discount
    print('Your total amount is: $', finalPrice)
elif x >= 50:
    print('Number of packages: ', x)
    discount = x * a * 0.3
    print('Your discount amount after 30% is: $', discount)
    finalPrice = (x * a) - discount
    print('Your total amount is: $', finalPrice)
elif x >= 20:
    print('Number of packages: ', x)
    discount = x * a * 0.2
    print('Your discount amount after 20% is: $', discount)
    finalPrice = (x * a) - discount
    print('Your total amount is: $', finalPrice)
elif x >= 10:
    print('Number of packages: ', x)
    discount = x * a * 0.1
    print('Your discount amount after 10% is: $', discount)
    finalPrice = (x * a) - discount
    print('Your total amount is: $', finalPrice)
else:
    print('Number of packages: ', x)
    discount = x * a * 0.0
    print('Your discount amount after 0% is: $', discount)
    finalPrice = (x * a) - discount
    print('Your total amount is: $', finalPrice)