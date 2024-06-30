""" 
We say our "normal" representation of operators is infix

    A+B, A*B, etc... 
    
The Postfix equivalent would be  AB+ (meaning A+B) and AB* (A*B)

And the Prefix would be +AB or *AB 


We know that the operators have their own order of precedence, and we must use parenthesis to dictate
our own custom order

    e.g A*B+C*D by default precedence would be (A*B)+(C*D) and to change this we would have to 
        fully parenthesis the expression.
        
Using Postfix or Prefix allows us to dictate the order of precedence of the operators without having 
to fully parenthesis the expression. 

    e.g Postfix AB*CD*+ is the same as (A*B)+(C*D)
        
        Prefix +*AB*CD      (think of this as +(*AB)(*CD))
        

We can convert fully parenthesised infix expressions to post and prefix using the fact that each 
operation will be enclosed in its own parenthesis.


Consider for Postfix:

    ( ( A * B + C ) + ( D * E ) )
    
    output = "", op_s = []
    
    We add our operands to the output, our left parenthesis to the op_s, and our operators to the
    op_s, however, we first pop any operators that have higher or equal precedence and add to the
    output, if ")", we pop all the operators to the output until we pop the corresponding "(".

    output = "AB", op_s = [(, (, *]  and now we come across "+"
    
    "*" has a higher precedence than "+" so we must pop "*" into the output. Continuing.

    output = "AB*C", op_s = [(, (, +] and we come across ")"
    
    We must pop all operators into the output until we reach the corresponding "(".

    output = "AB*C+", op_s = [(], Continuing.

    output = "AB*C+DE", op_s = [(, +, (, *] and now we come across ")". So pop all operators until "("

    output = "AB*C+DE*", op_s= [(, +] and we come to the last ")" ...

    output = "AB*C+DE*+", op_s = []. DONE!!!
    
"""


def postfix_expression(string):
    output = ""
    op_s = []
    operators = ["+", "-", "*", "/"]
    precedence = {"+": 0, "-": 0, "*": 1, "/": 1}
    for i in range(len(string)):
        # If ch is "(" we push into stack
        if string[i] == "(":
            op_s.append(string[i])
        # If ch is ")" we pop out all operators until next "(" into the output
        elif string[i] == ")":
            while len(op_s) > 0 and op_s[-1] != "(":
                output += op_s.pop()
            op_s.pop()
        # If ch is an operator, and there is an operator of higher or equal precedence preceding it,
        # we pop previous operator into the output and push current one into stack, else we just
        # push the operator into the stack
        elif string[i] in operators:
            if len(op_s) > 0 and op_s[-1] in operators and precedence[op_s[-1]] >= precedence[string[i]]:
                output += op_s.pop()
                op_s.append([string[i]])
            else:
                op_s.append(string[i])
        # If ch is " ", ignore it, makes output prettier
        elif string[i] == " ":
            pass
        # Finally add any remaining ch to the output
        else:
            output += string[i]
    # We dump remaining operators into the output
    while len(op_s) > 0:
        output += op_s.pop()
    return output


def example1():
    s1 = "((A*B)+(C*D))"
    s2 = "( A + B ) * ( C + D )"
    s3 = "( A + B ) * C"
    s4 = "A + B * C"
    lst = [s1, s2, s3, s4]
    for i in lst:
        print(postfix_expression(i))


""" 
Working Example of a post fix expression:

    Consider 4 5 6 * +  
    
    stack=[4]
    stack=[4,5]
    stack=[4,5,6]   we now see a *, this tells us to multiply the last 2 operands 
    stack=[4,30]    we now see a +, this tells us to add the last 2 operands 
    stack=[34]      DONE!!!
    
"""
import operator as op


# Terms are separated by " " delimiter
def postfix_math(string):
    terms = string.split(" ")
    s = []
    operators = {"+": op.add, "-": op.sub, "*": op.mul, "/": op.truediv}
    for i in terms:
        if i in operators:
            t1 = s.pop()
            t2 = s.pop()
            t3 = operators[i](t2, t1)
            s.append(t3)
        else:
            s.append(int(i))
    return s.pop()


def example2():
    ex1 = "4 5 6 * +"
    ex2 = "25 5 / -5 *"
    ex3 = "7 8 + 3 2 + /"
    lst = [ex1, ex2, ex3]
    for i in lst:
        print(postfix_math(i))
