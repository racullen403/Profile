def encode(strs):
    # Medium: Enode strings together with n# between to indicate new 
    # word of length n following #
    res = ""
    for s in strs:
        res += str(len(s)) + "#" + s  # "n#stringn#string..."
    return res 

def decode(s):
    res = [] 
    i = 0
    while i < len(s):
        j = i   # start of integer
        while s[j] != "#":
            j += 1  # ends at the # after integer
        length = int(s[i:j])    # convert to length
        res.append(s[j+1:j+1+length])   # add string following # of length
        i = j + 1 + length  # move i to start of next integer
    return res




