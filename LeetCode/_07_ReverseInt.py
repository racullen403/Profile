"""
We simply want to reverse a 32-bit integer, ensuring we do not go outside the signed 32-bit integer range,
[-2**31, 2**31 - 1], returning 0 if this would be the case

Solution:
    Reversing an integer is quite a simple process:
        - Simply take a sum starting with 0, multiply it by 10 and add the last digit from some integer X each time,
        then let X = X//10, repeat until X=0

        e.g x = 123, count = 0  -> x = 12, count = 3 -> x = 1, count = 32 -> x = 0, count = 321

    The main quirk of this question is to not use a number outside the signed 32-bit integer range as we must
    assume the environment cannot store this.

        - Case 1:
            If we start with -2**31, when we change the sign 2**31 > 2**31 - 1 so we return 0

        - Case 2:
            When we are calculating the new sum total, there is the chance that multiplying by 10 and adding the last
            digit makes a total > 2**32 - 1. Hence, we must ensure:

             sum*10 + X%10 <= 2**31 - 1

             or

             sum > ((2**31 - 1) - X%10) / 10


"""


def reverse_int(x):
    count = 0
    neg = True
    if x < 0:
        if x <= -(2**31):
            return 0
        neg = True
        x *= -1
    while x > 0:
        if count > ((2**31 - 1) - x % 10) / 10:
            return 0
        count = count * 10 + x % 10
        x //= 10
    if neg is True:
        return -count
    return count