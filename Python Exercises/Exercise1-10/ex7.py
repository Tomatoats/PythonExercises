conversion_ft_to_m = 0.09290304

length = input("What is the length of the house in feet? ")
width = input ("What is the length of the house in meters? ")

print("You entered dimensions of {0} by {1} feet".format(length, width))
area = int(length) * int(width)
converted = area * conversion_ft_to_m
output = """
The area is 
{0} square feet
{1} square meters
"""
#output.format(str(area), str(converted))15
print(output.format(str(area), str(converted)))

