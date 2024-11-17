def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

assert fibonacci(0) == 0               # 0th Fibonacci number is 0
assert fibonacci(1) == 1               # 1st Fibonacci number is 1
assert fibonacci(2) == 1               # 2nd Fibonacci number is 1
assert fibonacci(3) == 2               # 3rd Fibonacci number is 2
assert fibonacci(4) == 3               # 4th Fibonacci number is 3
assert fibonacci(5) == 5               # 5th Fibonacci number is 5
assert fibonacci(6) == 8               # 6th Fibonacci number is 8
assert fibonacci(10) == 55             # 10th Fibonacci number is 55
print(fibonacci(6))