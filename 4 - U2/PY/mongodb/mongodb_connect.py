# brew services start mongodb-community@7.0
#
# brew services stop mongodb-community@7.0

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

# Replace the placeholder with your Atlas connection string
# 17.0.0.1
uri = "localhost:27017"

# Set the Stable API version when creating a new client
client = MongoClient(uri, server_api=ServerApi("1"))

# Send a ping to confirm a successful connection
try:
    client.admin.command("ping")
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
