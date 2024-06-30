"""
Consider the problem of finding change for a vending machine.

The typical solution is to use a greedy algorithm, we find how many of the largest coin
to return, then the next largest, and so on until we have the correct change. This method
will not always give the optimal solution depending on the coins that exist.

Note in the below example, if we were to have a 8p coin, instead of returning 2 8p coins
for change of 16, our algorithm would return 10, 5, 1 which is not the optimal solution.
"""


# greedy algorithm, tries the largest coin first, then moves to smaller coins
def find_change(amount, coins=None):
    if coins is None:
        coins = [10, 5, 2, 1]
    for coin in coins:
        if coin == amount:
            return [coin]
        if coin < amount:
            largest_coin = coin
            return [largest_coin] + find_change(amount-largest_coin)


# Example of greedy algorithm
def example1():
    print("\n----Greedy Method----")
    for change in range(1, 17):
        print("Making change for {}:".format(change), find_change(change))


"""
To ensure we always get the optimal solution, we cannot stop when the first solution is 
found via the greedy method. A better solution might be to store our known results in 
memory, this way we can continue on to see if there are potentially more solutions
using less coins.
"""


def find_optimal_change(amount, coins=None):
    if coins is None:
        coins = [10, 8, 5, 2, 1]
    optimal_solution = None
    coins_used = amount
    for coin in coins:
        if amount == coin:
            return [coin]
        if coin < amount:
            potential_solution = [coin] + find_optimal_change(amount-coin)
            if len(potential_solution) < coins_used:
                optimal_solution = potential_solution
                coins_used = len(optimal_solution)
    return optimal_solution


# Example using a Cache to store optimum solution
def example2():
    print("\n----Optimal Solution using Cache----")
    for change in range(1, 17):
        print("Making change for {}:".format(change), find_optimal_change(change))


""" 
Now we will consider the dynamic programming way of solving this problem. This will work in 
a systematic way, working our way up from 1p to the desired amount of change we want. This 
will guarantee that at every step of the algorithm we already know the optimum change for 
some smaller amount.

How it works below:

    We initially create a dictionary of just the single coins:
    
        dic =   {   1: [1]
                    2: [2]
                    5: [5]
                    8: [8]
                    10:[10]
                }
                
    We then iterate from 1 ---> amount of change that is due, say 13
    
    If the iterable is not in the dictionary then we must add it with its minimum change 
    list.
    
    The first case would be 3:
    
        - set the potential change list to the previous change list + coin [1]
        
        - hence potentially the solution is 3: [2, 1]
        
        - now for coins smaller than 3, we have to see if any change list + said coin 
        would be smaller, so for coins [1] and [2] this is not the case hence we use this 
        potential solution as the actual solution 
        
        dic =   {   1: [1]
                    2: [2]
                    3: [2,1]
                    5: [5]
                    8: [8]
                    10:[10]
                }
    
    Continuing on, we get 4 which is not in the dictionary:
    
        - set 4: [2,1,1]
        - for coins smaller than 4 we do our comparisons
        - [1], we look at 3, this would be the same length so ignore
        - [2], we look at 2, this would give potential change list [2,2] which is smaller 
        than [2,1,1], hence we reassign to our potential solution.
        - there are no more coins smaller than 4 so we have our answer
        
    dic =   {   1: [1]
                2: [2]
                3: [2,1]
                4: [2,2]
                5: [5]
                8: [8]
                10:[10]
                }
        
    We continue in this way, building up the dictionary with all the optimal solutions for 
    every potential change amount, using previous values, until we reach our desire amount.
    
"""


def dp_find_change(amount, coins_used=None):
    # Setup
    coins = coins_used
    if coins is None:
        coins = [1, 2, 5, 8, 10]
    min_change = {}
    for coin in coins:
        min_change[coin] = [coin]
    # Execution
    for change in range(1, amount+1):
        if change not in min_change.keys():
            potential_min_change = min_change[change - coins[0]] + [coins[0]]
            for coin in coins:
                if coin <= change:
                    if len(min_change[change-coin]) < len(potential_min_change):
                        potential_min_change = min_change[change-coin] + [coin]
            min_change[change] = potential_min_change
    return min_change[amount]


# Example of dynamic program:
def example3():
    print("\n----Optimal Solution using DP----")
    for change in range(1, 17):
        print("Making change for {}:".format(change), dp_find_change(change))

