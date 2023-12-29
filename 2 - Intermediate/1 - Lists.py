# Lists: ordered, mutable, allows duplicate elements
mylist = ["banana", "cheery", "apple"]
print(mylist)

# Create an empty List
mylist2 = list()
print(mylist2)

# Lists can contain integers, Booleans, strings and Allows Duplicates
mylist2 = [5, True, "apple", "apple"]
print(mylist2)

# Accessing elements
mylist = ["banana", "cheery", "apple"]

item = mylist[0]
print(item)

# Accessing the last element in list
print("*** Accessing the last element in list ***")
item = mylist[-1]
print(item)
print()

# Accessing each element in list
print("*** Accessing all elements in list ***")
for i in mylist:
    print(i)
print()

# Locate element in list
print("*** Locate element in list ***")
if "banana" in mylist:
    print("yes")
else:
    print("no")
print()

# Number of elements in list
print("*** Number of elements in list ***")
print(len(mylist))
print()

# Appending to list
mylist = ["banana", "cherry", "apple"]
print(mylist)
print()

# Append new element to end
print("*** Append new element to end ***")
mylist.append("lemon")
print(mylist)
print()

# Insert element in index 1
print("*** Insert element in index 1 ***")
mylist.insert(1, "blueberry")
print(mylist)
print()

# Remove last element
print("*** Remove last element ***")
item = mylist.pop()
print(item)
print(mylist)
print()

# Remove a specific element
print("*** Remove specific element ***")
item = mylist.remove("cherry")
print(item)
print(mylist)
print()

# Reverse the list
print("*** Reverse the list ***")
print(mylist)
item = mylist.reverse()
print(mylist)
print()

# Sort the list
print("*** Sort the list ***")
print(mylist)
item = mylist.sort()
print(mylist)
print()

mylist = [4, 3, 1, -1, -5, 10]
print(mylist)
item = mylist.sort()
print(mylist)
print()

# Sort into new list
print("*** Sort into new list ***")
mylist = [4, 3, 1, -1, -5, 10]
new_list = sorted(mylist)
print(mylist)
print(new_list)
print()

# Create new list with same values in each element
print("*** Create new list with same values in each element ***")
mylist = [0] * 5
print(mylist)
print()

# Concatenate 2 lists
print("*** Concatenate 2 lists ***")
mylist2 = [1, 2, 3, 4, 5]
newlist = mylist + mylist2
print(mylist2)
print(newlist)
print()

# Slicing
print("*** Slicing ***")
mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
a = mylist[1:5]
print(mylist)
print(a)
print()

a = mylist[1:5:2]
print(mylist)
print(a)
print()

a = mylist[::-1]
print(mylist)
print(a)
print()

# Copying Lists
print("*** Copying Lists ***")
list_org = ["banana", "cherry", "apple"]
list_cpy = list_org
list_cpy.append("lemon")
print(list_org)
print(list_cpy)
print()

list_org = ["banana", "cherry", "apple"]
list_cpy = list_org.copy()
list_cpy.append("lemon")
print(list_org)
print(list_cpy)
print()

# Creating list with an expression
print("*** Creating list with an expression ***")
mylist = [1, 2, 3, 4, 5]
x = [i * i for i in mylist]
print(mylist)
print(x)
