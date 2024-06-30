def minWindow(s, t):
    # Hard: we simply keep track of the counts of characters in r and make comparisons to the counts
    # of characters in s, within the given window. We track how many matches we have, once we find a 
    # substring, update size, then slide left window pointer in until we no longer have the required 
    # matches.
    tc = {}
    sc = {}
    for ch in t:
        tc[ch] = 1 + tc.get(ch, 0)
    l = 0
    res = len(s) + 1
    output = ""
    need = len(t)
    found = 0
    for r in range(len(s)):
        sc[s[r]] = 1 + sc.get(s[r], 0)
        if s[r] in tc and sc[s[r]] <= tc[s[r]]:
            found += 1
        while l <= r and found == need:
            if (r - l + 1) < res:
                res = (r - l + 1)
                output = s[l: r+1]
            sc[s[l]] -= 1
            if s[l] in tc and sc[s[l]] < tc[s[l]]:
                found -= 1
            l += 1
    return output


