from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.gp8u6ok.mongodb.net/test"
client = MongoClient(url)
db = client.pytech
print("-- Pytech Collection List --")
print(db.list_collection_names())