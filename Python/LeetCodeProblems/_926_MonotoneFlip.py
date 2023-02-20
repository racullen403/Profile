"""
Given a string of binary, we want to form a monotonically increasing string by flipping the fewest bits.

    E.g.  110001 -> 000001 in 2 flips


    Solution 1:
        The solution to this problem will always result in the prefix and suffix form as follows:

            [0]*n + [1]*m where n and m lie in [0, length of string] and add to length of string.

        We can use this to find an answer in O(n) time, splitting the solutions into a left and right interval and
        choosing to flip 1's in the left interval to 0 and 0's in the right interval to 1.

            s = 11001

            i       left    left_flips        right         right_flips         total_flips

            0       []          0               [11001]         2                   2 *
            1       [1]         1               [1001]          2                   3
            2       [11]        2               [001]           2                   4
            3       [110]       2               [01]            1                   3
            4       [1100]      2               [1]             0                   2 *
            5       [11001]     3               []              0                   3

            So we see we get two solutions with a minimum of 2 flips at i=0 and i=4


    This solution will run in linear time, O(n), as it requires 2 total passes through the string, the first to find the
    number of 0's, and the second to pass to adjust the total flips for each character passing from suffix to prefix.
    We only require storing the left and right flips and the minimum solution, hench O(1) memory


    Solution 2: Dynamic
        Alternatively we can consider the fact that a monotonically increasing string will be constructed of prefix
        substrings that are also monotonically increasing, ie the prefix of length i is monotonically increasing if the
        prefix of length i-1 is monotonically increasing and s[i-1] = "1".

            If s[i-1] == "1" then dp[i] = dp[i-1]

            If s[i-1] == "0" then we must decide if we are to flip it to "1" or flip all the "1"'s to "0".


        e.g. s=11001

                i   num of 1's     s[i]       dp[i]
                0       0           -           0
                1       1           1           0
                2       2           1           0
                3       2           0           min(dp[2]+1, 2) = 1
                4       2           0           min(dp[3]+1, 2) = 2
                5       2           1           2


            In this way, you can see we have built up the final solution dp[-1]=2 using the optimal sub-solutions. We
            any time we find a 1, we add it to the count of 1's, and anytime we find a 0, we consider whether to flip
            it to 1, or flip all previous 1's to a 0. In this way we can build a solution in 1 pass rather than 2

"""


def monotone_flip(s):
    left = 0
    right = 0
    for ch in s:
        if ch == "0":
            right += 1
        elif ch != "1":
            print("Invalid character in string!")
            return
    sol = right
    for i in range(len(s)):
        if s[i] == "1":
            left += 1
        else:
            right -= 1
        if left + right < sol:
            sol = left + right
    return sol


def dynamic_monotone_flip(s):
    sol = 0
    ones = 0
    for i in range(len(s)):
        if s[i] == "1":
            ones += 1
        else:
            sol = min(sol + 1, ones)
    return sol

