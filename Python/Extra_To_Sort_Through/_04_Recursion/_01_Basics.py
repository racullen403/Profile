"""
Recursion is the method of solving a problem by breaking it down into smaller sub-problems,
these sub-problems will eventually reach a base case where it can be solved, then the
solution is used to solve the previous sub-problem, and so on until a complete solution
is found.

This usually involves calling the function itself again.

Consider a basic list summation:
"""


def list_sum(mylist):
    total = 0
    for i in mylist:
        total += i
    return total


# Recursively
def recursive_list_sum(mylist):
    if len(mylist) == 1:
        return mylist[0]
    return mylist.pop() + recursive_list_sum(mylist)


# a = [1, 2, 3, 4, 5]
# print("Normal Summation of a={}, ".format(a), list_sum(a))
# print("Recursive Summation of a={}, ".format(a), recursive_list_sum(a))

"""
Consider recursive_list_sum(mylist):

    On every iteration we are popping the last term out of the input list and adding it 
    to the final summation, eventually we get to recursive_list_sum([1]), this is the base 
    case with one item left and is returned. 
    
    e.g f is just recursive_list_sum
    
        1.  f([1,2,3,4]) = 4 + f([1,2,3])
        2.  f([1,2,3]) = 3 + f([1,2])
        3.  f([1,2]) = 2 + f([1])
        
        4.  f([1]) = 1      BASE CASE FOUND
        
        5.  f([1,2]) = 2 + 1 = 3
        6.  f([1,2,3]) = 3 + 3 = 6
        7.  f([1,2,3,4]) = 4 + 6 = 10
        
        DONE
        
        
Recursion Algorithms must obey 3 laws:

    There must be a BASE CASE (condition that stops the algorithm recursing)
    The state must change and move towards the base case 
    The algorithm must call itself recursively
"""


def factorial(n):
    fact = 1
    while n > 1:
        fact *= n
        n -= 1
    return fact


def recursive_fact(n):
    if n <= 1:
        return 1
    return n * recursive_fact(n-1)

# a = [1, 2, 3, 4, 5, 6]
# for i in a:
#     print("\nFactorial {}: ".format(i), factorial(i))
#     print("Recursive Factorial {}: ".format(i), recursive_fact(i))