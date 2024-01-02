# Strings: Ordered, immutable, text representation

# Creating a String
print("*** Creating a String **")

my_string = "Hello World"
print(my_string)
print()

# Accessing characters and substrings
print("*** Accessing characters and substrings ***")

my_string = "Hello World"
char = my_string[1]
print(char)
print()

char = my_string[-2]
print(char)
print()

# Slicing to obtain a substring
print("*** Slicing to obtain a substring")

my_string = "Hello World"
substring = my_string[1:4]
print(substring)
print()

# Concatenating two strings
print("*** Concatenating two strings ***")

greeting = "Hello"
name = "Foobar"
sentance = greeting + " " + name
print(sentance)
print()

# Iterating through a string
print("*** Iterating through a string ***")

for i in greeting:
    print(i)
print()

# Check for a character in a string
print("*** Check for a character in a string ***")

if "ll" in greeting:
    print("Yes")
else:
    print("No")
print()

# Trimming white space
print("*** Trimming white space ***")

my_string = "      Hello    World    "
my_string = my_string.strip()
print("*" + my_string + "*")
print()

# Converting Strings
print("*** Converting String ***")

my_string = "Hello World"
print(my_string.upper())
print(my_string.lower())
print(my_string.startswith("H"))
print(my_string.startswith("Hell"))
print(my_string.startswith("World"))
print(my_string.endswith("World"))
print(my_string.find("llo"))
print(my_string.find("kp"))
print(my_string.count("l"))
print(my_string.replace("l", "x"))
print()

# Converting a string to elements in a list
print("*** Converting a string to elements in a list ***")

my_string = "how are you doing"
mylist = my_string.split()
print(mylist)

my_string = "how,are,you,doing"
mylist = my_string.split(",")
print(mylist)
print()

# Converting elements in a list to a string
print("*** Converting elements in a list to a string ***")

from timeit import default_timer as timer

my_string = "how,are,you,doing"
mylist = my_string.split(",")
print(mylist)
new_string = " ".join(mylist)
print(new_string)

start = timer()
mylist = ["a"] * 6
print(mylist)
my_string = " ".join(mylist)
stop = timer()
print(my_string)
print(stop - start)
print()

# Formatting String
print("*** Formatting Strings ***")
print("*** % ***")
var = "Kish"
my_string = "the variable is %s" % var
print(my_string)

var = 3
my_string = "the variable is %d" % var
print(my_string)

var = 3.1425
my_string = "the variable is %.2f" % var
print(my_string)
print()

print("*** .format ***")
var = 3.1425
var2 = 6
my_string = "the variable is {:.2f} and {}".format(var, var2)
print(my_string)
print()

print("*** f-Strings ***")
var = 3.1425
var2 = 6
my_string = f"the variable is {var:.2f} and {var2}"
print(my_string)
