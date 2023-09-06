import os
import pprint

from pymongo import MongoClient

from bson.objectid import ObjectId

MONGODB_URI = os.getenv("MONGODB_URI")

client = MongoClient(MONGODB_URI)

db = client.bank

accounts_collection = db.accounts

# Find a single document
document_to_search = {"_id": ObjectId("64f7a6927bc128563fe39718")}

# update balance
new_balance = {"$inc": {"balance": 100}}

# print original document
pprint.pprint(accounts_collection.find_one(document_to_search))

# update document
result = accounts_collection.update_one(document_to_search, new_balance)


print("Dcuments updated: " + str(result.modified_count))

# print updated document
pprint.pprint(accounts_collection.find_one(document_to_search))

client.close()
