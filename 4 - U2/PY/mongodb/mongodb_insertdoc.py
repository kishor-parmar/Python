# brew services start mongodb-community@7.0
#
# brew services stop mongodb-community@7.0

import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["blog"]
mycol = mydb["customers"]

mydict = {"name": "Peter", "address": "Lowstreet 27"}

x = mycol.insert_one(mydict)

print(x)

print(x.inserted_id)
