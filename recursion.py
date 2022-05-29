

def recursive_method(n):
    if n < 1:
        print("n is less than 1")
    else:
        recursive_method(n - 1)
        print(n)


# recursive_method(4)


# factorial

# Step 1: recursive case - the flow

# n! = n * (n - 1) * (n - 2) * (n - 3) ... * 2 * 1

def factorial(n):
    assert n >= 0 and int(n) == n, "The number must be positive integer only"
    if n in [0, 1]:
        return 1
    else:
        return n * factorial(n - 1)


# print(factorial(14))

# fibonacci numbers - Recursion

def fibonacci(n):
    assert n >= 0 and int(n) == n, "Must be greater than zero and a whole number"
    if n in [0, 1]:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(60))
