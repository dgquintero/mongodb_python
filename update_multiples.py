import os
import pprint

from pymongo import MongoClient

from bson.objectid import ObjectId

MONGODB_URI = os.getenv("MONGODB_URI")

client = MongoClient(MONGODB_URI)

db = client.bank

accounts_collection = db.accounts

# filter
select_accounts = {"account_type": "checking"}

# update
set_field = {"$set": {"minimum_balance": 100}}

result = accounts_collection.update_many(select_accounts, set_field)

print("Documents matched: " + str(result.matched_count))
print("Documents updated: " + str(result.modified_count))


# print updated document
pprint.pprint(accounts_collection.find_one(select_accounts))

client.close()
