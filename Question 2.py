# Driver: Anshul Raghuvanshi
# Navigator: Christian Taylor
# This program is designed to take inputs from the user of two retail items they would like to add to their list.
# The user will then provide details about the item such as the amount in stock and its price.
# After the input is taken from the user, the program creates a table which summarizes the results of the items.

class Retail_Item:
    def __init__(self, item, amount, price):
        self.item = item
        self.amount = amount
        self.price = price

    def get_item(self):
        return self.item

    def get_amount(self):
        return self.amount

    def get_price(self):
        return self.price

def main():
    item1 = input('Please enter the first item you would like to purchase: ')
    amount1 = int(input('Please enter the amount in stock of the first item: '))
    price1 = float(input('Please enter the price of the first item: '))

    item2 = input('\nPlease enter the second item you would like to purchase: ')
    amount2 = int(input('Please enter the amount in stock of the second item: '))
    price2 = float(input('Please enter the price of the second item: '))

    retail1 = Retail_Item(item1, amount1, price1)
    retail2 = Retail_Item(item2, amount2, price2)

    a = "Item"
    b = "Amount"
    c = "Price"

    format1 = format(item1, "12")
    format2 = format(amount1, "12")
    format3 = format(price1, "21,.2f")
    format4 = format(item2, "12")
    format5 = format(amount2, "12")
    format6 = format(price2, "21,.2f")
    format7 = format(a, "18")
    format8 = format(b, "22")
    format9 = format(c, "3")

    print('\nName of item 1: {}'.format(retail1.get_item()))
    print('Amount of item 1: {}'.format(retail1.get_amount()))
    print('Price of item 1: {:.2f}'.format(retail1.get_price()))
    print('\nName of item 2: {}'.format(retail2.get_item()))
    print('Amount of item 2: {}'.format(retail2.get_amount()))
    print('Price of item 2: {:.2f}'.format(retail2.get_price()))
    print('\nHere is a summary of the items you added: ')
    print(format7, format8, format9)
    print('-----------------------------------------------')
    print(format1, format2, format3)
    print(format4, format5, format6)

main()
