def isAnagram(s, t):
    # Easy: Check same length, then use dicts to store counts of 
    # each character, finally check counts are the same, O(n) 
    if len(s) != len(t):
        return False
    sc = {}
    tc = {}
    for i in range(len(s)):
        sc[s[i]] = 1 + sc.get(s[i], 0)
        tc[t[i]] = 1 + tc.get(t[i], 0)
    for ch in s:
        if ch not in t or sc[ch] != tc[ch]:
            return False
    return True
    
