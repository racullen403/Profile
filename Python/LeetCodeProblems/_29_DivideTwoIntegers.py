"""
Given the Dividend and Divisor (positive or negative integers) we are tasked with returning the quotient of this
calculation without using Multiplication, Division, or the Mod Operation. We are also only allowed to store
32-bit signed integers [-2**31, 2**31 - 1].


Solution 1, using lookup table and no bit shift operators:

    Create a logarithmic lookup table until we found a total > Dividend

        e.g.    Take 79 / 4

                Count   Total
                1       4
                2       8
                4       16
                8       32
                16      64

                The next term would be (32, 128) which is larger than 79 so we stop before this.

    Next, we use a "Greedy" method, to take the largest possible total from the Dividend and add the respective Count
    to the output Quotient, doing this until the Dividend < Divisor.

    We will be left with the Quotient and the final Dividend being the "Remainder"

    We will have O(logn) Space Complexity (n being the Dividend) needed to store the lookup table.

    The time complexity is Linear in terms of the lookup table, however this is created in Logarithmic time and
    so Time Complexity will also be Logarithmic.


Solution 2: Using bit shifting

    Before we created a lookup table by simply doubling the count/total each iteration. This process
    of multiplication by X2 or //2 can be achieved using bit shifts >>, <<.

        e.g     21 // 2 -> 1
                10 // 2 -> 0
                5 // 2 -> 1
                2 // 2 -> 0
                1 // 2 -> 1     (21 == 10101 == 2**0 + 2**2 + 2**4 == 1+4+16 == 21)

                21 << 1 shifts the bits left by 1 position and adds 0 on the right
                10101 << 1 == 101010 which is just 21*2 == 42

                42 == 101010 == (2**5 + 2**3 + 2**1 == 2*(2**4 + 2**2 + 2**0)) == 2*21

                21 >> 1 shift bits to the right 1 position
                10101 >> 1 == 1010 == 10 which is just 21//2 e.g. we get the quotient and lose the remainder


Solution 3: without lookup table

    Our previous 2 solutions are both the same, one simply doubles by adding, while the other doubles by bit shifting,
    and we stored the results in a lookup table. If we wanted to keep the solution logarithmic but get rid of the
    excess space needed for the lookup table, we would simply redo the same method on each iteration removing the
    largest value we could for the numerator.

    This would save on Space however would increase the time needed to find the solution.


Overflow:

    - We are also tasked with only ever storing 32-bit signed integers, [-2**31, 2**31 - 1]
    - Overflow will only ever happen in the following cases

        - Case 1: When num = -2**31 and den = 1, we cant make -2**31 positive sp we simply return it as the answer

        - Case 2: When num = -2**31 and den = -1, the true answer would be 2**31 which is too large, return 2**31 - 1

        - Case 3: When building the lookup table, we stop when we reach a number larger than the dividend, this could
        potentially be a number larger than 2**31 - 1, so we must check the condition:

            number < (2**31 - 1) - number

"""


# Logarithmic solution without bit shifts and using (logn) lookup table
def return_quotient(num, den):
    # Deal with signs
    positive = (num < 0) == (den < 0)
    # Overflow
    if num == -(2**31):
        if den == 1:
            return -(2**31)
        elif den == -1:
            return (2**31)-1
    # Get rid of signs
    num = abs(num)
    den = abs(den)
    # Build "times table" lookup O(logn), use a flag to end the loop
    lookup = []
    count = 1
    total = den
    flag = True
    while total <= num and flag:
        lookup.append((total, count))
        if total < (2**31 - 1) - total:
            total += total
            count += count
        else:
            flag = False
    # Remove the biggest possible count from dividend, adding the count to the output, until dividend < divisor
    output = 0
    pointer = len(lookup) - 1
    while num >= den and pointer >= 0:
        if lookup[pointer][0] > num:
            pointer -= 1
        else:
            num -= lookup[pointer][0]
            output += lookup[pointer][1]
    if not positive:
        output = -output
    return output
