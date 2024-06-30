"""
Given so integer n, we want to return the smallest number of perfect squares that add up to give n.

Solution 1:
    - This can be solved using a dynamic programming approach, where we use the overlapping sub-solutions to create
    new solutions.

        e.g. take n = 12

            we create an array of length 13 represented as

                {   0: 0
                    1:
                    2:
                    3:
                    4:
                    5:
                    6:
                    7:
                    8:
                    9:
                    ...
                    11:
                    12:
                }

            We set dp[0] = 0 and now build up solutions using the optimal sub-solutions as follows.

                dp[i] = min(dp[i], dp[i-sq**2]+1), where sq = 1, 2, 3, ... until i-sq**2 < 0

            so,

                dp[1] = dp[0]+1
                dp[2] = dp[1]+1
                dp[3] = dp[2]+1
                dp[4] = min(dp[3]+1, dp[0]+1)

                ...

                dp[12] = min(dp[11]+1, dp[8]+1, dp[3]+1)



Solution 2:
    - This could also be solved using a greedy BFS, where we order the perfect squares that are less than n, and
    perform a bfs on them to find the summations that add to n.

    e.g. n = 12 , squares = [1, 4, 9]

        step = 1, summations = [ [[1]], [[4]], [[9]] ]
        step = 2, summations = [ [ [1,1], [1,4], [1,9] ], [ [4,4], [4,9] ], [ [9,9] ] ]

        etc ...

        - When a summation is greater than n=12 we would abandon that path.
        - Note that by ordering the squares and by only considering sums of squares equal or greater than the current,
        we can get rid of the repeated summation permutations like [1,4] and [4,1].
        - Continuing like this will lead to all summations that give 12, and we know that the first instance of a
        summation that gives 12 will be the smallest answer (by the nature of it being a bfs)


"""


# Dynamic Solution Approach
def perfect_squares_dp(n):
    dp = [n for _ in range(n+1)]
    dp[0] = 0
    for i in range(1, n+1):
        sq = 1
        while i - (sq**2) >= 0:
            dp[i] = min(dp[i], dp[i-sq**2]+1)
            sq += 1
    print(dp[-1])
    return dp[-1]


# BFS Approach, retains the path
def perfect_square_bfs(n):
    sq = 1
    nums = []
    sums = []
    while sq**2 <= n:
        if sq**2 == n:
            return 1
        nums.append(sq)
        sums.append(([sq**2], sq-1))
        sq += 1
    while True:
        new_lst = []
        for path, i in sums:
            for j in range(i, len(nums)):
                new_sum = (path + [nums[j]**2], j)
                if sum(new_sum[0]) == n:
                    return new_sum[0]
                elif sum(new_sum[0]) < n:
                    new_lst.append(new_sum)
        sums = new_lst



