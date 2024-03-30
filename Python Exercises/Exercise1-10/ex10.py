
price = []
quan = []
price.append(input("Enter price of item 1: "))
quan.append(input("Enter quanity of item 1: "))
price.append(input("Enter price of item 2: "))
quan.append(input("Enter quanity of item 2: "))
price.append(input("Enter price of item 3: "))
quan.append(input("Enter quanity of item 3: "))
subtotal = 0
for i in range(len(price)):
    subtotal =subtotal + (int(price[i]) * int(quan[i]))
tax = subtotal * 1.065
total = tax + subtotal
output = """
Subtotal: {0}
tax: {1}
total: {2}
"""
print(output.format(subtotal,tax,total))
