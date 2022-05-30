"""
We want to convert a positive integer into a string of Roman Numerals, [0, 3999]

Solution:
    - Use a lookup mapping integers to corresponding numerals
    - perform a greedy algorithm
"""


def int_to_roman(x):
    if x <= 0 or x >= 4000:
        return None
    lookup = {1000: "M",
              900: "CM",
              500: "D",
              400: "CD",
              100: "C",
              90: "XC",
              50: "L",
              40: "XL",
              10: "X",
              9: "IX",
              5: "V",
              4: "IV",
              1: "I"
              }
    order = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    i = 0
    output = ""
    while i < len(order):
        if x >= order[i]:
            x -= order[i]
            output += lookup[order[i]]
        else:
            i += 1
    return output

