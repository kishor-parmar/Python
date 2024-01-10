# Json

import json

person = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "hasChildren": False,
    "titles": ["engineer", "programmer"],
}

print("*** Dictionary ***")
print(person)
print()

# Convert Dictionary into JSON
print("*** Convert Dictionary to Json ***")

person_json = json.dumps(person)
print(person_json)
print()

# Use different formatting style
print("*** Use different formatting style ***")
person_json2 = json.dumps(person, indent=4, sort_keys=True)
print(person_json2)
print()

# Write Json Document to a file
print("*** Write Json Document to a file ***")

with open("person.json", "w") as json_file:
    json.dump(person, json_file, indent=4)
print()

# Convert Json to a python object
print("*** Convert Json to a python object ***")

print(person_json)
print()

person = json.loads(person_json)
print(person)
print()

# Convert Json to a python object and write back to a file
print("*** Convert Json to a python object and write back to a file ***")

print(person_json)
print()

with open("person.json", "r") as json_file:
    person = json.load(json_file)
    print(person)
print()

# Converting Objects to Json
print("*** Converting Objects to Json ***")


class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age


user = User("Kish", 65)


def encode_user(o):
    if isinstance(o, User):
        return {"name": o.name, "age": o.age, o.__class__.__name__: True}
    else:
        raise TypeError("Object of type User is not JSON serializable")


user_json = json.dumps(user, default=encode_user)
print(user_json)
print()

# Custom Json encoder
print("*** Custom Json encoder ***")

from json import JSONEncoder


class UserEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, User):
            return {"name": o.name, "age": o.age, o.__class__.__name__: True}
        return JSONEncoder.default(self, o)


user_json = json.dumps(user, cls=UserEncoder)
print(user_json)
print()

# Use the encoder directly
print("*** Use the encoder directly ***")

from json import JSONEncoder


class UserEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, User):
            return {"name": o.name, "age": o.age, o.__class__.__name__: True}
        return JSONEncoder.default(self, o)


user = User("Jason", 25)
user_json = UserEncoder().encode(user)
print(user_json)
print()


# Decode the Json back to an object
print("*** Decode the Json back to an object ***")

user = json.loads(user_json)
print(user)
print(type(user))
print()


def decode_user(dict):
    if User.__name__ in dict:
        return User(name=dict["name"], age=dict["age"])
    return dict


user = json.loads(user_json, object_hook=decode_user)
print(user.name)
print(user.age)
print(type(user))
print()
