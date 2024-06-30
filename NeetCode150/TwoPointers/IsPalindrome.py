def isPalindrome(s):
    # Easy: simply left most and right most points must be the same as 
    # we converge to center. For edge cases / sentences, we only 
    # consider lower case a-z values.
    # Use ch.isalnum() to tell if character or string is alphanumeric
    s = s.lower()
    l = 0 
    r = len(s)-1
    while l < r:
        while l < r and not s[l].isalnum():
            l += 1
        while l < r and not s[r].isalnum():
            r -= 1 
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1
    return True

def myalnum(ch):
    return (ord("a") <= ord(ch) <= ord("z") or
            ord("A") <= ord(ch) <= ord("Z") or
            ord("0") <= ord(ch) <= ord ("9"))