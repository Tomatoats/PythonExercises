import random

def answer(number):
    output = ""
    match number:
        case 1: output = "Yes"
        case 2: output = "No"
        case 3: output = "Maybe"
        case 4: output = "Ask again later"
    return output

number = random.randint(1,4)

question = input("What's your question? ")

print(answer(number))

