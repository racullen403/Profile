"""
Medium: Given a string s, split it into substrings where every substring is a palindrome. Return all possible lists of palindromic substrings.

Sol:
    - Create a palindrome checker. Then using backtracking, we can simply create strings of increasing length, if they form a palindrome, 
    add it to a list that carries over and start again from next position.
"""

def partition(s):
    res = [] 

    def backtrack(i, subset):
        if i == len(s): # At the end so have a complete list
            res.append(subset.copy())
        for j in range(i, len(s)):  # Iterate through, increasing length of string we check
            if isPalindrome(i, j):
                subset.append(s[i: j+1])    # Its a palindrome so add to list and carry forward
                backtrack(j + 1, subset)
                subset.pop()    # Remove previous palindrome and try for a new length
        
    def isPalindrome(i, j):
        while i < j and s[i] == s[j]:
            i += 1
            j -= 1
        return i >= j
    
    backtrack(0, [])
    
    return res
        
def test():
    s = "aab"
    print(partition(s))

