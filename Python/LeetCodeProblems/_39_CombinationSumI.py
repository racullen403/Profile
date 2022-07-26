"""
Given a list of distinct integers and a target integer, return a list of all unique combinations of integers that
add to give the target. The same number may be used an unlimited amount of times.


Solution:

    - Note that because the integer list is made up of distinct integers, we do not need to sort the input.
    - We simply apply a Depth First Search approach, recursively building the up combinations until they either
    equal the target, or get too big and must be abandoned.
    - Each time we add an integer to the combination, we maintain its index since we can use the same integers more
    than once.


Dynamic Programming Solution:

    - This is quite a bit more complicated but removes the need for a recursive call.

    - We build a list that will contain everyone combination up to our target:

        dp =    [ [], [], [], [], [] ]   target = 4      candidates = [1, 3, 2, 5, 4]
                   0   1   2   3   4

    - Iterate through candidates, if the number is larger than target, skip it. If it is less than or equal to target,
    we can build up sub-solutions.

        i = 0, num = 1

        We iterate from 1 -> 4 in dp to create the sub-solutions as follows:


            j = 1,

                j == num so we simply add [1] as a solution to dp[1]

                dp =    [ [], [ [1] ], [], [], [] ]
                           0     1      2   3   4


            j = 2,

                we look at dp[j-num] = dp[1], this is [ [1] ], using these combinations to make up 1, we can simply
                add num=1 to them to make up combinations that give 2

                dp =    [ [], [ [1] ], [ [1,1] ], [], [] ]
                           0     1         2       3   4


            Continuing in this way would give the following

                dp =    [ [], [ [1] ], [ [1,1] ], [ [1,1,1] ], [ [1,1,1,1] ] ]
                           0     1         2           3             4


        We would now simply move to the next number, i=1, num=3, and continue as before

                dp =    [ [], [ [1] ], [ [1,1] ], [ [1,1,1], [3] ], [ [1,1,1,1], [1, 3] ] ]
                           0     1         2              3                    4


        i = 2, num = 2

                dp =    [ [], [ [1] ], [ [1,1], [2] ], [ [1,1,1], [3], [1,2] ], [ [1,1,1,1], [1, 3], [1,1,2], [2,2] ] ]
                           0     1            2                 3                             4

        etc...

    - Finally dp[-1] will return all combination that add to give target=4
"""


def combination_sum_1(candidates, target):
    combinations = []

    # Recursive DFS
    def find_combinations(tar, path, ind):
        if tar < 0:
            return
        elif tar == 0:
            combinations.append(path)
        else:
            for i in range(ind, len(candidates)):
                find_combinations(tar - candidates[i], path + [candidates[i]], i)

    find_combinations(target, [], 0)

    return combinations


def combination_sum_dynamic(candidates, target):
    dp = [[] for _ in range(target + 1)]
    for num in candidates:
        if num > target:
            continue
        for i in range(num, target+1):
            if i == num:
                dp[i].append([i])
            for combination in dp[i - num]:
                dp[i].append(combination + [num])
    return dp[-1]


