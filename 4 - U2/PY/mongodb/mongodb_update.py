# brew services start mongodb-community@7.0
#
# brew services stop mongodb-community@7.0

import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["blog"]
mycol = mydb["customers"]

# Change the address from "Valley 345" to "Canyon 123"
# First instance only
myquery = {"address": "Valley 345"}
newvalues = {"$set": {"address": "Canyon 123"}}

mycol.update_one(myquery, newvalues)

# print "customers" after the update:
for x in mycol.find():
    print(x)
print()

# Update all documents where the address starts with the letter "S"
myquery = {"address": {"$regex": "^S"}}
newvalues = {"$set": {"name": "Minnie"}}

x = mycol.update_many(myquery, newvalues)

print(x.modified_count, "documents updated.")
print()
