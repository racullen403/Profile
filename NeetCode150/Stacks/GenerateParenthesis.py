def generateParenthesis(n):
    # Medium: Simply add ) and ( to current string, keeping track of the left and right parenthesis 
    # counts. If r ever exceeds l then terminate that string. If we reach l == r == n then we have 
    # generated a valid string. Use a stack to hold all possible solutions and pop each time, then
    # create then new solutions and add back in. Continue until stack is empty.
    res = [] 
    stack = [["(", 1, 0]]
    while stack:
        check = stack.pop()
        s = check[0]
        l = check[1]
        r = check[2]
        if l == n and  r == n:
            res.append(s)
        elif l <= n and r <= n and l >= r:
            stack.append([s + "(", l + 1, r])
            stack.append([s + ")", l, r + 1])
    return res

