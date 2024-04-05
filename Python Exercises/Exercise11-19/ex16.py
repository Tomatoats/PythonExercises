age = input("What is your age? ")
limit = 16
output ="You are {0} enough to drive."
print(output.format("old" if int(age) >= limit else "not old"))
