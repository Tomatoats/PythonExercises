import random

def password(length,special,numbers):
    spec = ["!","@","#","$","%","^","&","*","(",")","_","-","+","=","?","{","}"]
    numb = ["1","2","3","4","5","6","7","8","9","0"]
    let  = ["q","w","e","r","t","y","u","i","o","p","l","k","j","h","g","f","d","s","a","m","n","b","v","c","x","z"]
    passlength = random.randint(length, (length+4))
    lenleft = passlength - special - numbers
    passw = []
    for x in range(special):
        passw.append(random.choice(spec))
    for x in range(numbers):
        passw.append(random.choice(numb))
    for x in range(lenleft):
        passw.append(random.choice(let))
        random.shuffle(passw)
        
    return passw
        
        



length = int(input("What's the minimum length? "))
special = int(input("How many special characters? "))
numbers = int(input("How many numbers? "))



passw = password(length,special,numbers)
actual = "".join(str(x) for x in passw)
print("Your password is",actual)