import random

def validateDiff():
    flag = False
    while flag == False:
        diff = input("Enter the difficulty Level - 1, 2, or 3!")
        try:
            int(diff)
        except ValueError:
            print("Please give me only a number, 1, 2, or 3")
            continue
        if int(diff) > 3 or int(diff) < 1:
            print("Please only give me the number 1, 2, or 3 for difficulty")
        else:
            flag = True
            return diff

def game(diff):
    match diff:
        case 1: number = random.randint(1,10)
        case 2: number = random.randint(1,100)
        case 3: number = random.randint(1,1000)
    flag = False
    count = 0
    output = "" 
    guess = input("I have my number, What's your guess? ")
    try:
        int(guess)
    except ValueError:
        output = "Not a number. Guess again!"
    else:
        if int(guess) < number:
            output = "Too low. Try again!"
        elif int(guess) > number:
            output = "Too High. Try again!"
        else:
            output = "Wooo! You got it!"
            flag = True
    count = count + 1
    while flag == False:
        guess = input(output)
        try:
            int(guess)
        except ValueError:
            output = "Not a number. Guess again!"
        else:
            if int(guess) < number:
                output = "Too low. Try again!"
            elif int(guess) > number:
                output = "Too High. Try again!"
            else:
                output = "Wooo! You got it!"
                flag = True
        count = count+1
    print("You got it in {0} guesses!".format(count))


def validateEnd():
    flag = False
    while flag == False:
        answer = input("Do you want to play another game? (y/n) ")
        if answer.lower() == "y":
            return False
        elif answer.lower() == "n":
            return True
        else:
            print("Please only use 'y' or 'n'.")



print("Let's play Guess the number!")
MatchEnd = False
RoundEnd = False

while MatchEnd == False:
    print("1: 1-10. 2: 1-100.  3: 1-1000")

    diff = validateDiff()

    game(int(diff))

    MatchEnd = validateEnd()
