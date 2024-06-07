amount = input("What is the order amount? ")
state = input("What state do you live in? ")
county = input("What county do you live in? ")
taxper = 0
if "wis" in state.lower():
    taxper = .05
    if "eau claire" in county.lower():
        taxper = taxper+.005
    if "dunn" in county.lower():
        taxper = taxper+.004
if "ill" in state.lower():
    taxper =.08
tax = round(float(amount) * taxper,2)
total = tax + float(amount)

output = """
The tax is ${0}.
The total is ${1}.
"""
print(output.format(tax,total))