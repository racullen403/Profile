"""
In our example of converting an integer to some base string, we used a stack to hold the
results on each iteration and then pop them after to get the final result. This is very
similar to how a recursive function call works:

    A "stack frame" handles the local variables of the function and each call is
    pushed onto the last in the stack. In this way we get a stack where each "block"
    holds the function call and the local variable for that function, and the return
    value for that call is pushed on top of the stack into the next "block".

    Eventually as the state changes and gets to the base case, we will push a single return
    result (base case) to the top of the stack. This final value can then be used in place
    of the function call in the "block" below it, which will give a new result, which can
    be used again in place of the function call below that, and so on until we get the
    final result


    E.G. Sum List Recursively f([1,2,3,4])

            STACK FRAME
        ------------------
        BASE CASE
        f[1]
            =   1
        ------------------
        BLOCK 3
        f[1,2]
            =   f[1] + 2            ---> 1+2=3
        ------------------
        BLOCK 2
        f[1,2,3]
            =   f[1,2] + 3          ---> 3+3=6
        ------------------
        BLOCK 1
        f[1,2,3,4]
            =   f[1,2,3] + 4        --->6+4=10
        ------------------

        We see the stack frame is built up with the function call and the
        return result, if we have a recursive call then it is added on top of the stack
        as its own function call and so on until we get the base case, then the stack
        will collapse using each result to solve the next block. Note that local variable
        will also be stored in each block.
"""