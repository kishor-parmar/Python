# brew services start mongodb-community@7.0
#
# brew services stop mongodb-community@7.0

import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

mycol.drop()
