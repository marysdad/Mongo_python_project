import pymongo
import requests

from pprint import pprint

client = pymongo.MongoClient()

db = client['starwars']


#test
def db_setup():

    ships = requests.get("https://swapi.dev/api/starships/?page=1")
    return ships.json()


#test
# this adds the updated ship record with the pilot ID in the mongo ships collection
def insert_ships_collections(ship):

    ship_coll = db["starships"]
    ship_coll.insert_one(ship)

#test
def ships_api_call_back(api):
    ships = requests.get(api)
    return ships.json()

#test
def get_pilot_name(pilot):
    # This is make pilot API call to get the pilot data and store in pd
    pilot_data = requests.get(pilot)
    pd = pilot_data.json()

    return pd["name"]  # extracts pilot name



def replace_pilotAPI_with_pilotID(ship,db):
    pilots_id_list = []  # this is list for pilot ids to replace the list of pilot APIs

    for pilot in ship["pilots"]:

        print("PILOT ####################################")
        # print(pilot)

        pilot_name = get_pilot_name(pilot)

        # this gets pilot id from DB that matches pilot name from pilot API
        pilot_id = db.characters.find_one({"name": pilot_name}, {"_id":1})

        print("         pilot ", pilot_name, " ", pilot_id)

        # if ship does have pilots, add pilot ID to the list of pilot IDs for this ship
        # if len(pilot) != 0:
        pilots_id_list.append(pilot_id['_id'])

    ship["pilots"] = pilots_id_list  # this replaces the list of pilot API with the list of pilot ID
        # print("line 58 ",ship)
    insert_ships_collections(ship)