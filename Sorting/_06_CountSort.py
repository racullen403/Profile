"""
Count Sort:

    Count sort stores the number of occurrences of unique object in an auxiliary array, and uses it to map the count
    of an object to its position in a new array.


    E.G Consider [1, 4, 5, 1, 2, 1, 5, 3]

        - We find the largest number, max=5, auxiliary array = [0, 0, 0, 0, 0, 0] (length is 6 to include 0)

        - Add counts for each object, stored at the corresponding index given by the object

            [0, 3, 1, 1, 1, 2]
             0  1  2  3  4  5

        - Convert auxiliary array to cumulative counts

            [0, 3, 4, 5, 6, 8]

        - Create a new output array of the same length as the input array

            [0, 0, 0, 0, 0, 0, 0, 0]

        - Iterating through the input array in reverse (this ensures stability), we take the object=3, go to index 3 in
        the auxiliary array, which is 5, we place object=3 at the 5th position, 4th index. Subtract 1 from the count
        for 3.

            [0, 0, 0, 0, 4, 0, 0, 0] and aux=[0, 3, 4, 5, 5, 8]


        - Repeat for whole input array [1, 4, 5, 1, 2, 1, 5, 3]


        DONE!


Space Complexity is O(m+n) where n is the length of the new output array and m is the length of the auxiliary
array for storing the counts.

Time Complexity O(m+n), where n is the length of the input array and m is the length of the counts array (we must
iterate through it to create the cumulative counts).


Advantages to this method is there are no comparisons taking place which saves a lot of time.

Disadvantages are that we may have to create enormous arrays for holding counts, where most of the indexes may be
empty, as the max number in the input increases, the complexity tends towards O(m).

    - We could get around this by storing counts in a dictionary, then sorting its keys and using them to form the
    cumulative count's dictionary. From here we could just continue like before.
    - This method could cut down on memory requirements massively, however we would need to apply another sorting
    algorithm to the unique objects (keys in the dictionary) which may defeat the purpose, as we are relying on a
    secondary sort method.

"""


def count_sort(arr):
    # Find largest number m
    m = 0
    for obj in arr:
        if obj > m:
            m = obj
    m += 1
    # Add up counts
    aux = [0] * m
    for obj in arr:
        aux[obj] += 1
    # Convert counts to cumulative counts
    for i in range(1, m):
        aux[i] += aux[i-1]
    # Place objects into new output array
    output = [0]*len(arr)
    for i in range(len(arr)-1, -1, -1):
        output[aux[arr[i]]-1] = arr[i]
        aux[arr[i]] -= 1
    # Sort is not in place, so we must return the output
    return output


def count_sort_show(arr):
    print("\nOriginal Array:", arr, "\n")
    m = 0
    for obj in arr:
        if obj > m:
            m = obj
    m += 1
    print("  m =", m)
    aux = [0] * m
    for obj in arr:
        aux[obj] += 1
    for i in range(1, m):
        aux[i] += aux[i-1]
    print("  Cumulative Counts, aux =", aux)
    output = [0]*len(arr)
    print("\n    Starting Output:", output, "\n")
    for i in range(len(arr)-1, -1, -1):
        print("      Place object={}".format(arr[i]), " position={}".format(aux[arr[i]]-1), end=" ")
        output[aux[arr[i]]-1] = arr[i]
        print("  New Output:", output)
        aux[arr[i]] -= 1
    print("\n    Sorted Array:", output)


def example1():
    a = [1, 4, 5, 1, 2, 1, 5, 3]
    count_sort_show(a)

