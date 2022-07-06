import pymongo
import requests

from pprint import pprint

client = pymongo.MongoClient()

# db = client['starwars']
#
# luke = db.characters.find_one({"name": "Luke Skywalker"})


ships = requests.get("https://swapi.dev/api/starships/?page=1")

ships_data = ships.json()

# pprint(ships_data)
page = 1
ship_number = 0

while ships_data["count"] :
    # pprint(ships_data)

    page += 1

    ships = requests.get(f"https://swapi.dev/api/starships/?page={page}")


    ships_data = ships.json()
    print("##########################################################################################")
    print(f"PAGE {page}")
    # pprint(ships_data)
    ship_number = 0
    for ship in ships_data["results"]:
        print("SHIP ####################################")
        pprint(ship["name"])
        ship_number += 1
        for pilot in ship["pilots"]:
            print("PILOT ####################################")
            # print(pilot)
            pilot_data = requests.get(pilot)
            pd = pilot_data.json()
            pprint(pd["name"])
    print(f"There are {ship_number} ships")









# ship_number = 0
# for ship in ships_data["results"]:
#     print("SHIP ####################################")
#     pprint(ship["name"])
#     ship_number += 1
#     for pilot in ship["pilots"]:
#         print("PILOT ####################################")
#         # print(pilot)
#         pilot_data = requests.get(pilot)
#         pd = pilot_data.json()
#         pprint(pd["name"])
# print(f"There are {ship_number} ships")











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


