"""
IntroSort:

    There is a sort known as "IntroSort" which combines both the QuickSort and HeapSort to provide fast average
    performance and optimal worst case performance. It works by starting with QuickSort and switching to HeapSort when
    a recursion depth exceeds a level based on the logn, it will also switch to InsertionSort when the number of
    elements is below some threshold. This makes its worst case O(nlogn) instead of that of Quicksort O(n^2). It also
    uses 3 comparison sorts and so is a comparison sort itself, it is however in place and not Stable.

"""