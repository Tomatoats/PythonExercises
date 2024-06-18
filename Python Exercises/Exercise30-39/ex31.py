from prettytable import PrettyTable

def validateAge():
    flag = False
    while flag == False:
        try:
            age = input("What is your age? ")
            int(age)
        except ValueError:
            print("Please give me your age in whole numbers. ")
            continue
        else:
            flag = True
            return age

def validatePulse():
    flag = False
    while flag == False:
        try:
            pulse = input("What is your resting pulse? ")
            int(pulse)
        except ValueError:
            print("Please give me your pulse in whole numbers. ")
            continue
        else:
            flag = True
            return pulse

age = validateAge()
RestPulse = validatePulse()

pulseList = []
intensityList = []
intensity = .55
for i in range(9):
    targetRate = round(((((220 -int(age)) -int(RestPulse)) * intensity) + int(RestPulse)))
    intensityList.append(intensity)
    pulseList.append(targetRate)
    intensity = round(intensity + .05,2)

print(intensityList)
print(pulseList)
#TODO: Make a nice tabular list to show 