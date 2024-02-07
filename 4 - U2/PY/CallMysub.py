import u2py
result = u2py.call("MYSUB", "Kish", None)
print(result)
print(len(result))
for value in result:
    print(value)