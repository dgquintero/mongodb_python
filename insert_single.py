import datetime
import os

from pymongo import MongoClient

MONGODB_URI = os.getenv("MONGODB_URI")

client = MongoClient(MONGODB_URI)

db = client.bank

accounts_collection = db.accounts

new_account = {
  "account_holder": "Daniel Quintero",
  "account_id": "123",
  "account_type": "checking",
  "balance": 12000000,
  "last_update": datetime.datetime.utcnow()
}

# Create a new account
result = accounts_collection.insert_one(new_account)

document_id = result.inserted_id

print(document_id)

client.close()

