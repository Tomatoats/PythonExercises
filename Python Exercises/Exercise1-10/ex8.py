people = input("How many people? ")
pizza = input("How many pizzas? ")
slices = input("how many slices? ")

total = int(pizza) * int(slices)
sliceper = total // int(people)
remainder = total % int(people)
output = """
Each person gets {0} pieces of pizza.
There are {1} leftover places
"""
print(output.format(str(sliceper), str(remainder)))