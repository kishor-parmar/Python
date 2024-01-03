# Collections: Counter, NamedTuple, OrderedDict, DefaultDict, Deque

# Counter
print("*** Counter ***")

from collections import Counter

a = "aaaaabbbccccccccc"
mycounter = Counter(a)
print(mycounter)
print(mycounter.items())
print(mycounter.keys())
print(mycounter.values())
print(mycounter.most_common(1))
print(mycounter.most_common(1)[0])
print(mycounter.most_common(1)[0][0])
print(list(mycounter.elements()))
print()

# NamedTuple
print("*** NamedTuple ***")

from collections import namedtuple

Point = namedtuple("Point", "x,y")
mypoint = Point(1, -4)
print(mypoint)
print(mypoint.x, mypoint.y)
print()

# OrderedDict
print("*** OrderedDict ***")

from collections import OrderedDict

ordered_dict = OrderedDict()
ordered_dict["b"] = 2
ordered_dict["c"] = 3
ordered_dict["d"] = 4
ordered_dict["e"] = 5
ordered_dict["a"] = 1
print(ordered_dict)
print()

# DefaultDict
print("*** DefaultDict ***")

from collections import defaultdict

d = defaultdict(int)
d["a"] = 1
d["b"] = 2
print(d)
print(d["a"])
print(d["b"])
print(d["z"])
print()

# Deque
print("*** Dequse ***")

from collections import deque

d = deque()
d.append(1)
d.append(2)
print(d)

d.appendleft(3)
print(d)

d.pop()
print(d)
d.popleft()
print(d)

d.append(1)
d.append(2)
d.appendleft(3)
print(d)
d.remove(1)
print(d)

d.clear()
print(d)

d.append(1)
d.append(2)
d.appendleft(3)
d.extend([4, 5, 6])
print(d)

d.extendleft([7, 8, 9])
print(d)

d.rotate(1)
print(d)

d.rotate(-1)
print(d)
print()
