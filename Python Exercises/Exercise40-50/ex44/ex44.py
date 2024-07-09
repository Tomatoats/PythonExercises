import json

with open("Exercise40-50\ex44\ex44_in.JSON") as json_file:
    data = json.load(json_file)
print(data)

flag = False
products = data['products']
#print(products['name'])\
count = 0
while flag != True:
    count = 0
    item = input("What is the product Name? ")
    for x in products:
        if products[count]["name"] == item:
            print("Name: ",products[count]["name"],"\nPrice: ",products[count]["price"],"\nQuantity: ",products[count]["quantity"])
            flag = True
        count += 1
    if flag != True:
        print("Sorry, we don't have that Item.")