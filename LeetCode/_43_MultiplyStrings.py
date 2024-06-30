"""
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also
represented as a string.

Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.


Solution 1:

    - We simply calculate the entire total using normal multiplication methods, after converting
    ch -> int, and then convert the final int -> str

Solution 2:

    - We create an output list on length equal to the size of num1 + num1, no 2 numbers will every multiply
    to be bigger than this.
    - We then iterate through num1, keeping track of the order each time we move to the next digit. For each
    digit in num1, we loop through num2, adding to the order each time we move to the next digit in num2.
    Note that keeping track of the order is simply a matter of moving a pointer.


    E.g.    Take num1 = "123" and num2 = "456"


             output = [0, 0, 0, 0, 0, 0]
             pos = len(output) - 1 = 5


             Iterate through num1:

                n1 = 3, n1_pos = pos


                Iterate through num 2:

                    n2 = 6, n1_pos = 5

                        We now do the multiplication method

                        n1 * n2 = 3 * 6 = 18
                        place this at n1_pos

                        output = [0, 0, 0, 0, 0, 18]

                        move the carry term forward, and remove it from n1_pos

                        output = [0, 0, 0, 0, 1, 8]

                        now update the order by moving n1_pos -= 1


                    n2 = 5, n1_pos = 4

                        n1 * n2 = 3 * 5 = 15

                        output = [0, 0, 0, 0, 16, 8] -> output = [0, 0, 0, 1, 6, 8]

                        n1_pos -= 1

            We would simply repeat like this until all digits in num2 are exhausted, then go to the next
            digit in num1, and update the order by setting pos -= 1, therefore n1_pos starts at the next
            order of magnitude.

    - Finally we would just join this list of integers as a string
"""


# Solution 1
def multiply_strings(num1, num2):
    # Lookup for converting ch to int
    digits = {
        "0": 0,
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9
    }

    # Calculating the total of multiplying both numbers
    output = 0
    n2 = len(num2) - 1
    while n2 >= 0:
        n2_d = digits[num2[n2]]
        n1 = len(num1) - 1
        order_n2 = len(num2) - 1 - n2
        total = 0
        while n1 >= 0:
            n1_d = digits[num1[n1]]
            order_n1 = len(num1) - 1 - n1
            total += (n1_d * n2_d) * (10 ** order_n1)
            n1 -= 1
        output += total * (10 ** order_n2)
        n2 -= 1

    # Convert final total back to string, if this isn't allowed, we can very easily use different method.
    return str(output)


# Solution 2
def multiply_stings_2(num1, num2):
    output = [0] * (len(num1) + len(num2))  # Create output list
    pos = len(output) - 1  # Set initial pointer where we will add to first

    for n1 in num1[::-1]:
        n1_pos = pos  # Iterate through num1
        for n2 in num2[::-1]:
            output[n1_pos] += int(num1[n1]) * int(num2[n2])  # Add the product into n1_pos
            output[n1_pos - 1] += output[n1_pos] // 10  # Add the carry term into the next n1_pos
            output[n1_pos] %= 10  # Remove the carry from the n1_pos
            n1_pos -= 1  # Move to the next n1_pos and repeat
        pos -= 1  # Once we have run out of n1 terms, we move pos

    # We know need to remove any "0" padding terms in output
    padding = 0
    while padding < len(output) - 1 and output[padding] == 0:
        padding += 1

    return "".join(map(str, output[padding:]))


