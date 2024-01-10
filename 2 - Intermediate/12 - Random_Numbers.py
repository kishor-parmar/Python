import random

print()
# random float in [0,1)
print("*** random float in [0,1) ***")

a = random.random()
print(a)
print()

# random float in range [a,b]
print("*** random float in range [a,b] ***")

a = random.uniform(1, 10)
print(a)
print()

# random integer in range [a,b]. b is included
print("*** random integer in range [a,b]. b is included ***")

a = random.randint(1, 10)
print(a)
print()

# random integer in range [a,b). b is excluded
print("*** random integer in range [a,b). b is excluded ***")

a = random.randrange(1, 10)
print(a)
print()

# random float from a normal distribution with mu and sigma
print("*** random float from a normal distribution with mu and sigma ***")

a = random.normalvariate(0, 1)
print(a)
print()

# choose a random element from a sequence
print("*** choose a random element from a sequence ***")

a = random.choice(list("ABCDEFGHI"))
print(a)
print()

# choose k unique random elements from a sequence
print("*** choose k unique random elements from a sequence ***")

a = random.sample(list("ABCDEFGHI"), 3)
print(a)
print()

# choose k elements with replacement, and return k sized list
print("*** choose k elements with replacement, and return k sized list ***")

a = random.choices(list("ABCDEFGHI"), k=3)
print(a)
print()

# shuffle list in place
print("*** shuffle list in place ***")

a = list("ABCDEFGHI")
random.shuffle(a)
print(a)
print()
