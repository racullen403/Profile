"""
Rod Cutting:

    A business cuts steel rods of length n into various lengths, i, and for each length, the price it is sold is p_i.
    We want to know the best way to cut up the rods to maximize revenue r.


        First lets consider a rod of length n, and we can cut it into as many integer lengths as we want. How many
        potential ways of cutting it up are there?

            Well there will be n-1 places that we can cut, and we either make a cut, or don't make a cut, which is
            2 options, so there will be 2**(n-1) potential ways to cut the rod.


    Our approach:

        Let r_i be maximum revenue we can get from a rod of length i, then the problem can be defined as

            r_n = max(p_i + r_n-i) where 1 <= i <= n

        The idea here is that we don't know how to cut the rod, so we try all possible cases for where the cut can go,
        i, and then try and find the optimal way to cut a rod of length n-i.

        In this way, we know for a rod of length 1, the optimal solution r_1 is the rod itself, and so we can use this
        solution to know find the optimal solution r_2 by trying all potential cuts, working our way up to r_n by
        storing all previous optimal solutions and using them for r_n-1 in the above equation.

        Note that in solving r_n, we solve for all r_0, r_1, ..., r_(n-1) in order to form the final solution.

"""


# Bottom up approach
def rod_cutting(n, l, pl):
    revenue = [0 for _ in range(n+1)]
    cuts = [[] for _ in range(n+1)]
    for rod_length in range(1, n+1):
        opt = 0
        for i in range(len(l)):
            cut_length = l[i]
            cut_rev = pl[i]
            if cut_length > rod_length:
                break
            temp = revenue[rod_length - cut_length] + cut_rev
            if temp > opt:
                revenue[rod_length] = temp
                cuts[rod_length] = cuts[rod_length - cut_length] + [cut_length]
                opt = temp
    return cuts, revenue


def example():
    cut_length = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    cut_revenue = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
    lengths, revenue = rod_cutting(10, cut_length, cut_revenue)
    rod_length = 0
    for l, r in zip(lengths, revenue):
        print("For rod of length {}, optimal revenue is {} from cuts: {}".format(rod_length, r, l))
        rod_length += 1

