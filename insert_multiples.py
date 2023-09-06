import datetime
import os

from pymongo import MongoClient

MONGODB_URI = os.getenv("MONGODB_URI")

client = MongoClient(MONGODB_URI)

db = client.bank

accounts_collection = db.accounts

new_accounts = [{
  "account_holder": "Daniel Quintero Ocampo",
  "account_id": "123",
  "account_type": "checking",
  "balance": 12000000
},
{
  "account_holder": "Maria gomez",
  "account_id": "123345",
  "account_type": "checking",
  "balance": 120022344
}
]

# Create a new account
result = accounts_collection.insert_many(new_accounts)

document_id = result.inserted_ids

print("# of accounts created: " + str(len(document_id)))
print(f"_ids of inserted documents: {document_id}")

client.close()
