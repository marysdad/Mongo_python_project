import pymongo
import requests

from pprint import pprint

client = pymongo.MongoClient()

db = client['starwars']

luke = db.characters.find_one({"name": "Luke Skywalker"})


ships = requests.get("https://swapi.dev/api/starships/?page=2")

ships_data = ships.json()

for ship in ships_data["results"]:
    print("SHIP ####################################")
    pprint(ship["name"])
    for pilot in ship["pilots"]:
        print("PILOT ####################################")
        # print(pilot)
        pilot_data = requests.get(pilot)
        pd = pilot_data.json()
        pprint(pd["name"])











    # pprint(ship["pilots"])
    # pilot_data = requests.get(ship["pilots"][0])
    # pd = pilot_data.json()
    # pprint(pd)











# pprint(luke)

# droids = db.characters.find({"species.name":"Droid"})

# print(droids)

# for droid in droids:
#     print(droid)

# who = db.characters.find_one({"name":"Darth Vader"},{"name":1,"height":1,"_id":0})
#
# print(who)
#
# yellow = db.characters.find({"eye_color": "yellow"},{"name"})
#
# print(yellow)


