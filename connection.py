import os
from pymongo import MongoClient

MONGODB_URI = os.getenv("MONGODB_URI")

client = MongoClient(MONGODB_URI)

for db_name in client.list_database_names():
    print(db_name)
