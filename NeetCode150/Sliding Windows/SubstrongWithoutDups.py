def lengthOfLongestSubstring(s):
    # Medium: Keep track of letters and there index in hashmap and the start of the subsrting with l.
    # If we find a letter in the hashmap and it is in current substring then update l to this duplicate 
    # position to start the new substring without dups.
    letters = {}
    l = 0
    longest = 0
    for r in range(len(s)):
        if s[r] in letters and letters[s[r]] >= l:
            l = letters[s[r]] + 1
        letters[s[r]] = r 
        longest = max(longest, r - l + 1)
    return longest