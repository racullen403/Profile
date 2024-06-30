"""
We are given a list of objects that have some weight value and monetary value associated with them. We are tasked
with finding which objects we should carry in order to make the most money, without going over some weight limit.

In essence this is a subset problem. We know the total subsets that exist is 2**n and so it is not feasible to
generate every subset and check which is the best solution. We need another method.

If we consider a way of building up a solution using the optimal substructure of sub-solutions, we can implement a
dynamic programming method. Consider this:
    - We find the optimal solution for using only 1 object at any given weight.
    - We then consider 2 objects. For each weight we consider the case of the previous 1 object solution with the
    new weight added in, in each instance, we take the new optimal solution.
    - In this way we can build up a complete solution for n objects.
    - This method would only require O(max_cap*n) time, as we iterate over every weight up to the max capacity and do
    this for each n objects.

"""


def knapsack(max_cap, weights, values):
    dp = [([], 0)]*(max_cap + 1)
    for i in range(len(weights)):
        new_dp = [([], 0)]*(max_cap + 1)
        w = weights[i]
        v = values[i]
        for j in range(max_cap+1):
            if j < w:
                new_dp[j] = dp[j]
            elif dp[j-w][1] + v > dp[j][1]:
                new_dp[j] = (dp[j-w][0] + [w], dp[j-w][1] + v)
            else:
                new_dp[j] = new_dp[j-1]
        dp = new_dp
    return dp[-1]


