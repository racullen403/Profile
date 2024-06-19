"""
We know that in worst case, Quicksort can end up with an O(n^2) run time.

We can improve on Quicksort to make the expected run time be O(nlogn) by using random selection of pivot elements. We
simply pick a random index between l and r and swap it to the right most position, then apply our normal partition
algorithm as before. (this is trivial if we know how to do quicksort already).

To achieve the worst case O(nlogn) time complexity, we find the median of the segment being sorted and pivot about this
element. However, in practice this is too slow.
"""