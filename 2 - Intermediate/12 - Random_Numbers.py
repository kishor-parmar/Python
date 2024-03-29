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

# Seeding with 1
print("*** Seeding with 1 ***\n")

random.seed(1)
print(random.random())
print(random.uniform(1, 10))
print(random.choice(list("ABCDEFGHI")))
print()

# Re-seeding with 42
print("\n*** Re-seeding with 42 ***\n")
random.seed(42)  # Re-seed

print(random.random())
print(random.uniform(1, 10))
print(random.choice(list("ABCDEFGHI")))
print()

# Re-seeding with 1
print("\n*** Re-seeding with 1 ***\n")
random.seed(1)  # Re-seed

print(random.random())
print(random.uniform(1, 10))
print(random.choice(list("ABCDEFGHI")))
print()

# Re-seeding with 42
print("*** Re-seeding with 42 ***\n")
random.seed(42)  # Re-seed

print(random.random())
print(random.uniform(1, 10))
print(random.choice(list("ABCDEFGHI")))
print()

import secrets

# random integer in range [0, n).
print("*** random integer in range [0, n) ***")
a = secrets.randbelow(10)
print(a)
print()

# return an integer with k random bits
print("*** return an integer with k random bits ***")
a = secrets.randbits(5)
print(a)
print()

# choose a random element from a sequence
print("*** choose a random element from a sequence ***")
a = secrets.choice(list("ABCDEFGHI"))
print(a)
print()

# Random Numbers with Numpy
print("*** Random Numbers with Numpy ***")

import numpy as np

np.random.seed(1)
# rand(d0,d1,…,dn)
# generate nd array with random floats, arrays has size (d0,d1,…,dn)
print("*** generate nd array with random floats, arrays has size (d0,d1,…,dn) ***")

print(np.random.rand(3))
print()

# reset the seed
print("*** reset the seed ***")
np.random.seed(1)
print(np.random.rand(3))
print()

# generate nd array with random integers in range [a,b) with size n
print("*** generate nd array with random integers in range [a,b) with size n ***")

values = np.random.randint(0, 10, (5, 3))
print(values)
print()

# generate nd array with Gaussian values, array has size (d0,d1,…,dn)
# values from standard normal distribution with mean 0.0 and standard deviation 1.0
print("*** generate nd array with Gaussian values, array has size (d0,d1,…,dn) ***")
values = np.random.randn(5)
print(values)
print()

# randomly shuffle a nd array
# only shuffles the array along the first axis of a multi-dimensional array
print("*** randomly shuffle a nd array ***")

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
np.random.shuffle(arr)
print(arr)
print()
