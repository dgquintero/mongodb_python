import os
import pprint

from pymongo import MongoClient

from bson.objectid import ObjectId

MONGODB_URI = os.getenv("MONGODB_URI")

client = MongoClient(MONGODB_URI)

db = client.bank

accounts_collection = db.accounts

select_by_balance = {"$match": {"balance": {"$lt": 100000000000000}}}

separate_by_account_calculate_avg_valance = {
    "$group": { "_id": "$account_type", "average_balance": {"$avg": "$balance"}}
}


pipeline = [select_by_balance, separate_by_account_calculate_avg_valance]

result = accounts_collection.aggregate(pipeline)

print()
print("Average balance per account type:")

for doc in result:
    pprint.pprint(doc)

client.close()
