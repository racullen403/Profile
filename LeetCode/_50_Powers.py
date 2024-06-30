"""
Given x and integer n, calculate x^n.


    Solution 1:
        - The obvious brute force method is to simply iterate total*x n times until we get a solution.
        - THe problem with this is it runs in O(n) time.

    Solution 2:
        - We use the binary representation of n, e.g. n=12 is 1100.
        - Knowing the binary representation allows us to express the power as a multiplication of these terms

            x^12 where n=1100 in binary tells us x^8 * x^4

        - We can build up these multiplication terms in O(logn) time using doubling

            x -> x^2 -> x^4 -> x^8

        - We can get the binary representation by halving n and using the remainder term as the current binary value



"""


# Solution using binary representation of n
def power_1(x, n):
    if n == 0:
        return 1
    if n < 0:
        n = -n
        x = 1/x
    temp = n
    binary = []
    while temp != 0:
        binary.append(temp % 2)
        temp //= 2
    print("\nCalculate {}^{}:".format(x, n))
    print("Binary Representation of {} in a stack:".format(n), binary)
    total = 1
    for i in binary:
        if i == 1:
            total *= x
            print("  total = {}".format(total))
        x *= x
    return total


# More concise solution with bit manipulation
def pow(x, n):
    if n == 0:
        return 1
    if n < 0:
        n = -n
        x = 1/x
    temp = n
    total = 1
    while temp != 0:
        if temp & 1:  # Bitwise compare last digit of binary representation
            total *= x
        x *= x
        temp >>= 1  # Bit-shift temp right, removing the rightmost bit
    print(total)
    return total


# Recursive solution
def power_recursive(x, n):
    if n == 0:
        return 1
    if n < 0:
        return 1/power_recursive(x, -n)
    if n % 2 == 0:
        return power_recursive(x*x, n/2)
    return x*power_recursive(x, n-1)


power_1(2, -4)
pow(2, -4)
print(power_recursive(2, -4))