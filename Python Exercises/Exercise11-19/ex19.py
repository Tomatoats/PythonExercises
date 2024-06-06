flag = False
while flag == False:
    weight, height = input("Yo how much you weigh and how tall are ya(inch), sep by comma. ").split(',')
    try:
        int(weight)
        int(height)
    except ValueError:
        print("ayo mate i need numbers for weight and height.")
    
    else:
        flag = True
bmi = round((int(weight) / (int(height) * int(height))) * 703,1)
output = """
Your BMI is {0}
{1}
"""
print(output.format(bmi, "You are within the ideal weight range." if (bmi <25)else "You are overweight. You should see your doctor."))