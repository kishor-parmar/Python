# Length of strings

words = ["cat", "window", "defenestrate"]

for word in words:
    print(word, len(word))
print()

for x in range(6):
    print(x)
print()

words = ["Mary", "had", "a", "little", "lamb"]
for word in range(len(words)):
    print(word, words[word])
print()    

for n in range(2, 100):
    for x in range(2, n):
        if n % x == 0:
            break
    else:
        print(n, " is a prime number")
