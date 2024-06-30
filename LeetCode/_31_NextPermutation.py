"""
Given some permutation of integers, we are tasked with finding the next lexicographical permutation.

    e.g [1, 4, 3, 2] -> [2, 1, 3, 4]
        [4, 3, 2, 1] -> [1, 2, 3, 4]


Solution:

    We can find a linear solution to this using 2 pointers.

    - First let l start at the final index, we move l left until we reach a term that decreases from the previous,
    this ensures all previous terms are in descending order (Note, if no decreasing term is found then we simply
    reverse the permutation). Occurs when a[i-1] < a[i]

    - Next we find the index of the smallest number, that is also greater than the l term, call this r  (only
    look to the right of l). Let r start r=len(a)-1, we move r-=1 until we find a[r] > a[l]

    - We swap terms at l and r, this maintains the decreasing order of terms from l+1 onwards, simply reverse these
    remaining terms, and you get the next permutations


    Example:

            Take    [4, 2, 5, 3, 1]

            The first decreasing term is l=1, since 2 < 5.

            The smallest term, that is bigger than 2 will be 3, so r=3.

            Swap l and r    [4, 3, 5, 2, 1]

            Reverse terms l+1 onwards   [4, 3, 1, 2, 5] DONE!


"""


def next_lex_perm(a):
    l = len(a)-1
    while l > 0 and a[l-1] >= a[l]:
        l -= 1
    l -= 1
    # Find swap index
    if l >= 0:
        swap = len(a)-1
        while a[swap] <= a[l]:
            swap -= 1
        a[swap], a[l] = a[l], a[swap]
    # Reverse Remaining
    r = len(a)-1
    l += 1
    while l < r:
        a[l], a[r] = a[r], a[l]
        l += 1
        r -= 1
    return a


# Cycle through permutations
def show_perm_order(nums):
    a = nums
    b = list(nums)
    count = 1
    print("1:", a)
    while a != next_lex_perm(b):
        count += 1
        print("{}:".format(count), b)


