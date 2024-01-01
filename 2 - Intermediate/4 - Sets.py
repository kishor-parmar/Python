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

# Union of two sets
print("*** Union of two sets ***")

odds = {1, 3, 5, 7, 9}
evens = {2, 4, 6, 8}
primes = {2, 3, 5, 7}

u = odds.union(evens)
print(u)
print()

# Intersection of two sets
print("*** Intersection of two sets ***")

i = odds.intersection(primes)
print(i)
print()

# Difference of two sets
print("*** Difference of two sets ***")

setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}

diff = setA.difference(setB)
print(diff)
print()

# Symmetric Difference of two sets
print("*** Symmetric Difference of two sets ***")

diff = setA.symmetric_difference(setB)
print(diff)
print()

# Modifying a set
print("*** Modifying a set ***")

setA.update(setB)
print(setA)
print()

# Intersection of two sets with update
print("*** Intersection of two sets with update ***")

setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}

setA.intersection_update(setB)
print(setA)
print()

# Difference of two sets with update
print("*** Difference of two sets with update ***")

setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}

setA.difference_update(setB)
print(setA)
print()

# Symmetric Difference of two sets with update
print("*** Symmetric Difference of two sets with update ***")

setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}

setA.symmetric_difference_update(setB)
print(setA)
print()

# Subset of two sets
print("*** Subset of two sets ***")

setA = {1, 2, 3, 4, 5, 6}
setB = {1, 2, 3}

print(setA.issubset(setB))
print(setB.issubset(setA))
print()

# Superset of two sets
print("*** Superset of two sets ***")

print(setA.issuperset(setB))
print(setB.issuperset(setA))
print()

# Disjoint of two sets
print("*** Disjoint of two sets ***")

setA = {1, 2, 3, 4, 5, 6}
setB = {1, 2, 3}
setC = {7, 8}

print(setA.isdisjoint(setB))
print(setB.isdisjoint(setC))
print()

# Copying of two sets
print("*** Copying of two sets ***")

setA = {1, 2, 3, 4, 5, 6}

setB = setA.copy()
print(setB)

setB = set(setA)
print(setB)

print()

# Frozen Ssets
print("*** Frozen Sets ***")

a = frozenset([1, 2, 3, 4])
print(a)
print()
