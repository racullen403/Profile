def isValid(s):
    # Easy: add open parenthesis to stack, if its a closed, then check the stack isnt empty and check 
    # the last term in the stack is the correct opening, then pop. If stack empty at end, then valid.
    lookup = {"]": "[",
            "}": "{",
            ")": "("}
    stack = [] 
    for ch in s:
        if ch in lookup.values():
            stack.append(ch)
        elif not stack:
            return False
        else:
            p = stack.pop() 
            if lookup[ch] != p:
                return False
    return stack == []
