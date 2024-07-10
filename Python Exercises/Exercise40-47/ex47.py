import requests
from prettytable import PrettyTable

def getAstronauts():
    url = f"http://api.open-notify.org/astros.json"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        thePeeps = data['people']
        return thePeeps
    else:
        return None
    
def build(peoples,crafts):
    table = PrettyTable()
    table.add_column("Name",peoples)
    table.add_column("Craft",crafts)
    amount = len(peoples)
    print("There are ", amount, " people in space right now.\n")
    print(table)



thePeeps = getAstronauts()
count = 0
peoples = []
crafts = []
for x in thePeeps:
    peoples.append(thePeeps[count]['name'])
    crafts.append(thePeeps[count]['craft'])
    count += 1
    
build(peoples,crafts)
