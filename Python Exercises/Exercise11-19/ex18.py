determine = input("Are you in celcius or in feirenheit?")
inputdegree = input("And what temperature is it?")
if "c" in determine.lower():
    ratio = (9/5)
    degree = "feirenheit"
    answer = (float(inputdegree) * ratio) + 32
else:
    ratio = (5/9)
    degree = "celcius"
    answer = (float(inputdegree) -32) * ratio
output = """
The temperature in {0} is {1} degrees.
"""
print(output.format(degree,answer))
