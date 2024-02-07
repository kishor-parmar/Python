import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["blog"]
mycol = mydb["customers"]

# Delete the first record that matches query
myquery = {"address": "Mountain 21"}

mycol.delete_one(myquery)

# Delete all records that begin "S"
myquery = {"address": {"$regex": "^S"}}

x = mycol.delete_many(myquery)

print(x.deleted_count, " documents deleted.")
