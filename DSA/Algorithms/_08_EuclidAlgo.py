"""
Euclid's Algorithm is an efficient method for finding the Greatest Common Divisor of two integers (the
largest number that divides both with no remainder).

We use a series of steps such that the output of one is used as the input of the next

Procedure:

    - Let k=0 count the step we are on.
    - The goal of the kth step is to find quotient q_k and remainder r_k that satisfy

        r_(k-2) = q_k * r_(k-1) + r_k    where 0 <= r_k < r_(k-1)

        or

        r_k = r_(k-2) - q_k * r_(k-1)   we are finding the multiple of r_(k-1) s.t. when taken from r_(k-2)
                                        r_k < r_(k-1)< r_(k-1)

    - For k=0, r_(k-1) and r_(k-2) will be our 2 integers, r_(k-2) being the larger.
    - Eventually r_n=0 and the algorithm stops, r_(n-1) will be the gcd of our integers.


Example:

    GCD of a=36 and b=14, we know this should be 2.

        k=0
        r_-1 = 14, r_-2 = 36
        r_0 = 36 - 14*q_0

            q_0 = 1 -> r_0 = 22,   22 > r_-1 = 14 so try next value
            q_0 = 2 -> r_0 = 8,     8 < r_-1 = 14 so q_0 = 2,  we move to k=1


        k=1
        r_1 = 14 - 8*q_1

            q_1 = 1  ->  r_1 = 6,   6 <  r_0 = 8  so q_1 = 1,  we move to k=2


        k=2
        r_2 = 8 - 6*q_2

            q_2 = 1  ->  r_2 = 2,   2 < r_1 = 6  so q_2 = 1, we move to k=3


        k=3
        r_3 = 6 - 2*q_3

            q_3 = 1  ->  r_3 = 4 > r_2 = 2
            q_3 = 2  ->  r_3 = 2 = r_2 = 2
            q_3 = 3  ->  r_3 = 0 < r_2 = 2  -> The algorithm stops here at k=3, the gcd is r_2 = 2 DONE


NOTE: This method that gives r_k can just be replaced by the modulo division of r_(k-2) % r_(k-1).

"""


# Euclid's Algo for finding the GCD of 2 positive integers
def euclid_gcd(int1, int2):
    # First ensure only integers are used
    if not isinstance(int1, int) or not isinstance(int2, int) or int1 <= 0 or int2 <= 0:
        raise(ValueError("Please input POSITIVE INTEGERS"))
    else:
        # GCD of A and A is A
        if int1 == int2:
            return int1
        # Setup r_(k-2) and r_(k-1)
        elif int1 > int2:
            a = int1
            b = int2
        else:
            a = int2
            b = int1
        # Stops when r_(k-1) is 0, we call this b
        while b != 0:
            # Initial conditions are q = 0 and r = r_(k-1), here we call it a
            q = 0
            r = a
            # iterate through q_k from 0,1,2,3,... until r_k < r_(k-1)
            while r >= b:
                q += 1
                r = a - (q*b)
            # assign r_(k-2) = r_(k-1) and r_(k-1) = r_k, this is equivalent to moving to step k+1
            a = b
            b = r
        # Loop terminates when r_k=0 is assigned to b, we then need to return the previous r_(k-1) which
        # has been assigned to a
        return a


""" 
If we want to use modulo:

def gcd(a,b):
    while b != 0:
        i = b 
        b = a % b
        a = i 
    return a
"""
