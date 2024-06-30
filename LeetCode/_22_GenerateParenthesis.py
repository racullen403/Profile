"""
We are tasked with generating every possible set of valid parenthesis given the
number of pairs n:

e.g     n = 0       ...

        n = 1       ()

        n = 2       ()(), (())

        n = 3       ()()(), ()(()), (())(), ((())), (()())


Solution, DFS:
    - We solve using depth first search
    - Think of the parenthesis generation as a binary tree, either adding "(" or ")"
    - If the number of opening parenthesis is ever less than the closing, or, if we have more than n opening
    parenthesis, then we know the solution is no longer valid and can abandon that branch.
    - When we end up with the conditions for a valid solution, we insert that solution into
    the output that is retained in the recursion.


Solution, Dynamic:
    - We can create new solutions using previously found solutions

    0:

    1: ()

    2: (()), ()()

    3: ((())), (()()), (())(), ()(()), ()()()


        - We can see a pattern here:

            1   ->  ( + 0 + ) + 0 == ()

            2   ->  ( + 0 + ) + 1 == ()()
                    ( + 1 + ) + 0 == (())

            3   ->  ( + 0 + ) + 2 == ()(()) and ()()()
                    ( + 1 + ) + 1 == (())()
                    ( + 2 + ) + 0 == ((())) and (()())

            4   ->  ( + 0 + ) + 3 == ()((())), ()(()()), ()(())(), ()()(()), ()()()()
                    ( + 1 + ) + 2 == (())(()), (())()()
                    ( + 2 + ) + 1 == ((()))(), (()())()
                    ( + 3 + ) + 0 == (((()))), ((()())), ((())()), (()(())), (()()())

        - For the nth group,  ( + ith group + ) + n-i-1 group, in which we may need to iterate through terms for each
        item in the groups

        - Essentially all we are doing is putting () around the ith group and adding it to n-i-1 group, this ensures
        there will be n pairs of well-formed parenthesis, and we are always creating a new unique pattern.

"""


# Solution 1, Recursion
def generate_n_pairs(n):
    output = []
    dfs_brackets(n, "", 0, 0, output)
    return output


def dfs_brackets(n, path, i, j, solutions):
    if i > n or i < j:
        return
    elif i == n and j == n:
        solutions.append(path)
    else:
        dfs_brackets(n, path + "(", i + 1, j, solutions)
        dfs_brackets(n, path + ")", i, j + 1, solutions)


# Solution 2, Dynamic
def dynamic_n_patterns(n):
    # Start with level 0: ""
    dp = [[""]]
    # Iterate to desired level N
    for i in range(1, n+1):
        new_pats = []
        # Iterate through all our current levels
        for level in range(len(dp)):
            # Iterate through every pattern in the level
            for pat1 in dp[level]:
                # Create the new prefix
                new_prefix = "(" + pat1 + ")"
                # Iterate through every pattern in the N-i-l Level and add it to the prefix
                # then add this pattern into our new Nth level
                for pat2 in dp[i-level-1]:
                    new_pats.append(new_prefix + pat2)
        # Add this Nth level into the dp, to be used to create the N+1 level
        dp.append(new_pats)
    return dp[-1]

