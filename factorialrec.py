# Using recursion by creating a factorial
# procedure. Recursion has a base case and
# a recursive case which is defined almost 
# as itself.

# The base case is when n = 0 which makes
# factorial(0) = 1.
# The recursive case is a smaller version 
# of itself.

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Test
#print(factorial(3))
#print(factorial(4))
#print(factorial(6))
