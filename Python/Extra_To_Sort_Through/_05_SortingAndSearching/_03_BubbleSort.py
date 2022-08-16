""" 
Bubble Sort makes multiple passes through a list, comparing adjacent items and exchanging 
those that are out of order. Essentially each pass will place the next largest item in 
its correct place.
 
    E.G
    
        4, 2, 5, 3, 1   Compare 4 > 2, swap 
        2, 4, 5, 3, 1   Compare 4 < 5 correct, compare 5 > 3 swap 
        2, 4, 3, 5, 1   Compare 5 > 1 swap 
        2, 4, 3, 1, 5,  So we see 5 has "bubbled" its way to the correct position  
        
        Now we do another pass and we would expect the the next largest, 4, to do the 
        same 
        
        2, 4, 3, 1, 5   Compare 2 < 4 correct, compare 4 > 3 swap 
        2, 3, 4, 1, 5   Compare 4 > 1 swap 
        2, 3, 1, 4, 5   We can end comparison here at (n-1) items since 5 has been done
        
        2, 3, 1, 4, 5   Compare 2 < 3 correct, compare 3 > 1 swap 
        2, 1, 3, 4, 5   End comparison now at (n-2) items 
        
        2, 1, 3, 4, 5 Compare 2 > 1 swap 
        1, 2, 3, 4, 5 We can end now since there is only 1 item left.
        
In worst case, the list would be in reverse order, meaning we would have to make O(n^2)
comparisons to sort the list, ie n on first pass, n-1 on next, n-2, ...

Since Bubble Sort can require up to n passes through the list to sort it, we consider it
to be a very inefficient sorting algorithm. However, it has the advantage that it
can tell when a list is sorted already sorted and terminate early.
        
"""

# Standard n passes method
def bubble_sort1(alist):
    for last_index in range(len(alist)-1, 0, -1):
        for i in range(last_index):
            if alist[i] > alist[i+1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]
    return alist


# Method to end as soon as the sort is completed, <=n passes
def bubble_sort2(alist):
    for last_index in range(len(alist)-1, 0, -1):
        swap = False
        for i in range(last_index):
            if alist[i] > alist[i+1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]
                swap = True
        if swap is False:
            return alist
    return alist
