amount = input("What's the order amount? ")
state = input("What's the state? ")
tax = 0

if "WI" in state:
    tax = 0.055
taxamount = str(round(tax * float(amount),2))
total = str(float(amount) + float(taxamount))

output = """
The subtotal is ${0}
the tax is ${1}
The total is ${2}
"""
print(output.format(amount,taxamount,total))
