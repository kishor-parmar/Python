################
# swap variables
################

print()
print("swap variables")

a = 5
b = 10

a, b = b, a

print(a, b)
# 10, 5

####################
# List Comprehension
####################

print()
print("List Comprehension")

squares = [i * i for i in range(5)]
print(squares)
# [0, 1, 4, 9, 16]

squares = [i * i for i in range(5) if i % 2 == 0]
print(squares)
# [0, 4, 16]


############################
# Ternary operator (if-else)
############################

print()
print("Ternary operator (if-else)")

var = 42 if 3 > 2 else 999
print(var)
# 42


#########################
# Print without new lines
#########################

print()
print("Print without new lines")

# No need to do this:
data = [0, 1, 2, 3, 4, 5]
for i in data:
    print(i, end=" ")
print()

# One-liner
print(*data)
# 0 1 2 3 4 5


#############################
# Number of days left in year
#############################

print()
print("Number of days left in year")

import datetime

print((datetime.date(2025, 1, 1) - datetime.date.today()).days)

##################
# Reversing a List
##################

print()
print("Reversing a List")

a = [1, 2, 3, 4, 5, 6]
a = a[::-1]
print(a)
# [6, 5, 4, 3, 2, 1]

a = "level"
print(a == a[::-1])
# true


###############################
# Multiple variable assignments
###############################

print()
print("Multiple variable assignments")
a, b, c = 3, 99, "Python"

print(a, b, c)
# 3, 99, 'Python'


#########################################
# Space separated numbers to integer list
#########################################

print()
print("Space separated numbers to integer list")

user_input = "1 2 3 4 5 6"

my_list = list(map(int, user_input.split()))
print(my_list)
# [1, 2, 3, 4, 5, 6]


my_list = [line.strip() for line in open("person.txt", "r")]
print(my_list)
# ['Tom  Smith', 'Mike     Jones', 'Paul      Mac', 'John   Brown', '']

my_list2 = [line.replace(" ", "") for line in open("person.txt", "r")]
print(my_list2)
# ['TomSmith\n', 'MikeJones\n', 'PaulMac\n', 'JohnBrown\n', '']

my_list3 = [" ".join(line.split()) for line in open("person.txt", "r")]
print(my_list3)
# ['Tom Smith', 'Mike Jones', 'Paul Mac', 'John Brown', '']
