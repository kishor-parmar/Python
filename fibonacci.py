# Fibonacci  Series
# the sum of the two elements defines the next

def fib(n):
    result = []
    num1, num2 = 0, 1
    while num1 < n:
        result.append(num1)
        num1, num2 = num2, num1 + num2
    return result

x = fib(2000)
print(x)