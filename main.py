import pymongo
import requests

from pprint import pprint

client = pymongo.MongoClient()

db = client['starwars']
#
# luke = db.characters.find_one({"name": "Luke Skywalker"})

ship_coll = db["starships"]

ships = requests.get("https://swapi.dev/api/starships/?page=1")

ships_data = ships.json()

# pprint(ships_data)
page = 0
ship_number = 0




# this loops through all the ship data and only ends if there is no data left
doing = True
while doing != False :
    # pprint(ships_data)

    # this tracts and at the end show how many pages were scraped
    page += 1

    ships = requests.get(f"https://swapi.dev/api/starships/?page={page}")


    ships_data = ships.json()
    print("##########################################################################################")
    print(f"PAGE {page}")
    # pprint(ships_data)


    # this loops through the data of each ship
    for ship in ships_data["results"]:

        print("SHIP ####################################")
        pprint(ship["name"])
        ship_number += 1 # this tracks how many ships have been read
        pilots_id_list = [] # this is list for pilot ids to replace the list of pilot APIs

        # loops through each pilot API if there is more than one
        for pilot in ship["pilots"]:
            print("PILOT ####################################")
            # print(pilot)

            # This is make pilot API call to get the pilot data and store in pd
            pilot_data = requests.get(pilot)
            pd = pilot_data.json()


            pilot_name = pd["name"] # extracts pilot name

            # this gets pilot id from DB that matches pilot name from pilot API
            pilot_id = db.characters.find_one({"name": pilot_name},{"_id"})


            print("         pilot ", pilot_name, " ", pilot_id )
            # ship["pilots"] = ship["pilots":[].append(pilot_id)]

            # if ship does have pilots, add pilot ID to the list of pilot IDs for this ship
            if pilot:
                pilots_id_list.append(pilot_id)

        ship["pilots"] = pilots_id_list # this replaces the list of pilot API with the list of pilot ID
        ship_coll.insert_one(ship)


    print(f"There are {ship_number} ships")





    # this ends the loop if there is not more data left
    if  ships_data["next"] == None :
        break


# this displaces ship data set with pilot API replace with the pilot IDs
pprint(ships_data)



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


