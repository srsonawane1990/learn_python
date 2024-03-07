import json
import requests 
person_ISS = []
person_Tiangong = []
def space_data(url):
    data = requests.get(url)
    #print(data.json())
    dump = data.json()
    for person in dump["people"]:
        print(person["craft"])
        if(person["craft"] == "ISS"):
            person_ISS.append(person["name"])
        else:
            person_Tiangong.append(person["name"])
    
    print(person_ISS)
    print(person_Tiangong)
    print("Total no of persons in ISS " + str(len(person_ISS)))
    print("Total no of persons in Tiangong " + str(len(person_Tiangong)))

space_data("http://api.open-notify.org/astros.json")
