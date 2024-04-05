user = "hall"
password = "oats"
givenuser = input("What's your username? ")
givenpass = input("What's your password? ")

if givenuser in user:
    if givenpass in password:
        print("Welcome!\n")
    else:
        print("I don't know you!\n")
else:
    print("I don't know you!\n")
