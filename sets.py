# Create an empty set
s = set()

# Add elements to set
s.add(1)
s.add(2)
s.add(3)
s.add(4)

# {1 ,2, 3, 4}
print(s)

s.add(3)
s.remove(2)

# {1, 3, 4}
print(s)

print(f"The set has {len(s)} elements")
