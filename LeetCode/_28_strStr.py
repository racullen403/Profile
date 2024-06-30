"""
We are asked to find the index of the start of a sub-string pattern within the full string.


Solution, Brute force:
    - Iterate through entire string, until you find the first letter of the sub-string
    - Compare to the sub string, if wrong, continue iterating
    - In worst case this would be O(M*N) where n is length of string and m is length of substring


Solution 2, KMP:
    - This algorithm makes use of the proper prefix and proper suffix in each sub-pattern to allow us to find the
    sub-string in O(N) time.

    - Proper Prefix: All letter with 1 or more cut off end, "word" will have "w", "wo", "wor"

    - Proper Suffix: All letters with 1 or more cut off from front, "word" will have "d", "rd", "ord"

    - We need to pre-process our substring, where at each index, we concern ourselves only with the letters up to and
    including the index, and input the length of the longest proper prefix that is the same as the proper suffix.

        e.g.    Take "abbaabba",

                Characters  [ a, b, b, a, a ,b, b, a ]
                Index       [ 0, 1, 2, 3, 4 ,5, 6, 7 ]
                kmp         [ 0, 0, 0, 1, 1, 2, 3, 4 ]

                - We iterate through the pattern with i and let j be the current character we are comparing to,
                always starting with kmp[0] = 0, i = 1, and j = 0
                - If ch[i] = ch[j], then there is a prefix of length j+1 and suffix of length 1 so kmp[i] = j+1,
                now let j += 1 and i += 1
                - If ch[i] != ch[j] and j > 0, then we must set j = kmp[j-1] else we set the kmp[i] = 0

    - Now that we can create the list of values, we go through the string comparing its characters to the characters
    in the sub-string.

        - If we get through all the sub-string letters then we have found the solution
        - If we reach a point where the patterns break, we look at val[j-1], this tells us the number of previous
        characters that could still make up the sub-pattern to this point, and so we compare the current character
        to the val[j-1] character in the subpattern

        e.g.    Word:   l, e, e, l, e, e, l, e, e, t
                ind:    0, 1, 2, 3, 4, 5, 6, 7, 8, 9 (i)

                find:   l, e, e, l, e, e, t
                ind:    0, 1, 2, 3, 4, 5, 6 (j)
                val:    0, 0, 0, 1, 2, 3, 0

                We would make our way through the word until we get to:

                    i = 6 and j = 6 where we want to find "t" but instead find "l"

                    check val(j-1) = val(5) = 3

                    set j = 3 and compare word[i] == find[j], they are equal, so we can continue the iteration from
                    j+1. If they weren't, then we would set j = 0 and continue the iteration
"""


def find_substring_kmp(word, find):
    kmp = [0]*len(find)
    i = 1
    j = 0
    while i < len(find):
        if find[i] == find[j]:
            kmp[i] = j+1
            j += 1
            i += 1
        elif j > 0:
            j = kmp[j-1]
        else:
            i += 1
    j = 0
    i = 0
    while i < len(word):
        if word[i] == find[j]:
            i += 1
            j += 1
            if j == len(find):
                return i-len(find)
        elif j > 0:
            j = kmp[j-1]
        else:
            i += 1
    return -1
