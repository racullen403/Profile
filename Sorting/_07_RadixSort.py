"""
Radix Sort:

    Works by first grouping objects by their individual digits of the same place value (if place value doesn't exist,
    we take it as 0), then sort objects according order.

    E.G     [121, 432, 564, 23, 1, 45, 788]

            - We would sort by the unit place, then the 10's place, then the 100's place.

            - First find the largest number, and let x be the number of digits in it.

            - Now, go through the places one by one, using a "STABLE" sorting method, e.g. count_sort

            - Repeat for each position until we have done them all


Time Complexity:
    In our case it would be O(d*(n+k)) where d is the number of digits in the largest number, and n+k is the time
    complexity of the counting sort method. Note that this is better than the O(nlogn) of comparative methods.

Space Complexity:
    We require O(n+k) like in count sort, again for large numbers, k will dominate.

Radix sort is non-comparative and stable, it is faster than typical O(nlogn) methods, however, it is still very
inefficient with space as large 32-bit or 64-bit numbers will require huge amounts of memory and for that reason
it is not typically used in software libraries.
"""


def radix_sort(arr):
    m = 0
    for obj in arr:  # Find Largest value
        if obj > m:
            m = obj
    dig = 0
    while m != 0:  # Find number of digits in the largest obj
        dig += 1
        m //= 10
    d = 0
    initial_arr = arr
    while d < dig:  # Sort based on digit position, using count sort
        aux = [0]*10  # There are 10 digits max
        for obj in initial_arr:  # Count up digit occurrences
            digit = (obj // (10**d)) % 10  # Calculates digit at required position
            aux[digit] += 1
        for i in range(1, 10):  # Convert to cumulative counts
            aux[i] += aux[i-1]
        new_arr = [0] * len(initial_arr)
        for i in range(len(initial_arr)-1, -1, -1):  # Sort using counts
            digit = (initial_arr[i] // (10**d)) % 10
            new_arr[aux[digit]-1] = initial_arr[i]
            aux[digit] -= 1
        initial_arr = new_arr  # Initialise the array to be used again in the next loop
        d += 1
    return initial_arr


def radix_sort_show(arr):
    m = 0
    for obj in arr:
        if obj > m:
            m = obj
    print("\nLargest object:", m)
    dig = 0
    while m != 0:
        dig += 1
        m //= 10
    print("Number digits:", dig, "\n")
    d = 0
    initial_arr = arr
    while d < dig:
        print("  Digit pos", d)
        print("  Starting Array", initial_arr, "\n")
        aux = [0]*10
        for obj in initial_arr:
            digit = (obj // (10**d)) % 10
            aux[digit] += 1
        print("    Aux =", aux)
        for i in range(1, 10):
            aux[i] += aux[i-1]
        print("    Cumulative Counts, aux =", aux, "\n")
        new_arr = [0] * len(initial_arr)
        for i in range(len(initial_arr)-1, -1, -1):
            digit = (initial_arr[i] // (10**d)) % 10
            new_arr[aux[digit]-1] = initial_arr[i]
            aux[digit] -= 1
            print("    Output:", new_arr)
        print()
        initial_arr = new_arr
        d += 1
    print("Sorted Array:", initial_arr)


def example1():
    a = [121, 432, 564, 23, 1, 45, 788]
    radix_sort_show(a)


example1()