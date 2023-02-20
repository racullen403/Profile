"""
Given an array on integers, we want to calculate the total sum of all the minimum values of all the sub arrays.

    e.g. arr = [3, 4, 1]

        sub-arrays = [3, 4, 1], [3, 4], [4, 1], [3], [4], [1]

        minimums = 1, 3, 1, 3, 4, 1   <- This is the sum we want


Solution:
    - We can find the answer to this in O(n) time using a data structure called a monotone stack.

    Monotone Stack:
        - This structure tells us what an elements next lesser element is, and what its previous lesser element is,
        in O(n) time.
        - We use the basic idea of finding the monotonically increasing elements

            def monotone_increase(arr):
                stack = []
                for i in range(len(arr)):
                    while len(stack) and arr[stack[-1]] > arr[i]:
                        stack.pop()
                    stack.append(i)

        - We now create 2 auxiliary arrays ple and nle (previous/next lesser element arrays), where index i represents
        the element in the starting array at i, and the value stored at index i indicates the index of the next or
        previous lesser element.

        - Once we have our ple and nle arrays, we can use them to find our solutions as follows:

            Let arr = [2, 9, 7, 8, 3, 4, 6, 1]

                nle = [7, 2, 4, 4, 7, 7, 7, 7]

                ple = [0, 0, 0, 2, 0, 4, 5, 7]


            Now consider element 3, index 4. The nle[4] = 7 and ple[4] = 0

            This tells us 3 is the minimum from index 4 -> 6 and from index 1 -> 4. We consider both these separately


                We have [9, 7, 8]  [3] and [4, 6], now consider

                    [9, 7, 8]       [3]     [4, 6]

                    [7, 8]                  [4]

                    [8]                     []

                    []

                the left and right lists are all the possible combinations either side of [3] that will make up a
                valid subarray whose minimum is 3.

                    i.e 4*3 which are the lengths from 3 to the next lesser element in either direction, including 3.

            We simply iterate this process over the whole array, and multiply each number of combinations by the
            respective minimum, to get the total sum of minimums.


            NOTE: we use -1 to represent where the nle or ple is the index of the element itself, indicating it
            has no next or previous lesser element. This allows us to also calculate the distances more easily.

"""


class MonotoneStack:

    def __init__(self, arr):
        self.arr = arr
        self.ple = self.create_ple()
        self.nle = self.create_nle()
        self.solution = self.solve()

    def create_ple(self):
        arr = self.arr
        stack = []
        output = [-1] * len(arr)  # If element has no previous lesser, then it stretches left to -1
        for i in range(len(arr)):
            while len(stack) and arr[stack[-1]] > arr[i]:
                stack.pop()
            if len(stack):
                output[i] = stack[-1]
            stack.append(i)
        return output

    def create_nle(self):
        arr = self.arr
        stack = []
        output = [len(arr)] * len(arr)  # If element has no next lesser, then it stretches right to len(arr)
        for i in range(len(arr)):
            while len(stack) and arr[stack[-1]] > arr[i]:
                output[stack.pop()] = i
            stack.append(i)
        return output

    def solve(self):
        total = 0
        arr = self.arr
        for i in range(len(arr)):
            l_dis = i - self.ple[i]
            r_dis = self.nle[i] - i
            combinations = l_dis * r_dis
            total += combinations * arr[i]
        return total

    def show(self):
        print("Input Array:", self.arr)
        print("PLE:", self.ple)
        print("NLE:", self.nle)
        print("Total Sum of the Minimums of all Sub-Arrays:", self.solution)


def example():
    arr = [2, 9, 7, 8, 1, 3, 4, 6]
    sol = MonotoneStack(arr)
    sol.show()


