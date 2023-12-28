
people = [
    {"name" : "Harry", "house" : "Chestnut"},
    {"name" : "John", "house" : "Meadway"},
    {"name" : "Mark", "house" : "Abbeydale"}
]

people.sort(key=lambda person: person["name"])

print(people)

people.sort(key=lambda person: person["house"])
print(people)
