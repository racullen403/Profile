"""
Given sequence of n terms, we want to find the kth permutation of the sequence.

    e.g. n = 4 tells us [1, 2, 3, 4] and k = 9 tells us to find the 9th permutation

            k=1 1234    k=7 2134
            k=2 1243    k=8 2143
            k=3 1324    k=9 2314
            k=4 1342    k=10 2341
            k=5 1423
            k=6 1432

Solution:
    - Consider for some given first term in the sequence, we know there will be (n-1)! permutations. This means for the
    kth permutation we have

        i * (n-1)! < k <= (i+1) * (n-1)!, where i will be the sequence term

        e.g n=4 and k=9, we get 6i < 9 <= 6i + 6, so i=1 tells us the term at index 1 is our first term

            2 _ _ _

            now we reduce our terms to [1, 3, 4], where n=3 and k=3 (from 9 - 6)

                2i < k=3 <= 2i + 2, so i=1, tells us index 1 gives the second term of our sequence

            2 3 _ _

            now reduce terms [1, 4], n=2, k=1  (from 3-2)

                i < k=1 <= i + 1, i=0 will give the solution, so index 0 gives the third term

            2 3 1 _

            now reduce terms [4], we only have 1 term so add it

            2 3 1 4

    - By this process, we can find the kth permutation of a sequence of n terms on O(n) time

"""


def find_kth_permutation(n, k):
    sequence = [i for i in range(1, n+1)]
    numbers = []

    def factorial(n):
        if n == 0:
            return 1
        return n * factorial(n-1)

    while n > 1:
        count = 0
        fact = factorial(n-1)
        while k > fact:
            k -= fact
            count += 1
            fact = factorial(n-1)
        numbers.append(sequence[count])
        sequence.pop(count)
        n -= 1
    numbers.append(sequence[0])

    return numbers


print(find_kth_permutation(4, 9))
