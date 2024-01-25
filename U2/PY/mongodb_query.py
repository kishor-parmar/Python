import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["blog"]
mycol = mydb["customers"]

# find documents with address Park Lane 38
myquery = {"address": "Park Lane 38"}

mydoc = mycol.find(myquery)

for x in mydoc:
    print(x)
print()

# Find documents where the address starts with the letter "S" or higher:
myquery = {"address": {"$gt": "S"}}

mydoc = mycol.find(myquery)

for x in mydoc:
    print(x)
print()

# Find documents where address starts with S usin regex
myquery = {"address": {"$regex": "^S"}}

mydoc = mycol.find(myquery)

for x in mydoc:
    print(x)
print()
