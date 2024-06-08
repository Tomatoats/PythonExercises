answer = input("Is the Car silent when you turn the key? ")
if "y" in answer.lower():
    answer = input("Are the battery terminals corroded? ")
    if "y" in answer.lower():
        print("Clean terminals and try starting again.")
    else:
        print("Replace cables and try again.")
else:
    answer = input("Does the car make a slicking noise? ")
    if "y" in answer.lower():
        print("replace the battery. ")
    else:
        answer = input("Does the car crank up but fail to start? ")
        if "y" in answer.lower():
            print("Check Spark Plug Connections ")
        else:
            answer = input("Does the engine start and then die? ")
            if "y" in answer.lower():
                answer = input("Does your car have fuel injection? ") 
                if "y" in answer.lower():
                    print("Get it in for service. ")
                else:
                    print("Check to ensure the choke is opening and closing. ")
            else:
                print("This should not be possible. ")
