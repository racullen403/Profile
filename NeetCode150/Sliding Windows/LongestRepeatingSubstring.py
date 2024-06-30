def characterReplacement(s, k):
    # Medium: We keep track of the counts of each letter within a given window, and the largest count
    # we have found so far. From here, all we have to do is take this max count from the size of the 
    # window, if it is more than k, then we know we have to replace more than k so is invalid, therfore,
    # move left point forward until window is valid again.
    l = 0 
    maxf = 0 
    res = 0 
    count = {} 
    for r in range(len(s)):
        count[s[r]] = 1 + count.get(s[r], 0)
        maxf = max(maxf, count[s[r]])
        while (r - l + 1) - maxf > k:
            count[s[l]] -= 1
            l += 1
        res = max(res, r - l + 1)
    return res