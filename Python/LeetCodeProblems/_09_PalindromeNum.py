"""
We want to know if an integer is a palindrome

Solution 1:
    The easiest check for this is to simply reverse the integer, if we get the
    same number then the integer was a palindrome.

Solution 2:
    By similar process we break the number down, however we can stop at the half-way point.

    e.g     start:  num = 12321 total = 0
            step 1: num = 1232  total = 1
            step 2: num = 123   total = 12
            step 3: num = 12    total = 123     since total >= num, we stop

            - now if num == total, then we have an even palindrome
            - if total//10 == num, we have an odd palindrome
            - else we don't have a palindrome

    Our edge cases will be when num < 0 or if num > 0 and num%10=0, in these instances, the num is not a
    palindrome, and we can return False
"""


def is_int_palindrome(x):
    if x < 0:
        return False
    num = x
    total = 0
    while num > 0:
        total = (total * 10) + (num % 10)
        num = num // 10
    return total == x


def sol_two(x):
    if x < 0 or (x > 0 and x % 10 == 0):
        return False
    total = 0
    while x > total:
        total = total*10 + x % 10
        x //= 10
    return (x == total) or (x == total//10)
