# brew services start mongodb-community@7.0
#
# brew services stop mongodb-community@7.0

import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

print()
print(f"Databases = {myclient.list_database_names()}")

mydb = myclient["blog"]

mycol = mydb["posts"]

print()
print(f"Collections in database '{mydb.name}' = {mydb.list_collection_names()} ")
print()
