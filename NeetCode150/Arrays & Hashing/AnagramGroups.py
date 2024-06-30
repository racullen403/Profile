def groupAnagrams(strs):
    
    # Medium: we turn each string into an array of length 26 for 
    # each lower case letter and add counts, convert to tuple and 
    # use as key to contain list of similar strings. O(m * n)

    lookup = {}

    for s in strs:
        counts = [0] * 26 
        for ch in s:
            i = ord(ch) - ord("a")
            counts[i] += 1

        a = tuple(counts)
        if a not in lookup:
            lookup[a] = []
        lookup[a].append(s)

    return lookup.values()

    

    
