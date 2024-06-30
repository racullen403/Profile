"""
Count-and-say is a sequence of digit strings defined as follows:

    - countAndSay(1) = "1"
    - countAndSay(n) is the way you would say the digit string from countAndSay(n-1)

    e.g     n = 1       "1"         Base Case
            n = 2       "11"        one 1
            n = 3       "21"        two 1's
            n = 4       "1211"      one 2 and one 1




"""


# With Recursion
def count_and_say(n):
    if n == 1:
        return "1"
    else:
        l = 0
        r = 0
        temp = []
        say = ""
        s = count_and_say(n-1)
        while l < len(s):
            if l == len(s):
                return say
            while r < len(s) and s[l] == s[r]:
                r += 1
            temp.append(str(r-l))
            temp.append((s[l]))
            l = r
        return say.join(temp)


# Without Recursion:
def count_and_say_2(n):
    say = "1"
    for _ in range(n-1):
        l, r, new_say, temp = 0, 0, "", []
        while l < len(say):
            while r < len(say) and say[l] == say[r]:
                r += 1
            temp.append(str(r-l))
            temp.append(say[l])
            l = r
        say = new_say.join(temp)
    return say
