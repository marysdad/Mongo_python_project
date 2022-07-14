import pymongo

client = pymongo.MongoClient("mongodb://3.67.168.9:27107")

db = client["DummyDataBase"]

db.create_collection("Towns")