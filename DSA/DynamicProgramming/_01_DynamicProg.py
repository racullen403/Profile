"""
Dynamic Programming is like the divide and conquer method, is solves a problem by combining the solutions to it's
sub-problems. Divide and conquer would partition the problem into disjoint sub-problems, and then solve them
recursively and combine the solutions. This differs from dynamic programming, this applies when the sub-problems
overlap and share "subsub-problems". If we applied a dived and conquer method to this, we would end up doing more work
than necessary by repeatedly solving the common "subsub-problems". Dynamic programming will solve each "subsub-problem"
just once and save the answer, avoiding recomputing the answer every time it solves the "subsub-problem".

We typically apply DP to optimisation problems, where a problem can have many solutions, and we wish to find one that
is optimal.

In general, applying dp has 4 main steps:
    - Characterise the structure of an optimal solution
    - Recursively define the value of an optimal solution
    - Compute value of an optimal solution
    - Construct the solution from the computed information

The two key ingredients that an optimisation problem must have in order for dp is the optimal substructure and the
overlapping sub-problems.
    - We must first characterise the structure of an optimal solution such that the optimal solution contains within
    it the optimal solutions of its sub-problems, we say it exhibits optimal substructure.
    - Secondly, the recursive algorithm for the problem revisits the same problem repeatedly, having overlapping
    subproblems.
"""