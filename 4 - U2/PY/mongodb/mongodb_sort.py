# brew services start mongodb-community@7.0
#
# brew services stop mongodb-community@7.0

import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["blog"]
mycol = mydb["customers"]

# Sort all documents by name -1 = decending, 1 = ascending (default)
mydoc = mycol.find().sort("name", -1)

for x in mydoc:
    print(x)
print()
