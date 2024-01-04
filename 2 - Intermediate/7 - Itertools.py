# Itertools: Product, Permutations, Combinations, Accumulate, Groupby, Infinite iterators

# Product
print("*** Product ***")

from itertools import product

a = [1, 2]
b = [3, 4]
prod = product(a, b)
print(list(prod))

a = [1, 2]
b = [3]
prod = product(a, b, repeat=2)
print(list(prod))
print()

# Permutations
print("*** Permutations ***")

from itertools import permutations

a = [1, 2, 3]
perm = permutations(a)
print(list(perm))
perm = permutations(a, 2)
print(list(perm))
print()

# Combinations
print("*** Combinations ***")

from itertools import combinations, combinations_with_replacement

a = [1, 2, 3, 4]
comb = combinations(a, 2)
print(list(comb))

comb_wr = combinations_with_replacement(a, 2)
print(list(comb_wr))
print()

# Accumulate
print("*** Accumulate ***")

from itertools import accumulate
import operator

a = [1, 2, 3, 4]
acc = accumulate(a)
print(a)
print(list(acc))

acc = accumulate(a, func=operator.mul)
print(a)
print(list(acc))

acc = accumulate(a, func=max)
a = [1, 2, 5, 3, 4]
print(a)
print(list(acc))
print()

# Groupby
print("*** Groupby ***")

from itertools import groupby


def smaller_than_3(x):
    return x < 3


a = [1, 2, 3, 4]
group_obj = groupby(a, key=smaller_than_3)
for key, value in group_obj:
    print(key, list(value))

group_obj = groupby(a, lambda x: x < 3)
for key, value in group_obj:
    print(key, list(value))
print()

persons = [
    {"name": "Tim", "age": 25},
    {"name": "Dan", "age": 25},
    {"name": "Lisa", "age": 27},
    {"name": "Clare", "age": 28},
]

group_obj = groupby(persons, lambda x: x["age"])
for key, value in group_obj:
    print(key, list(value))
print()

# Infinite Iterators
print("*** Infinite Iterators ***")

from itertools import count, cycle, repeat

for i in count(10):
    print(i)
    if i == 20:
        break

a = [1, 2, 3]
# for i in cycle(a):
#     print(i)

for i in repeat(a, 3):
    print(i)

print()
