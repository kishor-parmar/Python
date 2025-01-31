# Import the Surreal class
from surrealdb import Surreal


db = Surreal("https://cloud.surrealdb.com")

# Create a record with a random ID
person = db.create("person")


db.close
