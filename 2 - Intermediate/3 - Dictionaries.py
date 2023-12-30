# Dictionary: Key-Value pairs, Unordered, Mutable

# Creating a dictionary
print("*** Creating a dictionary ***")

mydict = {"name": "Max", "age": 28, "city": "New York"}
print(mydict)
print()

mydict2 = dict(name="Mary", age=27, city="Boston")
print(mydict2)
print()

# Accessing value
print("*** Accessing value ***")

value = mydict["name"]
print(value)
print()

# Adding items
print("*** Adding items ***")

mydict["email"] = "kp@123.com"
print(mydict)
print()

# Updating items
print("*** Updating items ***")

mydict["email"] = "joe@abc.com"
print(mydict)
print()

# Deleting items
print("*** Deleting items ***")

del mydict["name"]
print(mydict)

mydict.pop("age")
print(mydict)
print()

# Locate key in dictionary
print("*** Locate key in dictionary ***")

if "city" in mydict:
    print(mydict["city"])
print()

try:
    print(mydict["city1"])
except:
    print("Error")
print()

# Accessing each key in Dictionary
print("*** Accessing each key in Dictionary ***")

for key in mydict:
    print(key, ":", mydict[key])
print()

for key, value in mydict.items():
    print(key, value)
print()

# Copying a dictionary
print("*** Copying a dictionary ***")

mydict_cpy = mydict.copy()
mydict_cpy["name"] = "Joe"
print(mydict)
print(mydict_cpy)
print()

mydict_cpy = dict(mydict)
mydict_cpy["name"] = "Joe"
print(mydict)
print(mydict_cpy)
print()

# Merging dictionaries
print("*** Merging dictionaries ***")

my_dict = {"name": "Max", "age": 28, "email": "max@xyz.com"}
my_dict2 = dict(name="Mary", age=27, city="Boston")
print(my_dict)
print(my_dict2)
my_dict.update(my_dict2)
print(my_dict)
print()

# Using numbers as keys
print("*** Using numbers as keys ***")

mydict = {2: 9, 6: 36, 9: 81}
print(mydict)

value = mydict[6]
print(value)
print()
