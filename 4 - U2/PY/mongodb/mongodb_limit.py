# brew services start mongodb-community@7.0
#
# brew services stop mongodb-community@7.0

import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["blog"]
mycol = mydb["customers"]

myresult = mycol.find().limit(5)

# print the result:
for x in myresult:
    print(x)
