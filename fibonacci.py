# Fibonacci  Series
# the sum of the two elements defines the next

def fib(n):
    num1, num2 = 0, 1
    while num1 < n:
        print(num1, end=', ')
        num1, num2 = num2, num1 + num2
#       num1 = num2
#       num2 = num1 + num2

fib(2000)
