"""
We want to calculate the minimum cost to travel on each of the days given in a list "days", we are given the costs
for a 1-day, 7-day and 30-day pass

Solution:
    - We keep track of the total cost for all days, even non-travel days which would remain the same as the previous
    day, this helps us set up our dynamic program.
    - We consider at each travel day the options:
        - The previous days cost + 1 day pass
        - 7 days ago cost + 7-day pass
        - 30 days ago cost + 30 day pass
    - We choose the minimum cost and add it to the dp, then move to next day.

"""


def min_cost_for_tickets(days, costs):
    if len(days) < 1:
        return
    dp = [0 for _ in range(days[-1] + 1)]
    day = 0
    for i in range(len(dp)):
        if i < days[day]:
            dp[i] = dp[i-1]
        else:
            m_cost = dp[i-1] + costs[0]
            seven = i - 7
            thirty = i - 30
            if seven < 0:
                seven = 0
            if thirty < 0:
                thirty = 0
            m_cost = min(m_cost, dp[seven] + costs[1], dp[thirty] + costs[2])
            dp[i] = m_cost
            day += 1

    print("Days:", days)
    print("Costs:", costs)
    print("DP:", dp)

    return dp[-1]


def example1():
    d = [1, 4, 6, 7, 8, 20]
    c = [2, 7, 15]
    min_cost_for_tickets(d, c)


example1()

