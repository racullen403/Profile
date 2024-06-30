"""
We will look at the case of converting an integer into a string with a different base.

The key to this is the "Divide by x" method,

    - We divide by some base, and push the remainder into a stack.
    - Repeat with new value until we reach 0.
    - Pop the values out of the stack in reverse to get the integer value in some new base.

"""


# String starts with 0 for positive number, 1 for negative number
def integer2base(integer, base=2):
    lookup = "0123456789ABCDEF"
    output = "0"
    if integer < 0:
        integer *= (-1)
        output = "1"
    s = []
    while integer != 0:
        s.append(lookup[integer % base])
        integer = integer // base
    while len(s) > 0:
        output = output + s.pop()
    return output


""" 
Now we will consider a recursive method for this:

    - Our base case will be when the input integer, integer divides to give 0. When this 
    happens we will simply return the last character using lookup[remainder].
    
    - We will reduce the state towards this base case by integer dividing by the "base" 
    and using this as the input to the next function call.
    
    - Instead of using a stack and popping the characters back out in reverse to get the 
    base string version of the integer, we can simply use the recursion call in the order 
    we want the characters to appear (see function below for order)
        
"""


def recursive_integer2base(integer, base=2):
    lookup = "0123456789ABCDEF"
    if integer // base == 0:
        return lookup[integer % base]
    return recursive_integer2base(integer // base, base=base) + lookup[integer % base]


# Function that calls our recursion function and allows us to distinguish +ve and -ve
# integers with starting "0" or "1" respectively
def recursive_int2base(integer, base=2):
    output = "0"
    if integer < 0:
        output = "1"
        integer *= (-1)
    return output + recursive_integer2base(integer, base=base)


print(recursive_int2base(-10))
