# Sets: unordered, mutable, no duplicates

# Creating a Set
print("*** Creating a set ***")

myset = {
    1,
    2,
    3,
}
print(myset)

myset = set([1, 2, 3])
print(myset)

myset = set("Hello")
print(myset)
print()

# Adding elements to a set
print("*** Adding items to a set ***")

myset = set()
myset.add(1)
myset.add(2)
myset.add(3)
print(myset)
print()

# Removing elements
print("*** Removing elements ***")
myset.remove(3)
print(myset)

myset.discard(99)
print(myset)
print()

# Emptying a set
print("*** Emptying a set ***")

myset.clear()
print(myset)
print()

# Removing an arbitrary element from the set
print("*** Removing an arbitrary element from the set ***")

myset = set()
myset.add(1)
myset.add(2)
myset.add(3)

print(myset.pop())
print(myset)
print()

# Accessing each element in set
print("*** Accessing all elements in set ***")

for i in myset:
    print(i)
print()

# Locate element in set
print("*** Locate element in set ***")

if 2 in myset:
    print("yes")
print()
