""" 
We say our "normal" representation of operators is infix

    A+B, A*B, etc... 
    
The Postfix equivalent would be  AB+ (meaning A+B) and AB* (A*B)

And the Prefix would be +AB or *AB 


We know that the operators have their own order of precedence and we must use parenthesis to dictate 
our own order 

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
from _01_Stack import Stack


def postfix_expression(string):
    output = ""
    op_s = Stack()
    operators = ["+", "-", "*", "/"]
    precedence = {"+": 0, "-": 0, "*": 1, "/": 1}
    for i in range(len(string)):

        # If ch is "(" we push into stack
        if string[i] == "(":
            op_s.push(string[i])

        # If ch is ")" we pop out all operators until next "(" into the output
        elif string[i] == ")":
            while op_s.peek() != "(":
                output += op_s.pop()
            op_s.pop()

        # If ch is an operator, and there is an operator of higher or equal precedence preceding it,
        # we pop previous operator into the output and push current one into stack, else we just
        # push the operator into the stack
        elif string[i] in operators:
            if not op_s.is_empty() and op_s.peek() in operators and precedence[op_s.peek()] >= precedence[string[i]]:
                output += op_s.pop()
                op_s.push([string[i]])
            else:
                op_s.push(string[i])

        # If ch is " ", ignore it, makes output prettier
        elif string[i] == " ":
            pass

        # Finally add any remaining ch to the output
        else:
            output += string[i]

    # We dump remaining operators into the output
    while not op_s.is_empty():
        output += op_s.pop()

    return output

# s1 = "((A*B)+(C*D))"
# s2 = "( A + B ) * ( C + D )"
# s3 = "( A + B ) * C"
# s4 = "A + B * C"
# lst = [s1, s2, s3, s4]
# for i in lst:
#     print(postfix_expression(i))


""" 
A great way of understanding Postfix is as follows:

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
    s = Stack()
    operators = {"+": op.add, "-": op.sub, "*": op.mul, "/": op.truediv}
    for i in terms:
        if i in operators:
            t1 = s.pop()
            t2 = s.pop()
            t3 = operators[i](t2, t1)
            s.push(t3)
        else:
            s.push(int(i))
    return s.pop()

ex1 = "4 5 6 * +"
ex2 = "25 5 / -5 *"
ex3 = "7 8 + 3 2 + /"
lst = [ex1, ex2, ex3]
for i in lst:
    print(postfix_math(i))