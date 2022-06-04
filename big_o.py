# product and sum

# what is the runtime of the following code?

def foo(array):
    sum = 0
    product = 1

    for i in array:
        sum += 1

    for i in array:
        product *= 1

    print(f"Sum = {str(sum)} Product = {str(product)}")

# assignment of sum O(1)
# assignment of product O(1)
# first for loop O(n)
# adding to variable O(1)
# second for loop O(n)
# multiplying variable O(1)
# printing sum and product O(1)

# time complexity O(n)
# ____________________________________________________________________________________ #

# Print Pairs

def printPairs(array):
    for i in array:
        for j in array:
            print(f"{str(i)} , {str(j)}")

# first for loop O(n**2)
# second for loop O(n)
# print statement O(1)

# time complexity O(2n**2) ---> O(n**2)

# _________________________________________________________________________ #

# print unordered pairs

def printUnorderedPairs(array):
    for i in range(0, len(array)):
        for j in range(1 + 1, len(array)):
            print(array[i], array[j])

# counting iterations

# 1st ---> n-1
# 2nd ---> n-2
# 3rd ---> n - 3
# ... 1

# (n-1) + (n-2) + (n-3) + ... 1 = n(n-1) / 2 = n**2 / 2 + n

# time complexity = O(n**2)

