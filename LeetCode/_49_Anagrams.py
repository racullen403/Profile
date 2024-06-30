"""
Given and list of strings, group them by anagrams.

    Solution 1:
        - We sort each string, and use this sorted string as the key for a hashmap that will store the groupings
        - Note that in this case, sorting each of the strings is what will dominate the time complexity as looking
        up in a hashmap is O(1).


    Solution 2:
        - We can speed up this hashing solution by using Prime Numbers, this is because any number can be uniquely
        expressed by its primefactors, meaning, if we assign a unique prime number for each letter a-z, then, any sting
        that is an anagram, will have the same primefactors, and so multiply to give the same key for out hashmap.

        e.g.   a, b, c which is represented by the first 3 primes, 2, 3, 5

                then any combination, abc, acb, bac, bca cab, cba will always multiply to 2*3*5=30

        - This gets rid of the need to sort, greatly speeding up the algorithm to O(n)

"""


# Sort the strings and use as the key in hashmap
def group_by_anagram_1(strings):
    lookup = {}
    for s in strings:
        sorted_word = "".join(sorted(s))
        if sorted_word not in lookup:
            lookup[sorted_word] = []
        lookup[sorted_word].append(s)
    return lookup.values()


# Grouping using prime factors
def group_by_anagrams_primes(strings):
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
    count = 0
    letters = {}
    output = {}
    for s in strings:
        total = 1
        for l in s:
            if l not in letters:
                letters[l] = primes[count]
                count += 1
            total *= letters[l]
        if total not in output:
            output[total] = []
        output[total].append(s)
    return output.values()


st = ["eat", "tan", "ate", "tea", "bat", "nat"]
print(group_by_anagram_1(st))
print(group_by_anagrams_primes(st))

