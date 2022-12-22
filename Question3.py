# Driver: Christian Taylor
# Navigator: Anshul Raghuvanshi

# This program allows us to calculate the amount of the tip given the tip amount
# percentage and the subtotal.

# Use the input function to prompt the user to assign a value of type float to two new
# variables "subtotal" and "tipAmount".

subtotal = float(input('Please enter the subtotal: '))
tipAmount = float(input('Now enter the tip amount (as a %): '))

# Create a new variable called "tip". In order to calculate the tip, you take the percentage
# amount and divide it by 100 then multiply the result by the subtotal.
# Create another variable "total". The sum of the subtotal and the tip gives you the total.

tip = (tipAmount/100) * subtotal
total = subtotal + tip

# Use the format function inside of the print function to adjust the number of decimal places
# to two and to format as a floating point value.
# Use sep="" to remove the space between the dollar sign and the numerical value.

print('Subtotal: $', format(subtotal, ",.2f"), sep="")
print('Tip: $', format(tip, ",.2f"), sep="")
print('Total: $', format(total, ",.2f"), sep="")




