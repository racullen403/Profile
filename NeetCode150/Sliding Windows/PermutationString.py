def checkInclusion(s1, s2):
    # Medium: We move a sliding window of size s2 through s1 to check all permutations. This can be done 
    # in 2 ways. First, store array size 26 to map to all the letters for both s1 and s2, then count the 
    # indices that match, update as we move our window across, if at any point we get 26 matches, we know
    # that window is a permutation.
    #
    # The cooler maths way is to map all letters to unique prime numbers, any two permutations will have 
    # the same unique product by mathematical proof.
    if len(s2) < len(s1):
        return False
    a = [0]*26
    b = [0]*26
    for i in range(len(s1)):
        a[ord(s1[i]) - ord("a")] += 1
        b[ord(s2[i]) - ord("a")] += 1 
    matches = 0
    for i in range(26):
        if a[i] == b[i]:
            matches += 1
    l = 0
    for r in range(len(s1), len(s2)):
        if matches == 26:
            return True 
        i = ord(s2[r]) - ord("a")

        b[i] += 1
        if a[i] == b[i]:
            matches += 1
        elif a[i] + 1 == b[i]:
            matches -= 1

        j = ord(s2[l]) - ord("a")
        b[j] -= 1
        if b[j] == a[j]:
            matches += 1
        elif b[j] + 1 == a[j]:
            matches -= 1
        
        l += 1

    return matches == 26


