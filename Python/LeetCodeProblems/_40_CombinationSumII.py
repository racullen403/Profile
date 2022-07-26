"""
Given a collection of integers, "candidates", and a target number "target", find all unique combinations of numbers in
candidates that sum to give target. We may only use each number once (note, if there are 2 of the same number, you may
use 2 of that number).


Solution:

    - Solution is very similar to _39_CombinationSumI, using a recursive DFS.
    - The main difference is that the integers are not unique in this case, and we can only use each integer once.
    - We sort the list, candidates, this way we can avoid creating duplicate combinations by checking
    candidates[i] != candidates[i-1].

"""


def combination_sum_2(candidates, target):
    candidates.sort()
    combinations = []

    # DFS recursion
    def find_combinations(ind, path, tar):
        if tar == 0:
            combinations.append(path)
        else:
            for i in range(ind, len(candidates)):
                if candidates[i] > tar:
                    return
                if i == ind or candidates[i] != candidates[i - 1]:
                    find_combinations(i + 1, path + [candidates[i]], tar - candidates[i])

    find_combinations(0, [], target)

    return combinations

