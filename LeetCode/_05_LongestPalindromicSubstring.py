"""
We are asked to find the largest palindromic substring of a given string.

Solution 1:
    First let us consider how to find a palindrome:
    - One method is to start in the middle/centre and move symmetrically outwards (radially), this way
    we can identify sub-string palindromes to help us find the longest one.
    - Using this, we can move along the string and find the largest palindrome substring starting from each
    character/ characters (depending on odd of even cases)
    - Note that this method would take O(n^2) time to run

Solution 2:
    - We can find the solution to this in O(n) time using Manacher's algorithm, taking advantage
    of sub-palindromes that occur inside palindromes.
    - This only works for odd length strings, so to ensure this, we insert a dummy character between
    letters and at the start and end.

        e.g     "abaaba" -> "| a | b | a | a | b | a |"

    - We will create a LPS (the longest palindrome substring) array with len(s)*2 + 1 spaces

        e.g     String S:  " |  a  |  b  |  a  |  a  |  b  |  a  |"
                LPS    L:   [0, 1, 0, 3, 0, 1, 6, 1, 0, 3, 0, 1, 0]
                Pos    i:   [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

        We can interpret this as, LPS[i] = l meaning either substring from position (i-l)
        to position (i+l) is a palindrome of length l (this is neglecting the "|" dummy terms),
        or we can say substring from index (i-l)/2 to (i+l)/2-1 is a palindrome of length l.

    - Our task is to create this LPS array in one pass O(n) time. We do this by identifying the
    situations where LPS values about some centre position are symmetric, and so we do not need
    to calculate the new LPS values to the right of the centre as they will be the same as those
    to the left which are already calculated.

        r: our current right pointer where L[r] is unknown
        l: our current left pointer, which corresponds to r, l=2*c - r
        c: centre pointer L[c]=d
        cr: right of centre pointer where cr = c+d
        cl: left of centre pointer where cl = c-d
        i_l: palindrome at cl
        i_r: palindrome at cr

    - If we know L[c] = d, then we know s[c-d:c+d+1] is a palindrome.

    Case  1
     Set L[r] = L[l]
    - i_l palindrome is completely contained in our centre palindrome
    - i_l palindrome is not a prefix of our centre palindrome
    - These conditions are satisfied when L[l] < (cr-r)

    Case 2
    Set L[r] = L[l]
    - i_l is a prefix of centre palindrome
    - centre palindrome is a suffix
    - These conditions are satisfied when L[l] = (cr-r) AND cr=2*N

    Note in Case 1 and Case 2, the i_r palindrome simply cannot expand more than the i_l one, that is why
    L[r] = L[l], i_l and i_r are contained within the current "centre palindrome" we are evaluating about.

    Case 3:
    L[r] >= L[l]
    - i_l is a prefix of the centre palindrome (and so completely contained)
    - centre palindrome is not a suffix of input string
    - These conditions are satisfied when L[l] = (cr-r) AND cr < 2*N
    - In this case there is the possibility that i_r can expand beyond i_l

    Case 4:
    L[r] >= cr-r
    - i_l is not completely contained in centre palindrome (ie not a prefix of palindrome)
    - This conditions is met when L[l] > cr-r
    - In this case, i_r is at least (cr-r) and could possibly expand

    Finally:
    - We compute the LPS values for L[r] based off of some current centre position c.
    - We change c -> r if the palindrome centred at r expands beyond cr.
"""


# Solution 1
# For even palindrome, r = l+1 to start
# For odd palindrome, r = l to start
def get_palindrome(s, l, r):
    while l >= 0 and r <= len(s)-1 and s[l] == s[r]:
        l -= 1
        r += 1
    return s[l+1:r]


def get_longest_palindrome(s):
    longest = ""
    for l in range(len(s)):
        palindrome = get_palindrome(s, l, l)
        if len(palindrome) > len(longest):
            longest = palindrome
        palindrome = get_palindrome(s, l, l+1)
        if len(palindrome) > len(longest):
            longest = palindrome
    return longest


# Solution 2
def manacher_algo(s):
    # Return string is 1 ch or less
    if len(s) <= 1:
        return len(s)
    # Setup new string p and initial LPS array
    p = ""
    for ch in s:
        p += "|"+ch
    p += "|"
    print("String:", p)
    lps = [0]*len(p)
    lps[1] = 1
    c = 1
    r = 2
    # i is index of centre of biggest palindrome, b is its length
    i = 0
    b = 0
    while r < len(p):
        l = 2*c - r
        cr = c + lps[c]
        diff = cr - r
        if lps[l] < diff:
            lps[r] = lps[l]
        elif lps[l] == diff and cr == len(p)-1:
            lps[r] = lps[l]
        else:
            lps[r] = min(lps[l], diff)
            new_r = get_new_palindrome(p, r - lps[r], r + lps[r])
            lps[r] = new_r - r
            c = r
        if lps[r] > b:
            b = lps[r]
            i = r
        r += 1
    print("LPS Array:", lps)
    print("LPS:", end=" ")
    if i % 2 == 1:
        print(s[(i-1)//2 - b//2: (i-1)//2 + b//2 + 1])
    else:
        print(s[(i-1)//2 - b//2 + 1: (i-1)//2 + b//2 + 1])


def get_new_palindrome(s, l, r):
    while l > 0 and r < len(s)-1 and s[l-1] == s[r+1]:
        l -= 1
        r += 1
    return r


# Clean implementation
def clean_algo(s):
    t = "#".join("^{}$".format(s))
    lps = [0]*len(t)
    c = 0
    cr = 0
    i = 0
    for r in range(1, len(t)-1):
        diff = cr-r
        if diff > 0:
            lps[r] = min(diff, lps[(2*c)-r])
        while t[r + lps[r] + 1] == t[r - lps[r] - 1]:
            lps[r] += 1
        if lps[r] > lps[i]:
            i = r
        if lps[r] > diff:
            c = r
            cr = c + lps[c]
    print("String:", t)
    print("LPS Array:", lps)
    print("Longest substring:", t[i - lps[i]: i + lps[i] + 1])
    return s[(i-lps[i])//2: (i+lps[i])//2]
