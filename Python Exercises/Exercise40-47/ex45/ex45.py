name= input("What would you like to name the output file? ")
start = "Exercise40-50\ex45\\"
out = start + name +".txt"

filein = open("Exercise40-50\ex45\ex45_in.txt","r")
names = filein.read()
filein.close()
newNames = names.replace("utilize","use")

fileout = open(out,"w+")
fileout.write(newNames)