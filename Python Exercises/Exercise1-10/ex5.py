x = input("What is the first number? ")
y = input("What's the second number? ")
# Lets hope these auto convert
ix = int(x)
iy = int(y)
sum = ix+iy
minus = ix-iy
divide = ix/iy
mult = ix*iy

line1 = x +  " + "  + y + " = " + str(sum)
line2 = x + " - " + y + " = " + str(minus)
line3 = x + " / " + y + " = " + str(divide)
line4 = x + " * " + y + " = " + str(mult)
output =  line1 + "\n" + line2 + "\n" + line3 + "\n" + line4 + "\n"
# THere's gotta be a better way!

print(output)