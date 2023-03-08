# Fibonacci  Series
# the sum of the two elements defines the next

num1, num2 = 0, 1
while num1 < 1000:
    print(num1, end=', ')
    num1, num2 = num2, num1 + num2
#    num1 = num2
#    num2 = num1 + num2

