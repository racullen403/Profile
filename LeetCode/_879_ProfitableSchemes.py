"""
Given n members and a number of potential crimes, where the ith crime generates profit[i] and requires group[i] members
to succeed, we want to find the number of profitable schemes.

    - A profitable scheme is a subset of the crimes that generate at least the minProfit given.
    - The total number of members participating in the scheme must be less than or equal to n.

The answer may be very large so return answer in Mod(10^9 + 7)


Intuition:
    - The first thing that comes to mind is finding the different unique permutations of crimes that can happen, ie the
     subsets of the complete set, if we can do that, then we simply need to choose the subsets that agree with the
     given conditions, ie less than n members, and more than or equal to minProfit

    - We know that generating subsets is done by adding to the base subsets, ie, the base subsets of a list of objects
    will be the subsets that contain only 1 of those objects, we then add more to them to create the next subset
    (ie different linear combinations of these base vectors/objects will for different subsets), and
    so on until we have every combination.

    - We can create these subsets using a DFS and we can terminate the DFS early if we get to a stage where we need
    more members than there exists, once we reach this point, we just have to check if the combination of crimes
    reached the minProfit, if it did then add it to the list.

    - This problem with this method is that there are 2**n total possible subsets, this means for larger values of n
    this method becomes almost impossible to calculate. We need a new method.

    - We can consider this as another form of the Knapsack problem, where we now have 2 constraints instead of the
    just 1. We know to solve the Knapsack problem we have to build up optimal sub-solutions 1 object at a time, for
    every given weight less than or equal to the max capacity of the Knapsack. In this case, we will have to build
    up the optimal solutions, 1 crime at a time, for every given number of potential members, less than or equal to n,
    and for any given profit greater than or equal to minProfit.

    - In this case we would create an array dp[i][j][k] where for the i crimes, given j members and a working profit
    of k, then dp[i][j][k] would give the number of profitable schemes

"""


def find_profitable_schemes(n, minProfit, group, profit):
    i = len(group)
    profitable_schemes = 0
    schemes = [(group[j], profit[j], j) for j in range(i)]
    while schemes:
        scheme = schemes.pop()
        if scheme[0] <= n:
            for j in range(scheme[2] + 1, i):
                schemes.append((scheme[0] + group[j], scheme[1] + profit[j], j))
            if scheme[1] >= minProfit:
                profitable_schemes += 1
    return profitable_schemes


def example1():
    prof = find_profitable_schemes(10, 3, [2, 3, 5], [6, 7, 8])
    print(prof)


def find_profitable_schemes_dp(n, minProfit, group, profit):
    dp = [[0] * (minProfit + 1) for _ in range(n + 1)]
    dp[0][0] = 1
    for i in range(len(group)):
        p = profit[i]
        g = group[i]
        new_dp = [[0] * (minProfit + 1) for _ in range(n + 1)]
        for j in range(n + 1):
            for k in range(minProfit + 1):
                if j < g:
                    new_dp[j][k] = dp[j][k]
                else:
                    new_dp[j][k] = dp[j][k] + dp[j - g][max(k - p, 0)]
        dp = new_dp
        print(dp)
    return sum(dp[j][minProfit] for j in range(n+1))


def example2():
    n = 5
    minProfit = 3
    group = [2, 2]
    profit = [2, 3]
    sol = find_profitable_schemes_dp(n, minProfit, group, profit)
    print(sol)

example2()




