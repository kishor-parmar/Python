import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["blog"]
mycol = mydb["customers"]

# print one record
x = mycol.find_one()
print(x)
print()

# print all records
for x in mycol.find():
    print(x)
print()

# print specific fields from records
for x in mycol.find({}, {"_id": 0, "name": 1, "address": 1}):
    print(x)
print()

# print all fields except one from records
for x in mycol.find({}, {"address": 0}):
    print(x)
print()
