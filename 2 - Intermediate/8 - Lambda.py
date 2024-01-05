# lambda arguments: expression

# Function
print("*** Fuction ***")


def func_add10(x):
    x = x + 10
    return x


print(func_add10(3))
print()

# Lamda
print("*** Lamda ***")

add10 = lambda x: x + 10
print(add10(3))

mult = lambda x, y: x * y
print(mult(2, 4))
print()

# Sorting
print("*** Sorting ***")

points2d = [(1, 2), (15, 1), (5, -1), (10, 4)]
points2d_sorted = sorted(points2d)
print(points2d)
print(points2d_sorted)
print()

points2d_sorted = sorted(points2d, key=lambda x: x[1])
print(points2d)
print(points2d_sorted)
print()


def sort_by_y(x):
    return x[1]


points2d_sorted = sorted(points2d, key=sort_by_y)
print(points2d)
print(points2d_sorted)
print()

points2d = [(1, 2), (15, 1), (5, -1), (10, 4)]
points2d_sorted = sorted(points2d, key=lambda x: x[0] + x[1])
print(points2d)
print(points2d_sorted)
print()

# Map (func, seq)
print("*** map(func, seq) ***")

a = [1, 2, 3, 4, 5]
b = map(lambda x: x * 2, a)
print(a)
print(list(b))
print()

c = [x * 2 for x in a]
print(list(c))
print()

# Filter (func,seq)
print("*** filter(func, seq) ***")

a = [1, 2, 3, 4, 5, 6]
b = filter(lambda x: x % 2 == 0, a)
print(a)
print(list(b))

c = [x for x in a if x % 2 == 0]
print(c)
print()

# Reduce(func, seq)
print("*** reduce(func,seq) ***")

from functools import reduce

a = [1, 2, 3, 4, 5]
producta = reduce(lambda x, y: x * y, a)
print(producta)
