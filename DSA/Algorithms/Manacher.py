"""
We want to find longest palindrome in a string in O(n) time.

    "a b a x a b a x a b y b a x a b y b "

The first thing to do is transform the sting in something we can work with, we do this by adding dummy characters
between every character and put outer bounds the give the outer dummy characters and 0 length. This allows us to
consider both the even and odd cases.

    s = "^#a#b#a#x#a#b#a#x#a#b#y#b#a#x#a#b#y#b#$"

Now we want to create an LPS (longest palindrome substring) array.

    LPS, p = [ 0, 0, ....., 0] with length len(s)

We will update this array to give us useful information when finding the next place to search for a palindrome. It
will contain the length of the palindrome centered at the index. This is very useful as it allows us to find the
next centre position to check using mirror properties of palindromes.

Let

    c = 0, the centre of the current palindrome
    cr = 0, the centre of a palindrome to the right of c

We want to iterate through the string in one pass, updating the LPS array, p as we go, starting at the first
# and ending at the last #.

Consider the partially filled out LPS array

    s = " ^ # a # b # a # x # a # b # a # x # a # b # y # b # a # x # a # b # y # b # $ "
    p = [ 0 0 1 0 3 0 1 0 7 ...

    We have solved for c=9 from index 0 - 16 and the palindrome now ends at index 17 x.

    We now want to find the next centre position to test from, so try cr=10 #, we then look at the mirror of this
    palindromes centre, at index 8, p[8]=0 and is contained within the palindrome at c=9, hence we know that
    the palindrome at index 10 is also of length 0, so p[10]=0

    Try cr=11, s[11]=a, p[7]=1, this is fully contained in palindrome at c=10 so p[11]=1

    Try cr=12, s[12]=#, p[6]=0, ... p[12]=0

    Try cr=13, s[13]=b, p[5]=3, in this case we have both the prefix and suffix "# a # b # a #" for the centre c,
    ie the cr palindrome reaches the right edge and its mirror reaches the left edge, in this case, we have the
    potential to expand the palindrome at cr beyond this limit and so must consider it for the next palindrome.

        Set p[13]=3 and start expanding the palindrome

            s = " ^ # a # b # a # x # a # b # a # x # a # b # y # b # a # x # a # b # y # b # $ "
            p = [ 0 0 1 0 3 0 1 0 7 0 1 0 3 ...

            we would expand around index 13 s[13]=b p[13]=3 and find this palindromes length

            s = " ^ # a # b # a # x # a # b # a # x # a # b # y # b # a # x # a # b # y # b # $ "
            p = [ 0 0 1 0 3 0 1 0 7 0 1 0 9 ...             .

            so we found this to be on length 9, now we just continue the process from before, filling in the next
            lps values from the mirror palindromes until we find the next centre to expand about.


            There are 4 cases to consider:
                1. Mirror is completely contained within the palindrome, ignore
                2. Current palindrome expands to the end of input, ignore
                3. Palindrome expands to right edge and mirror expands to left edge, this is the new centre case
                4. Palindrome expands to right edge and mirror expands beyond left edge, ignore

"""


def manacher(s):
    ss = "#".join("^{}$".format(s))
    p = [0] * len(ss)
    c = 0
    cr = 1
    while cr < len(ss)-1:
        r = c + p[c]
        cl = 2*c - cr
        dist = r - cr
        p[cr] = min(p[cl], dist)   # min in this case ensure we can complete the LPS array and not go out of index range
        """
        This while loop may look like it is just finding the palindrome under every iteration, cause O(n^2).
        
        However, for sub-palindromes that already have their mirror calculated in the array, it will simply do 1 extra
        character check and fail, therefore not doing the loop.
        
        Hence, only when we are checking a sub-palindrome that expands beyond the current right edge of the current 
        palindrome centered on c, will it loop further.
        
        We could write some logic to skip the cases of contained sub-palindromes, however, it is faster to just do the
        initial condition check of the while loop.
        """
        while ss[cr + 1 + p[cr]] == ss[cr - 1 - p[cr]]:
            p[cr] += 1
        if p[cr] > dist:
            c = cr
        cr += 1
    return p


s = "abaxabaxabybaxabyb"
print(manacher(s))

