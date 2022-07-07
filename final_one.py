import pymongo
import definitions

from pprint import pprint

client = pymongo.MongoClient()

db = client['starwars']


def insert_ships_collections(ship):
    ship_coll = db["starships"]
    ship_coll.insert_one(ship)

# this is star ships collection for the db that I will populate near the end of the code.

ships_data = definitions.db_setup()


# this adds the updated ship record with the pilot ID in the mongo ships collection


# pprint(ships_data)
page = 0
ship_number = 0

# this loops through all the ship data and only ends if there is no data left
doing = True
while doing != False :
    # pprint(ships_data)

    # this tracts and at the end show how many pages were scraped
    page += 1


    ships_data = definitions.ships_api_call_back(f"https://swapi.dev/api/starships/?page={page}")

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


        definitions.replace_pilotAPI_with_pilotID(ship,db)

    print(f"There are {ship_number} ships")





    # this ends the loop if there is not more data left
    if  ships_data["next"] == None :
        break


# this displaces ship data set with pilot API replace with the pilot IDs
pprint(ships_data)


