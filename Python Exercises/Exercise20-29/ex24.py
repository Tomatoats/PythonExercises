first = input("Enter two strings and i'll tell you if they are anagrams:\nEnter the first string: ")
second = input("Enter the second string: ")
strings = [first,second]
def setup(strin):
    strin = strin.lower()
    strin = strin.replace(" ","")
    sorte = sorted(strin)
    tostrin = ''.join(sorte)
    print(tostrin)
    return tostrin

def isAnagram(s1,s2):
    output = "{0} and {1}"
    print(output.format(s1,s2))
    if len(s1) != len(s2):
        print("This is not an anagram!")
    else:
        if s1 == s2:
            print ("this is an anagram!")
        else:
            print("This is not an anagram!")
count = 0
for x in strings:
    strings[count] = setup(x)
    count = count+1
isAnagram(strings[0],strings[1])