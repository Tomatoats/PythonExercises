weight,alc,gender,hours = input("Input your weight, alc consumed in ounces, your gender, and hours since last drink! seperated by comma ").split(",",4)
ratio = 0.66
if "man" in gender:
    ratio = 0.73
BAC = str((float(alc) * 5.14) / (float(weight) * float(ratio)) - (0.15 * int(hours)))
output = """
Your BAC is {0}
It is {1} for you to drive
"""
print(output.format(BAC, "not legal" if (float(BAC) >= 0.08) else "legal"))