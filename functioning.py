import pymongo
import requests

from pprint import pprint

client = pymongo.MongoClient()

db = client['starwars']
#

# this is star ships collection for the db that I will populate near the end of the code.

def db_setup():

    ships = requests.get("https://swapi.dev/api/starships/?page=1")
    return ships.json()

ships_data = db_setup()


# this adds the updated ship record with the pilot ID in the mongo ships collection
def insert_ships_collections(ship):

    ship_coll = db["starships"]
    ship_coll.insert_one(ship)

# pprint(ships_data)
page = 0
ship_number = 0


def ships_api_call_back(api):
    ships = requests.get(api)
    return ships.json()

def get_pilot_name(pilot):
    # This is make pilot API call to get the pilot data and store in pd
    pilot_data = requests.get(pilot)
    pd = pilot_data.json()

    return pd["name"]  # extracts pilot name



def replace_pilotAPI_with_pilotID(ship):

    for pilot in ship["pilots"]:
        print("PILOT ####################################")
        # print(pilot)

        pilot_name = get_pilot_name(pilot)

        # this gets pilot id from DB that matches pilot name from pilot API
        pilot_id = db.characters.find_one({"name": pilot_name}, {"_id"})

        print("         pilot ", pilot_name, " ", pilot_id)

        # if ship does have pilots, add pilot ID to the list of pilot IDs for this ship
        if pilot:
            pilots_id_list.append(pilot_id)

    ship["pilots"] = pilots_id_list  # this replaces the list of pilot API with the list of pilot ID
    insert_ships_collections(ship)



# this loops through all the ship data and only ends if there is no data left
doing = True
while doing != False :
    # pprint(ships_data)

    # this tracts and at the end show how many pages were scraped
    page += 1


    ships_data = ships_api_call_back(f"https://swapi.dev/api/starships/?page={page}")

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


        replace_pilotAPI_with_pilotID(ship)

    print(f"There are {ship_number} ships")





    # this ends the loop if there is not more data left
    if  ships_data["next"] == None :
        break


# this displaces ship data set with pilot API replace with the pilot IDs
pprint(ships_data)


