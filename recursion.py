

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


# print(fibonacci(60))

# Sum of Digits

def sum_of_digits(n):
    assert n >= 0 and int(n) == n, "Must be greater than zero and a real number"
    if n == 0:
        return 0
    else:
        return int(n % 10) + sum_of_digits(int(n//10))


# print(sum_of_digits(6543))

# calculate power using recursion

def power(base, exponent):
    assert exponent >= 0 and int(exponent) == exponent, "Exponent cannot be negative and must be a whole number"
    if exponent == 0:
        return 1
    if exponent == 1:
        return base
    else:
        return base * power(base, exponent - 1)


# print(power(2, 4))

# Greatest common divisor

def greatest_common_divisor(n1, n2):
    assert int(n1) == n1 and int(n2) == n2, "Numbers must be integers"
    if n1 < 0:
        n1 = abs(n1)
    if n2 < 0:
        n2 = abs(n2)
    while n2 == 0:
        return n1
    else:
        return greatest_common_divisor(n2, n1 % n2)

# print(greatest_common_divisor(48052, -18492))


# Decimal to binary
# Divide number by 2
# get integer quotient for next iteration
# get remainder for binary digit
# repeat until quotient is 0

def d2b(n):
    assert n == int(n), "Must be integer"
    if n == 0:
        return 0
    else:
        return n % 2 + 10 * d2b(int(n / 2))


# print(d2b(10034))

arr = [1, 2, 3]


def productOfArray(arr):
    if len(arr) == 0:
        return 1
    else:
        return arr[0] * productOfArray(arr[1:])
    # result = 1
    # for x in arr:
    #     result *= x
    # return result

# print(productOfArray(arr))

# recursive range

def recurse_range(n):
    if n <= 0:
        return 0

    return n + recurse_range(n - 1)

print(recurse_range(35))