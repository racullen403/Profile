"""
We are given two sorted lists of integers and asked to find the median of them.

Median has two key properties in this case:
    - We should have 2 lists either side of the median that are equal length
    - All terms in the left list should be less than terms in the right list

Consider:
    - Take some sorted list of length m, A = [a0, a1, ... , am-1]
    - We can cut this list in m+1 positions, i=0 will be in front of a0 and i=1
    will be in front of a1 and so on until i=m which will be after am-1.
    - Cutting the list will create a left and right list about the cut at
    position i

        A_left = [a0, a1, ..., ai-1]
        A_right = [ai, ai+1, ..., am-1]

    - Now take a second sorted list of length n and cut it at some position j

        B_left = [b0, b1, ..., bj-1]
        B_right = [bj, bj+1, ..., bn-1]

    - Let A_left and B-left be the left set and A_right and B_right be the
    right set

                Left Set                                Right Set

        A_left = [a0, a1, ..., ai-1]            A_right = [ai, ai+1, ..., am-1]
        B_left = [b0, b1, ..., bj-1]            B_right = [bj, bj+1, ..., bn-1]

    - If we can ensure that the length of the left set is the same as the length
    of the right set, and that the max of the left set is less than the min of
    the right set, then we have found the median position.


    1) First condition, equal list lengths:

        left set length = i+j
        right set length = (m-i) + (n-j)
        so we require i+j == (m-i) + (n-j)

        NOTE: this only can work if the sets are both even or both odd lengths, if one
        is even and one is odd then we require i+j==(m-i)+(n-j)+1, this means the left
        set will have 1 extra term in it which will be the median under the right conditions.

        We set the smaller list as A and i will be some value in range of 0-m while
        j is found as follows

            j = (m+n+1)//2 - i

        NOTE: we start with i=imin+imax//2, and adjust the searching range [imin:imax]
        based on the second condition, this way we can move the cut in the smaller
        list using a binary search method as we know it's sorted (we can ditch half
        the remaining cut positions at a time until we find the right position)

    2) Second condition:

        ai-1 <= bj AND bj-1 <= ai

        This ensures that the max(left set) <= min(right set)


Edge Cases:

    When i=0, i=m, j=0 or j=n, technically the cut would be at the at one of the
    following indices, -1, m, n, none of these actually exist as index positions.

    This has effect when we want to compare ai-1 <= bj and bj-1 <= ai.

    Now if i and j aren't edge cases we have seen that we need to check both of
    the above cases. But if we have one or both of the edge case with i and j, then
    we may not have to look at one or both of the cases above.

    If (j==0 or i==m or bj-1 <= ai) AND (i==0 or j==n or ai-1 <= bj) them i is
    perfect and we have found the cut

    If j>0 and i<m and bj-1 > ai then i was too small and must be increased

    If i>0 and j<n and ai-1 > bj then i is too large and must be decreased.

"""


def median_of_two_sorted_lists(A, B):
    # 1) Setup
    m = len(A)
    n = len(B)
    if n < m:
        # Swap lists about to ensure A is the smaller one
        A, B, m, n = B, A, n, m
    if m == 0:
        # First list is empty (remember it is smaller)
        if n == 0:
            # Second list is empty
            raise ValueError
        else:
            # Do normal median on second list
            if n % 2 == 1:
                return B[n//2]
            else:
                return (B[n//2] + B[n//2 - 1]) / 2
    # 2) Execution
    imin = 0
    imax = m
    while imin <= imax:
        # the left set will include 1 extra term in the case of odd number of values
        i = (imin + imax) // 2
        j = ((m + n + 1) // 2) - i
        if i > 0 and A[i-1] > B[j]:
            # Condition 2 is not satisfied, A[i-1] is too large,
            # we must move the cut left
            imax = i-1
        elif i < m and A[i] < B[j-1]:
            # Condition 2 not satisfied, A[i] is too small, we must
            # move the cut right
            imin = i+1
        else:
            # Our Conditions are satisfied and cut is in the correct position, we
            # now must deal with edge cases
            if i == 0:
                max_left = B[j-1]
            elif j == 0:
                max_left = A[i-1]
            else:
                max_left = max(A[i-1], B[j-1])
            # When we have an uneven number of elements, the median is stored to the
            # left of the cut
            if (m + n) % 2 == 1:
                return max_left
            else:
                if i == m:
                    min_right = B[j]
                elif j == n:
                    min_right = A[i]
                else:
                    min_right = min(A[i], B[j])
                return (min_right + max_left)/2.0
