def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)
assert factorial(0) == 1            # Edge case: 0! = 1
assert factorial(1) == 1            # 1! = 1
assert factorial(5) == 120          # 5! = 5 × 4 × 3 × 2 × 1 = 120
assert factorial(7) == 5040         # 7! = 5040
assert factorial(10) == 3628800     # 10! = 3628800
assert factorial(15) == 1307674368000       # 15! = 1307674368000
assert factorial(20) == 2432902008176640000 # 20! = 2432902008176640000