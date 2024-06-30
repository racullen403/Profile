def evalRPN(tokens):
    # Medium: only trick part is remembering the order you are popping elements and truncating division.
    stack = [] 
    for ch in tokens:
        if ch == "+":
            a = stack.pop()
            stack[-1] += a
        elif ch == "-":
            a = stack.pop()
            stack[-1] -= a
        elif ch == "*":
            a = stack.pop()
            stack[-1] *= a
        elif ch == "/":
            a = stack.pop()
            b = stack.pop()
            stack.append(int(b/a))
        else:
            stack.append(int(ch))
    return stack[0]

