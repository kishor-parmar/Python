import json

person = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "hasChildren": False,
    "titles": ["engineer", "programmer"],
}

# convert into JSON:
person_json = json.dumps(person)
# use different formatting style
person_json2 = json.dumps(person, indent=4, separators=("; ", "= "), sort_keys=True)

# the result is a JSON string:
print(person_json)
print()
print(person_json2)

print()
person = json.loads(person_json)
print(person)
print()

# Write to a file
with open("person.json", "w") as outfile:
    json.dump(person, outfile, indent=4)  # you can also specify indent etc...


# Read from file
with open("person.json", "r") as infile:
    person = json.load(infile)
print(person)
print()


# Encoder
from json import JSONEncoder


class User:

    def __init__(self, name, age):
        self.name = name
        self.age = age


user = User("Kish", 60)


class UserEncoder(JSONEncoder):

    def default(self, o):
        if isinstance(o, User):
            return {"name": o.name, "age": o.age, o.__class__.__name__: True}
        return JSONEncoder.default(self, 0)


userJSON = UserEncoder().encode(user)
print(userJSON)
user = json.loads(userJSON)
print(user)
print()


# Decoder
def decode_user(dct):
    if User.__name__ in dct:
        return User(name=dct["name"], age=dct["age"])
    return dct


user = json.loads(userJSON, object_hook=decode_user)
print(user.name, user.age)
