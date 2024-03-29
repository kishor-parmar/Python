# Tuple: Ordered, Immutable, allows duplicate elements

# Creating a Tuple
print("*** Creating a tuple ***")

mytuple = ("Max", 28, "Boston")
mytuple2 = "Max", 28, "Boston"
print(mytuple)
print(mytuple2)

mytuple = "Max"
print(type(mytuple))

mytuple = ("Max",)
print(type(mytuple))

mytuple = tuple(["Max", 28, "Boston"])
print(type(mytuple))
print(mytuple)
print()

# Accessing elements
print("*** Accessing elements ***")

item = mytuple[1]
print(item)
print()

# Accessing the last element in tuple
print("*** Accessing the last element in tuple ***")

item = mytuple[-1]
print(item)
print()

# Accessing each element in tuple
print("*** Accessing all elements in tuple ***")

for i in mytuple:
    print(i)
print()

# Locate element in tuple
print("*** Locate element in tuple ***")

if "Max" in mytuple:
    print("yes")
else:
    print("no")
print()

# Number of elements in tuple
print("*** Number of elements in tuple ***")

my_tuple = ("a", "p", "p", "l", "e")
print(len(my_tuple))
print()

# Number occurrences in a tuple
print("*** Number occurrences in a tuple ***")

print(my_tuple.count("p"))
print()

# Finding the first index of an element
print("*** Finding the first index of an element ***")

print(my_tuple.index("p"))
print()

# Convert tuple to a list & vice versa
print("*** Convert tuple to a list & vice versa ***")

print(my_tuple)
my_list = list(my_tuple)
print(my_list)

my_tuple2 = tuple(my_list)
print(my_tuple2)
print("")

# Slicing
print("*** Slicing ***")

a = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
b = a[2:5]
print(b)
print()

# Reverse the tuple
print("*** Reverse the tuple ***")

b = a[::-1]
print(b)
print()

# Unpacking
print("*** Unpacking ***")

my_tuple = ("Max", 28, "Boston")
name, age, city = my_tuple
print("name = ", name)
print("age = ", age)
print("city = ", city)
print()

my_tuple = (0, 1, 2, 3, 4)
i1, *i2, i3 = my_tuple
print(i1)
print(i3)
print(i2)
print()

# Comparing tuple with a list
print("*** Comparing tuple with a list ***")

# Size of Tuple v List
print("*** Size of Tuple v List ***")
import sys

my_list = [0, 1, 2, "hello", True]
my_tuple = (0, 1, 2, "hello", True)
print(sys.getsizeof(my_list), "bytes")
print(sys.getsizeof(my_tuple), "bytes")
print()

# Time is takes to create a list v tuple
print("*** Time is takes to create a list v tuple ***")
import timeit

print(timeit.timeit(stmt="[0,1,2,3,4,5]", number=1000000), "List")
print(timeit.timeit(stmt="(0,1,2,3,4,5)", number=1000000), "Tuple")
print()
