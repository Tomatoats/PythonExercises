def yoink(inFile):
    filein = open(inFile,"r")
    tostring = filein.read()
    return tostring

def count(given):
    counted = dict()
    words = given.split(" ")
    words.sort()
    count = 0
    for x in words:
        if x in counted:
            count += 1 
            counted.update({x:count})
        else:
            count = 1
            counted.update({x:count})
    countedD = {key: value for key, value in sorted(counted.items(),key = lambda item: item[1],reverse=True)} # in order to get sorted by highest value
    #sorted(counted, key = counted.get, reverse= False) #in order to get a sorted dictionary by key
    #sorted(counted.items(), key=lambda x: x[1], reverse=True)
    return countedD


def clean(given):
    cleaning = given.replace(",","")
    cleaned = cleaning.replace("\n"," ")
    squeaky = cleaned.lower()
    return squeaky

def printAsterisk(counted):
    for x,y in counted.items():
        output = x + ": " + "*"*y
        print(output)
        

givenInput = yoink("Exercise40-50\ex46\ex46_in.txt")
cleanerinput = clean(givenInput)
counted = count(cleanerinput)
printAsterisk(counted)

